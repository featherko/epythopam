"""Getting geocode for addresses."""
import asyncio
from typing import Union

import geopy
from async_lru import alru_cache
from final.fre.api_key import my_key
from final.fre.pony_db import Flat, db_bind
from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import GoogleV3
from pony.orm import commit, db_session


class GeoParse:
    """Class for geocode.

    Used to get geocode for each address in database
    """

    def __init__(self, api_key: str):
        self.sem = None
        self.lock = None
        self.queue = None
        self.api_key = api_key
        self.geocoder = None

    async def parse(self) -> None:
        """Start parse.

        Create list of tasks.  Closes tasks once queue is empty.
        """
        self.sem = asyncio.Semaphore(20)
        self.lock = asyncio.Lock()
        self.queue = asyncio.Queue(maxsize=100)
        tasks = [asyncio.ensure_future(self.parse_flat()) for _ in range(40)]
        async with GoogleV3(
            api_key=self.api_key, adapter_factory=AioHTTPAdapter
        ) as self.geocoder:
            await self.produce()
            await self.queue.join()
            for t in tasks:
                t.cancel()

    async def parse_flat(self) -> None:
        """Geocode gather.

        Getting flat id from queue. Uses it to access to address. Writes it into db, if return from geocode not Falsy.
        Prints, if failed to gather geo for given flat.
        """
        while True:
            with db_session:
                flat_id = await self.queue.get()
                f = Flat[flat_id]
                loc = await self.geocode(query=f.address)
                if loc:
                    f.geo_lat, f.geo_long = loc.latitude, loc.longitude
                    async with self.lock:
                        commit()
                    print(f)
                else:
                    print("Failed", f)
                self.queue.task_done()

    @alru_cache(maxsize=8)
    async def geocode(self, query: str) -> Union[None, geopy.location.Location]:
        """Get geocode.

        :param query: given address
        :return: None, if location not found, Otherwise Location class from geopy.location
        Can be iterated over as (location<String>, (latitude<float>, longitude<Float))
        """
        async with self.sem:
            return await self.geocoder.geocode(
                query=query, exactly_one=True, timeout=10
            )

    async def produce(self) -> None:
        """Add to queue.

        Adds new Flat id to queue, to run for tasks.
        """
        with db_session:
            for f in Flat.select(geo_long=None).order_by(Flat.location):
                await self.queue.put(f.id)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    db_bind()
    asyncio.run(GeoParse(api_key=my_key()).parse())
