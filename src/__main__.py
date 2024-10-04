from .zones import Zones
from .block import Block
from .group import Group
from redis import Redis

groups: list[Group] = [Zones(), Block()]
r = Redis()


def insert():
    for group in groups:
        group.insert_values(r)


def update():
    blocks = r.keys("*[^(:1)(:5)(:28)]")


if __name__ == "__main__":
    insert()
