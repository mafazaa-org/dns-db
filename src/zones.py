from sqlite3 import Cursor
from ._zones import *
from .group import Group


class Zones(Group):

    def __init__(self):
        self.low_list = low + [
            {
                "host": "examplezone.com",
                "answers": [{"type": "A", "answer": "127.0.0.1"}],
            }
        ]
        self.high_list = (
            high
            + low
            + [
                {
                    "host": "examplezone.com",
                    "answers": [{"type": "A", "answer": "127.0.0.1"}],
                }
            ]
        )

        self.to_string = lambda x: x["host"]
        self.to_records = lambda x: [
            {"host": x["host"], "type": answer["type"], "answer": answer["answer"]}
            for answer in x["answers"]
        ]
        self.group_name = "zoneslist"
        self.table_schema = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]

        super().__init__()

    def initialize_db(self, crsr: Cursor):
        super().initialize_db(crsr)

        answers_schema = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "zone_id INT",
            "type INT",
            "answer TEXT",
        ]
        crsr.execute(f"CREATE TABLE answers({','.join(map(lambda x : f"\n {x} NOT NULL", answers_schema))}, FOREIGN KEY(zone_id) REFERENCES zoneslist(id))")

    # _valid
    def _valid(self, list, list_name: str):

        super()._valid(list, list_name)
        for record in list:
            if len(record["answers"]) < 1:
                raise Exception(
                    f"Found domain '{record['host']}' without answers in {list_name}"
                )
