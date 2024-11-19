from .zones import Zones
from .block import Block
from .group import Group
from redis import Redis
from flask import Flask, request
from re import match

app = Flask(__name__)


def main():
    app.run("localhost", 1212, True)


@app.get("/block/regex")
def block_regex():
    level = request.args["level"]
    return Block(level).get_regex()


@app.post("/update/redis")
def update_redis():
    level = request.args["level"]
    server = request.args["server"]

    groups: list[Group] = [Zones(level), Block(level)]
    r = Redis(server)

    for group in groups:
        group.insert_values(r)

    return {"status": "success"}


@app.post("/update/local")
def update_local():
    level = request.args["level"]
    server = request.args["server"]
    block = Block(level)
    r = Redis(server, decode_responses=True)
    keys = r.keys("*")
    keys = [x for x in keys if (match("^[^:]+$", x) and r.get(x) == "1")]
    if level == "low":
        block.list = keys
        block.update_file()
        return keys
    low_block = Block("low")
    keys = [x for x in keys if not x in low_block.list]
    block.list = keys
    block.update_file()
    return keys


if __name__ == "__main__":
    main()
