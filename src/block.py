from zone import Zone


class Block:

    def __init__(self):
        low_regex_contains = low["regex"]["contains"]
        low_regex_subdomains = low["regex"]["subdomains"]

        self.low_regex = self.create_regex(low_regex_contains, low_regex_subdomains)

        self.high_regex = self.create_regex(
            low_regex_contains + high["regex"]["contains"],
            low_regex_subdomains + high["regex"]["subdomains"],
        )

        self.low_list = low["list"]
        self.high_list = low["list"] + high["list"]

    def validate(self):
        hosts = []

        hosts.extend(self.high_list)
        hosts.extend(
            [
                f"www.{reg}.com"
                for reg in low["regex"]["contains"] + high["regex"]["contains"]
            ]
        )

        hosts.extend(
            [
                f"{reg.replace('?', '')}.example.com"
                for reg in low["regex"]["subdomains"] + high["regex"]["subdomains"]
            ]
        )

        for domain in hosts:
            Zone.from_json(0, {"host": domain, "type": "A", "answer": "0.0.0.0"})

    @property
    def low_json(self) -> dict:
        return {"list": self.low_list, "regex": self.low_regex}

    @property
    def high_json(self) -> dict:
        return {"list": self.high_list, "regex": self.high_regex}

    @property
    def file_name(self) -> str:
        return "blocklist.json"

    def create_regex(self, contains: list, subdomains: list):
        return f"(.*({'|'.join(contains)}).*)|((.+\.)?({'|'.join(subdomains)})\..+)"


low = {
    "list": [],
    "regex": {
        "contains": [
            "porn",
            "sex",
            "naked",
            "nude",
            "ass",
            "boob",
            "tities",
            "a55hole",
            "breast",
            "cocaine",
            "alcohol",
            "dick",
            "bitch",
            "butt",
            "fuck",
            "anime",
            "anal",
            "blowjob",
            "dildo",
            "xnxx",
            "strip",
            "vpn",
            "sweet(chicks|kisses|xladies)",
            "lesbian",
            "phcdn",
            "adsystem",
            "undress",
            "devianart",
            "sxccdn",
            "lgbt",
        ],
        "subdomains": ["ads?"],
    },
}


high = {
    "list": [],
    "regex": {
        "contains": [
            "tiktok",
            "netflix",
            "spotify",
            "music",
            "soundcloud",
            "egybest",
            "cimaclub",
            "imdb",
        ],
        "subdomains": ["movies?"],
    },
}
