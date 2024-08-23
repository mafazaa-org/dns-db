from sqlite3 import Connection, Cursor
from ._zones import *
from .group import Group
from dnslib import QTYPE


TYPE_LOOKUP = {
    "A": QTYPE.A,
    "AAAA": QTYPE.AAAA,
    "CAA": QTYPE.CAA,
    "CNAME": QTYPE.CNAME,
    "DNSKEY": QTYPE.DNSKEY,
    "MX": QTYPE.MX,
    "NAPTR": QTYPE.NAPTR,
    "NS": QTYPE.NS,
    "PTR": QTYPE.PTR,
    "RRSIG": QTYPE.RRSIG,
    "SOA": QTYPE.SOA,
    "SRV": QTYPE.SRV,
    "TXT": QTYPE.TXT,
    "SPF": QTYPE.TXT,
}


class Zones(Group):

    def __init__(self):
        self.low_list = low
        self.high_list = high + low

        self.to_string = lambda x: x["host"]
        self.to_records = lambda x: [
            {"host": x["host"], "type": answer["type"], "answer": answer["answer"]}
            for answer in x["answers"]
        ]
        self.group_name = "zoneslist"
        self.table_schema = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "host TEXT UNIQUE",
        ]
        self.to_db = lambda x: ((x["host"],), x["answers"])
        self.table2_name = "answers"
        self.table2_schema = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "zone_id INTEGER",
            "type INTEGER",
            "answer TEXT",
        ]

        super().__init__()

    def update_db(self, crsr: Cursor, level: str):
        for domain, answers in self.get_list(level):
            crsr.execute(f"INSERT INTO {self.group_name}(host) VALUES(?)", domain)
            domain_id = crsr.execute(
                f"SELECT id from {self.group_name} WHERE host = ?", domain
            ).fetchone()[0]
            answers = map(
                lambda x: (domain_id, TYPE_LOOKUP[x["type"]], x["answer"]), answers
            )
            crsr.executemany(
                "INSERT INTO answers (zone_id, type, answer) VALUES(?, ?, ?)", answers
            )

    # _valid
    def _valid(self, list, list_name: str):

        super()._valid(list, list_name)
        for record in list:
            if len(record["answers"]) < 1:
                raise Exception(
                    f"Found domain '{record['host']}' without answers in {list_name}"
                )
