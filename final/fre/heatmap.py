"""Making heatmap."""
from typing import Iterable

from final.fre.pony_db import Flat, db_bind
from folium import folium
from folium.plugins import HeatMap
from pony.orm import *


def layer() -> None:
    """Create map with layer.

    Creates map with given data, where f.geo_lat and f.get_long are latitude and longitude respectively, avg(f.ppm) is
    weight for such point on map.
    """
    m = folium.Map(location=[59.93399475, 30.367615217112643])
    query = db_query_hm()
    g = {
        0: "black",
        0.2: "blue",
        0.3: "teal",
        0.4: "green",
        0.5: "yellow",
        0.6: "orange",
        0.7: "red",
    }
    heatmap = HeatMap(query, radius=25, blur=45, gradient=g)
    m.add_child(heatmap)
    m.save("./templates/heatmap.html")


@db_session
def db_query_hm() -> Iterable:
    """Query from db.

    Mostly used to make tests simplified.
    """
    query = select((f.geo_lat, f.geo_long, avg(f.ppm)) for f in Flat if f.geo_lat)
    return query  # noqa: R504


if __name__ == "__main__":
    db_bind()
    layer()
