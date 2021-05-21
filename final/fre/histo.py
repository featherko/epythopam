"""Making histograms."""
from typing import Generator


import matplotlib.pyplot as plt
import seaborn as sns
from final.fre.pony_db import Flat, db_bind
from pony.orm import *


@db_session
def avg_price_png() -> None:
    """Histogram picture.

    Creates histograms with average flat price in district for each town in given list of cities.
    """
    cities = ["Санкт-Петербург", "Москва", "Екатеринбург"]
    for city in cities:
        query = select((f.district, avg(f.price)) for f in Flat if f.city == city)
        name_query = [x[0] for x in query]
        price_query = [round(x[1] / 10 ** 6, 1) for x in query]
        len_q = len(name_query)
        sns.set()
        plt.figure(figsize=(19, 10.8))
        plt.xlabel("Цены, млн. P")
        plt.ylabel("Районы")
        plt.title(f"{city}, Средние цены по районам")
        plt.hist(
            name_query,
            bins=len_q,
            range=(0, len_q),
            weights=price_query,
            orientation="horizontal",
            align="left",
        )
        plt.savefig(f"./static/{city}")
        plt.show()


def avg_square_png() -> None:
    """Histogram picture.

    Creates histograms with average square metres area in district for each town in given list of cities.
    """
    cities = ["Санкт-Петербург", "Москва", "Екатеринбург"]
    for city in cities:
        query = db_query_hg(city)
        name_query = [x[0] for x in query]
        price_query = [(x[1]) for x in query]
        len_q = len(name_query)
        sns.set()
        plt.figure(figsize=(19, 10.8))
        plt.xlabel("Метраж")
        plt.ylabel("Районы")
        plt.title(f"{city}, Средний метраж по районам")
        plt.hist(
            name_query,
            bins=len_q,
            range=(0, len_q),
            weights=price_query,
            orientation="horizontal",
            align="left",
        )
        plt.savefig(f"./static/{city}_square")
        plt.show()


@db_session
def db_query_hg(city: str) -> Generator:
    """Response from db.

    Mostly used to make tests simplified.
    """
    query = select((f.district, avg(f.square)) for f in Flat if f.city == city)
    return query  # noqa: R504


if __name__ == "__main__":
    db_bind()
    avg_price_png()
    avg_square_png()
