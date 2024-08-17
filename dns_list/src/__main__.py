from src.zones import Zones
from src.block import Block
from src.group import Group

levels = ["high", "low"]


def main():
    records: list[Group] = [Zones(), Block()]

    for group in records:
        group.dump()


if __name__ == "__main__":
    main()
