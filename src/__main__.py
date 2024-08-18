from .zones import Zones
from .block import Block
from .group import Group

levels = ["high", "low"]


def main():
    records: list[Group] = [Zones(), Block()]

    for group in records:
        group.dump()


if __name__ == "__main__":
    main()
