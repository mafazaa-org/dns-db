from .zones import Zones
from .block import Block
from .group import Group
from sqlite3 import connect
from os import remove
from os.path import join

levels = ["high", "low"]


def main():
    groups: list[Group] = [Zones(), Block()]
    for level in levels:
        db_file = join(level, "lists.db")
        try:
            remove(db_file)
        except FileNotFoundError:
            ...
        conn = connect(db_file)
        crsr = conn.cursor()

        for group in groups:
            group.initialize_db(crsr)
            group.update_db(conn, crsr, level)


if __name__ == "__main__":
    main()
