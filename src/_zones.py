low = [
    # safe search | strict mode
    {
        # google & youtube
        "host": "(www\.google\..+)",
        "answers": [
            {"type": "CNAME", "answer": "forcesafesearch.google.com"},
        ],
    },
    {
        "host": "(((www\.youtube(-nocookie)?)|(m\.youtube)|(youtubei?\.googleapis))\.com)",
        "answers": [{"type": "CNAME", "answer": "restrict.youtube.com"}],
    },
    {
        "host": "forcesafesearch.google.com",
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
    },
    {
        "host": "restrict.youtube.com",
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
    },
    {
        # bing
        "host": "www.bing.com",
        "answers": [{"type": "A", "answer": "204.79.197.220"}],
    },
    {
        # duckduckgo
        "host": "duckduckgo.com",
        "answers": [{"type": "CNAME", "answer": "safe.duckduckgo.com"}],
    },
]


high = []
