from redis import Redis
from os import environ
from os.path import join
from json import load

MAX_TTL = 4294967295


class Group:

    def __init__(self) -> None:
        self.list: list
        self.low_raw: dict
        self.high_raw: dict
        self.name: str
        self.to_redis: function
        self.get_raw()

    def insert_values(self, r: Redis):
        for value in self.list:
            self.to_redis(r, value)

    def get_raw(self):
        self.low_raw = load(open(join("low", f"{self.name}.json"), encoding="utf-8"))
        if environ["level"] != "high":
            return
        self.high_raw = load(open(join("high", f"{self.name}.json"), encoding="utf-8"))

    @classmethod
    def merge_high_decorator(cls, func):

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                ...

        return wrapper
