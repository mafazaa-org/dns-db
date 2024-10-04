from .zones import Zones
from .block import Block
from .group import Group
from redis import Redis
from dnslib import QTYPE


def main():

    groups: list[Group] = [Zones(), Block()]
    r = Redis()

    for group in groups:
        group.insert_values(r)


if __name__ == "__main__":
    main()
