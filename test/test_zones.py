from dns_lists.src.zones import Zones
from dns_lists.src._zones import *
from dns_lists.src.block import Block
from re import match
from .utils import with_ending
from pytest import raises


def test_initialization():
    low_list = low.copy() + [
        {
            "host": "examplezone.com",
            "answers": [{"type": "A", "answer": "127.0.0.1"}],
        }
    ]
    high_list = high.copy() + low_list

    zones = __init__()

    low_list.sort(key=zones.to_string)
    high_list.sort(key=zones.to_string)

    assert zones.high_list == high_list
    assert zones.low_list == low_list

    # test to string
    assert (
        zones.to_string({"host": "www.google.com", "type": "A", "answer": "0.0"})
        == "google.com"
    )
    assert (
        zones.to_string({"host": "google.com", "type": "A", "answer": "0.0"})
        == "google.com"
    )

    # test to records

    assert zones.to_records(
        {"host": "www.google.com", "answers": [{"type": "A", "answer": "0.0.0.0"}]}
    ) == [{"host": "www.google.com", "type": "A", "answer": "0.0.0.0"}]

    assert zones.to_records(
        {
            "host": "www.google.com",
            "answers": [
                {"type": "A", "answer": "0.0.0.0"},
                {"type": "AAAA", "answer": "::"},
                {"type": "CNAME", "answer": "forcesafesearch.google.com"},
            ],
        }
    ) == [
        {"host": "www.google.com", "type": "A", "answer": "0.0.0.0"},
        {"host": "www.google.com", "type": "AAAA", "answer": "::"},
        {
            "host": "www.google.com",
            "type": "CNAME",
            "answer": "forcesafesearch.google.com",
        },
    ]


def test_valid():
    block = Block()

    invalid_zones = [
        {
            "host": block.to_records(x)[0]["host"],
            "answers": [
                {
                    "type": block.to_records(x)[0]["type"],
                    "answer": block.to_records(x)[0]["answer"],
                }
            ],
        }
        for x in [[], 2323, ["hello"], "hwllo", "", None, "goooooooo"]
    ]

    for invalid_zone in invalid_zones:
        group = __init__()

        group.high_list.append(invalid_zone)

        with raises(Exception, match=f"found invalid host '.*' in high list"):
            group.valid()

    group = __init__()
    group.high_list.append({"host": "some_host.com", "answers": []})
    with raises(
        Exception, match=f"Found domain 'some_host.com' without answers in high list"
    ):
        group.valid()


def test_matches():
    zones = __init__()
    for domain in low_match:
        _test_matches(domain, zones.low_list)
        _test_matches(domain, zones.high_list)

    for domain in high_match:
        _test_matches(domain, zones.high_list)


def test_non_matches():
    zones = __init__()

    for domain in low_no_match:
        _test_matches(domain, zones.low_list, True)
        _test_matches(domain, zones.high_list, True)

    for domain in high_no_match:
        _test_matches(domain, zones.high_list, True)


@with_ending
def _test_matches(domain: str, regex: list, original_found=False, ending=""):
    domain = domain + ending
    found = original_found
    for regex in regex:
        if match(regex["host"], domain):
            found = not original_found

    assert found


low_match = [
    "www.google.com",
    "www.google.ad",
    "www.google.ae",
    "www.google.com.af",
    "www.google.com.ag",
    "www.google.al",
    "www.google.am",
    "www.google.co.ao",
    "www.google.com.ar",
    "www.google.as",
    "www.google.at",
    "www.google.com.au",
    "www.google.az",
    "www.google.ba",
    "www.google.com.bd",
    "www.google.be",
    "www.google.bf",
    "www.google.bg",
    "www.google.com.bh",
    "www.google.bi",
    "www.google.bj",
    "www.google.com.bn",
    "www.google.com.bo",
    "www.google.com.br",
    "www.google.bs",
    "www.google.bt",
    "www.google.co.bw",
    "www.google.by",
    "www.google.com.bz",
    "www.google.ca",
    "www.google.cd",
    "www.google.cf",
    "www.google.cg",
    "www.google.ch",
    "www.google.ci",
    "www.google.co.ck",
    "www.google.cl",
    "www.google.cm",
    "www.google.cn",
    "www.google.com.co",
    "www.google.co.cr",
    "www.google.com.cu",
    "www.google.cv",
    "www.google.com.cy",
    "www.google.cz",
    "www.google.de",
    "www.google.dj",
    "www.google.dk",
    "www.google.dm",
    "www.google.com.do",
    "www.google.dz",
    "www.google.com.ec",
    "www.google.ee",
    "www.google.com.eg",
    "www.google.es",
    "www.google.com.et",
    "www.google.fi",
    "www.google.com.fj",
    "www.google.fm",
    "www.google.fr",
    "www.google.ga",
    "www.google.ge",
    "www.google.gg",
    "www.google.com.gh",
    "www.google.com.gi",
    "www.google.gl",
    "www.google.gm",
    "www.google.gr",
    "www.google.com.gt",
    "www.google.gy",
    "www.google.com.hk",
    "www.google.hn",
    "www.google.hr",
    "www.google.ht",
    "www.google.hu",
    "www.google.co.id",
    "www.google.ie",
    "www.google.co.il",
    "www.google.im",
    "www.google.co.in",
    "www.google.iq",
    "www.google.is",
    "www.google.it",
    "www.google.je",
    "www.google.com.jm",
    "www.google.jo",
    "www.google.co.jp",
    "www.google.co.ke",
    "www.google.com.kh",
    "www.google.ki",
    "www.google.kg",
    "www.google.co.kr",
    "www.google.com.kw",
    "www.google.kz",
    "www.google.la",
    "www.google.com.lb",
    "www.google.li",
    "www.google.lk",
    "www.google.co.ls",
    "www.google.lt",
    "www.google.lu",
    "www.google.lv",
    "www.google.com.ly",
    "www.google.co.ma",
    "www.google.md",
    "www.google.me",
    "www.google.mg",
    "www.google.mk",
    "www.google.ml",
    "www.google.com.mm",
    "www.google.mn",
    "www.google.com.mt",
    "www.google.mu",
    "www.google.mv",
    "www.google.mw",
    "www.google.com.mx",
    "www.google.com.my",
    "www.google.co.mz",
    "www.google.com.na",
    "www.google.com.ng",
    "www.google.com.ni",
    "www.google.ne",
    "www.google.nl",
    "www.google.no",
    "www.google.com.np",
    "www.google.nr",
    "www.google.nu",
    "www.google.co.nz",
    "www.google.com.om",
    "www.google.com.pa",
    "www.google.com.pe",
    "www.google.com.pg",
    "www.google.com.ph",
    "www.google.com.pk",
    "www.google.pl",
    "www.google.pn",
    "www.google.com.pr",
    "www.google.ps",
    "www.google.pt",
    "www.google.com.py",
    "www.google.com.qa",
    "www.google.ro",
    "www.google.ru",
    "www.google.rw",
    "www.google.com.sa",
    "www.google.com.sb",
    "www.google.sc",
    "www.google.se",
    "www.google.com.sg",
    "www.google.sh",
    "www.google.si",
    "www.google.sk",
    "www.google.com.sl",
    "www.google.sn",
    "www.google.so",
    "www.google.sm",
    "www.google.sr",
    "www.google.st",
    "www.google.com.sv",
    "www.google.td",
    "www.google.tg",
    "www.google.co.th",
    "www.google.com.tj",
    "www.google.tl",
    "www.google.tm",
    "www.google.tn",
    "www.google.to",
    "www.google.com.tr",
    "www.google.tt",
    "www.google.com.tw",
    "www.google.co.tz",
    "www.google.com.ua",
    "www.google.co.ug",
    "www.google.co.uk",
    "www.google.com.uy",
    "www.google.co.uz",
    "www.google.com.vc",
    "www.google.co.ve",
    "www.google.co.vi",
    "www.google.com.vn",
    "www.google.vu",
    "www.google.ws",
    "www.google.rs",
    "www.google.co.za",
    "www.google.co.zm",
    "www.google.co.zw",
    "www.google.cat",
    "www.youtube.com",
    "m.youtube.com",
    "youtubei.googleapis.com",
    "youtube.googleapis.com",
    "www.youtube-nocookie.com",
    "www.bing.com",
    "duckduckgo.com",
]

high_match = []

low_no_match = [
    "ads.google.com",
    "analytics.google.com",
    "youtube.com",
    "example.youtube.com",
    "search.google.ad",
]

high_no_match = []


def __init__() -> Zones:
    return Zones()
