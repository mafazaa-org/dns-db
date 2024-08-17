from zones import Zones
from block import Block
from json import dump
from os.path import join

levels = ["high", "low"]


def main():
    records = [Zones(), Block()]

    for group in records:
        for level in levels:
            with open(join(level, group.file_name), "w", encoding="utf-8") as f:
                dump(get_json(group, level), f)


def get_json(group, level):
    match level:
        case "high":
            return group.high_json
        case "low":
            return group.low_json


if __name__ == "__main__":
    main()
