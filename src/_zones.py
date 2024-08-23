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
    {
        "host": "high-dns.mafazaa.com",
        "answers": [
            {"type": "A", "answer": "15.184.191.201"},
            {"type": "A", "answer": "15.184.243.155"},
        ],
    },
    {
        "host": "low-dns.mafazaa.com",
        "answers": [
            {"type": "A", "answer": "157.241.6.180"},
            {"type": "A", "answer": "157.241.47.209"},
        ],
    },
    {
        "host": "test-dns.mafazaa.com",
        "answers": [
            {"type": "A", "answer": "15.184.77.248"},
            {"type": "A", "answer": "15.184.210.155"},
        ],
    },
    {
        "host": "init-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "157.175.34.158"}],
    },
    {
        "host": "primary.high-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "15.184.191.201"}],
    },
    {
        "host": "secondary.high-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "15.184.243.155"}],
    },
    {
        "host": "primary.low-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "157.241.6.180"}],
    },
    {
        "host": "secondary.low-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "157.241.47.209"}],
    },
    {
        "host": "primary.test-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "15.184.210.155"}],
    },
    {
        "host": "secondary.test-dns.mafazaa.com",
        "answers": [{"type": "A", "answer": "15.184.77.248"}],
    },
    {
        "host": "mafazaa.com",
        "answers": [
            {"type": "CNAME", "answer": "dog23hurt1ub4.cloudfront.net."},
            {"type": "TXT", "answer": "v=spf1 include:spf.privateemail.com ~all"},
        ],
    },
    {
        "host": "www.mafazaa.com",
        "answers": [{"type": "CNAME", "answer": "dog23hurt1ub4.cloudfront.net."}],
    },
    {
        "host": "_756f122304675a4a8f1b46cd20959f85.mafazaa.com",
        "answers": [
            {
                "type": "CNAME",
                "answer": "_f55a3c6b0b17477fc15ec82f173b1e04.sdgjtdhdhz.acm-validations.aws.",
            }
        ],
    },
    {
        "host": "default._domainkey.mafazaa.com",
        "answers": [
            {
                "type": "TXT",
                "answer": "v=DKIM1;k=rsa;p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2TfiMs9hPl62R+aE1HSfQReYid4AsrY2Aa1gP3i9kdfN7p0mA6CgWW1udTOw7dGUwR3Hs2MeoemPL3J87D9Nbi+Rn60KgBzfSiqbdsR2ZlMCgT0nGc8IYjxy/J1oGmfX3g82SIyK/8EkNj6p2U0YOGqWF2YlTck9VhhC6LBqCRMCFsUGsxQbAXKsk7tUOFZtpcye0A8f2xqjsMahAbrXq0jj5op1CMBxqhi5XeAoDPppip+wRN8+Qdcz+MoC10SG9gqsTHQGOQlPgzAG2BQcxOx8tTZUaMc8V8wU0WSyl23b0hm1BAH70rgFZCiIRW1T1uc7OoYb46QbMoqjuwzfwIDAQAB",
            }
        ],
    },
]


high = []
