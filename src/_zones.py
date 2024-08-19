low = [
    # safe search | strict mode
    {
        # google & youtube
        "host": "(w{3}\.)?google\..+",
        "answers": [
            {"type": "CNAME", "answer": "forcesafesearch.google.com"},
        ],
    },
    {
        "host": "((((w{3}\.)?youtube(-nocookie)?)|(m\.youtube)|(youtubei?\.googleapis))\.com)",
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
        "host": "(w{3}\.)?bing.com",
        "answers": [{"type": "CNAME", "answer": "strict.bing.com"}],
    },
    {
        # duckduckgo
        "host": "duckduckgo.com",
        "answers": [{"type": "CNAME", "answer": "safe.duckduckgo.com"}],
    },
]


high = []
