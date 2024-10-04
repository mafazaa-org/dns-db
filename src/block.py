from re import match
from redis import Redis
from .group import Group, MAX_TTL


class Block(Group):

    def __init__(self):
        self.name = "block"
        super().__init__()
        self.list = self.low_raw["list"]
        self.merge_high()
        self.to_redis = lambda r, value: r.setex(value, MAX_TTL, 1)

    @Group.merge_high_decorator
    def merge_high(self):
        self.list += self.high_raw["list"]

    def create_regex(self, contains: list, subdomains: list):
        return f"(.*({'|'.join(contains)}).*)|((.+\.)?({'|'.join(subdomains)})\..+)"
