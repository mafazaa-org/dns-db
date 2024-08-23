from .zones import Zones
from .block import Block
from .group import Group
from sqlite3 import connect, PARSE_DECLTYPES, register_adapter, register_converter
from os import remove
from os.path import join
from re import match

levels = ["high", "low"]


def main():
    groups: list[Group] = [Zones(), Block()]
    for level in levels:
        db_file = join(level, "data.db")
        try:
            remove(db_file)
        except FileNotFoundError:
            ...
        conn = connect(db_file, detect_types=PARSE_DECLTYPES)
        register_adapter(bool, int)
        register_converter("BOOLEAN", lambda v: bool(int(v)))

        crsr = conn.cursor()

        for group in groups:
            group.initialize_db(crsr)
            group.update_db(crsr, level)

        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
