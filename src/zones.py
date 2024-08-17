from _zones import *
from group import Group


class Zones(Group):

    def __init__(self):
        self.low_list = low
        self.high_list = high + low

        self.to_string = lambda x: x["host"]
        self.to_records = lambda x: [
            {"host": x["host"], "type": answer["type"], "answer": answer["answer"]}
            for answer in x["answers"]
        ]
        self.group_name = "zones list"

        super().__init__()

    # _valid
    def _valid(self, list, list_name: str):

        super()._valid(list, list_name)
        for record in list:
            if len(record["answers"]) < 1:
                raise Exception(
                    f"Found domain '{record['host']}' without answers in {list_name}"
                )

    @property
    def file_name(self) -> str:
        return "zones.json"

    @property
    def low_json(self) -> dict:
        return self.low_list

    @property
    def high_json(self) -> dict:
        return self.high_list
