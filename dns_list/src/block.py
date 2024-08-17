from re import match
from ._block import *
from .group import Group


class Block(Group):

    def __init__(self):
        self.low_list = low["list"]
        self.high_list = low["list"] + high["list"]

        self.low_regex_contains = low["regex"]["contains"]
        self.low_regex_subdomains = low["regex"]["subdomains"]

        self.high_regex_contains = self.low_regex_contains + high["regex"]["contains"]
        self.high_regex_subdomains = (
            self.low_regex_subdomains + high["regex"]["subdomains"]
        )

        self.to_string = lambda x: x
        self.to_records = lambda x: [{"host": x, "type": "A", "answer": "0.0.0.0"}]
        self.group_name = "blocklist"

        super().__init__()

    # set
    def set(self):

        self._set(self.low_regex_contains, "low regex (contains)")
        self._set(self.low_regex_subdomains, "low regex (subdomains)")
        self._set(self.high_regex_contains, "high regex (contains)")
        self._set(self.high_regex_subdomains, "high regex (subdomains)")

        super().set()

        for domain in self.high_list:

            if not match(self.low_regex, domain) == None:
                raise Exception(
                    f"{domain} exists in high.list while it's already blocked by low.regex \n[{self.group_name}]"
                )

            if not match(self.high_regex, domain) == None:
                raise Exception(
                    f"{domain} exists in high.list while it's already blocked by high.regex \n[{self.group_name}]"
                )

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
    def low_json(self) -> dict:
        return {**super().low_json, "regex": self.low_regex}

    @property
    def high_json(self) -> dict:
        return {**super().high_json, "regex": self.high_regex}

    @property
    def high_regex(self):
        return self.create_regex(self.high_regex_contains, self.high_regex_subdomains)

    @property
    def low_regex(self):
        return self.create_regex(self.low_regex_contains, self.low_regex_subdomains)

    def create_regex(self, contains: list, subdomains: list):
        return f"(.*({'|'.join(contains)}).*)|((.+\.)?({'|'.join(subdomains)})\..+)"
