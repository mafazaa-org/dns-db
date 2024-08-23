from re import match
from sqlite3 import Cursor, Connection
from ._block import *
from .group import Group


class Block(Group):

    def __init__(self):
        self.low_list = low["list"] + ["exampleblock.com"]
        self.high_list = low["list"] + high["list"] + ["exampleblock.com"]

        self.low_regex_contains = low["regex"]["contains"]
        self.low_regex_subdomains = low["regex"]["subdomains"]

        self.high_regex_contains = self.low_regex_contains + high["regex"]["contains"]
        self.high_regex_subdomains = (
            self.low_regex_subdomains + high["regex"]["subdomains"]
        )

        # initialze for group
        self.to_string = lambda x: x
        self.to_records = lambda x: [{"host": x, "type": "A", "answer": "0.0.0.0"}]
        self.to_db = lambda x: (x,)
        self.group_name = "blocklist"
        self.table_schema = ["domain TEXT PRIMARY KEY"]

        super().__init__()

    # set
    def set(self):

        self._set(self.low_regex_contains, "low regex (contains)")
        self._set(self.low_regex_subdomains, "low regex (subdomains)")
        self._set(self.high_regex_contains, "high regex (contains)")
        self._set(self.high_regex_subdomains, "high regex (subdomains)")

        def common_between_regex_and_list(list: list, level: str):

            for domain in list:

                if match(self.low_regex, domain):
                    raise Exception(
                        f"{domain} exists in {level} list while it's already blocked by low.regex \n[{self.group_name}]"
                    )

                if match(self.high_regex, domain):
                    raise Exception(
                        f"{domain} exists in {level} list while it's already blocked by high.regex \n[{self.group_name}]"
                    )

        common_between_regex_and_list(self.high_list, "high")
        common_between_regex_and_list(self.low_list, "low")

    def _set(self, list: list, list_name: str):
        found = []
        for element in list:
            if self.to_string(element) in found:
                raise Exception(
                    f"dublicate of '{element}' in {list_name} \n[{self.group_name}]"
                )
            found.append(self.to_string(element))

    # valid zones
    def valid_zones(self):

        super().valid_zones()
        super()._valid_zones(
            [
                f"www.{reg}.com"
                for reg in self.low_regex_contains + self.high_regex_contains
            ],
            "regex contains",
        )

        super()._valid_zones(
            [
                f"{reg.replace('?', '')}.example.com"
                for reg in self.low_regex_subdomains + self.high_regex_subdomains
            ],
            "regex subdomains",
        )

    @property
    def high_regex(self):
        return self.create_regex(self.high_regex_contains, self.high_regex_subdomains)

    @property
    def low_regex(self):
        return self.create_regex(self.low_regex_contains, self.low_regex_subdomains)

    def create_regex(self, contains: list, subdomains: list):
        return f"(.*({'|'.join(contains)}).*)|((.+\.)?({'|'.join(subdomains)})\..+)"

    def update_db(self, conn: Connection, crsr: Cursor, level: str):
        crsr.executemany(
            f"INSERT INTO {self.group_name} VALUES(?)", self.get_list(level)
        )
        conn.commit()
