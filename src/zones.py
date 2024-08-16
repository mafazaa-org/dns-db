from zone import Zone


class Zones:

    def __init__(self):
        self.low_regex = low["regex"]
        self.low_match = low["match"]

        self.high_regex = self.low_regex + high["regex"]
        self.high_match = self.low_match + high["match"]

    def validate(self):

        records = []

        for record in self.high_match + self.high_regex:
            for answer in record["answers"]:
                records.append(
                    {
                        "host": record["host"],
                        "type": answer["type"],
                        "answer": answer["answer"],
                    }
                )

        for record in records:
            Zone.from_json(
                0,
                {
                    "host": record["host"],
                    "type": record["type"],
                    "answer": record["answer"],
                },
            )

    @property
    def file_name(self) -> str:
        return "zones.json"

    @property
    def low_json(self) -> dict:
        return {"match": self.low_match, "regex": self.low_regex}

    @property
    def high_json(self) -> dict:
        return {"match": self.high_match, "regex": self.high_regex}


low = {
    "regex": [
        {
            "host": "(www\.google\..+)|(((www\.youtube(-nocookie)?)|(m\.youtube)|(youtubei?\.googleapis))\.com)",
            "answers": [
                {
                    "type": "A",
                    "answer": "216.239.38.120",
                },
                {
                    "type": "AAAA",
                    "answer": "2a00:1450:4006:811::2004",
                },
            ],
        }
    ],
    "match": [
        {
            "host": "www.bing.com",
            "answers": [{"type": "A", "answer": "204.79.197.220"}],
        },
        {
            "host": "duckduckgo.com",
            "answers": [{"type": "CNAME", "answer": "safe.duckduckgo.com"}],
        },
    ],
}

high = {"regex": [], "match": []}
