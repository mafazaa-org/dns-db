from src.block import Block
from re import match
from test.test_domain import test_domain

ending = ""


def main():
    global ending

    block = Block()

    test_matches(block)
    test_non_matches(block)

    ending = "."

    test_matches(block)
    test_non_matches(block)


def test_matches(block: Block):

    for domain in low_match:
        domain = domain + ending

        test_domain(
            domain,
            "test_block.test_matches (id = 1)",
            match(block.low_regex, domain),
        )
        test_domain(
            domain, "test_block.test_matches (id = 2) ", match(block.high_regex, domain)
        )

    for domain in high_match:
        domain = domain + ending
        test_domain(
            domain, "test_block.test_matches (id = 3) ", match(block.high_regex, domain)
        )


def test_non_matches(block: Block):
    for domain in low_no_match:
        domain = domain + ending
        test_domain(
            domain,
            "test_block.test_non_matches (id = 1) ",
            match(block.low_regex, domain) == None,
        )

    for domain in high_no_match:
        domain = domain + ending

        test_domain(
            domain,
            "test_block.test_non_matches (id = 2) ",
            match(block.high_regex, domain) == None,
        )

        test_domain(
            domain,
            "test_block.test_non_matches (id = 3) ",
            match(block.low_regex, domain) == None,
        )


low_match = [
    "www.pornhub.com",
    "ns500242.ns500249.ns500248.ns500270.ns500250.ns500262.ns500250.ns500213.ns500261.ns500245.ns500225.ns500219.sweetchicksclub.com",
    "ns500242.ns500249.ns500248.ns500270.ns500250.ns500262.ns500250.ns500213.ns500261.ns500245.ns500225.ns500219.sweetkisses.com",
    "ns500242.ns500249.ns500248.ns500270.ns500250.ns500262.ns500250.ns500213.ns500261.ns500245.ns500225.ns500219.sweetxladies.com",
    "www.xnxx.com",
    "xnxx.com",
    "pornhub.com",
    "www.sex.com",
    "sex.com",
    "sex.hello.example.com",
    "naked.com",
    "nude.com",
    "ass.com",
    "ass.sex.com",
    "asses.pornhub.com",
    "tities.com",
    "a55hole.com",
    "breast.pornhub.com",
    "cocaine.alcohol.com",
    "dick.com",
    "www.striphacker.com",
    "ads.google.com",
    "ads.example.com",
    "ad.sex.com",
    "ad.hello.world.com",
    "www.nordvpn.com",
    "secure-vpn.com",
]

high_match = [
    "tiktok.com",
    "www.tiktok.com",
    "tiktok-cdn",
    "movies.example.com",
    "movie.example.com",
    "ad.example.com",
    "ads.example.com",
    "egybest.com",
    "cimaclub.hello",
    "spotify.com",
    "login5.spotify.com",
    "hello.cimaclub.watch",
]

low_no_match = [
    "www.google.ad",
    "www.google.movie",
]

high_no_match = []


if __name__ == "__main__":
    main()
