from block import Block
from re import match


def main():
    block = Block()

    test_matches(block)

    test_non_matches(block)


def test_matches(block: Block):
    for domain in low_match:
        assert match(block.low_regex, domain) != None
        assert match(block.high_regex, domain) != None

    for domain in high_match:
        assert match(block.high_regex, domain) != None


def test_non_matches(block: Block):
    for domain in low_no_match:
        assert match(block.low_regex, domain) == None

    for domain in high_no_match:
        assert match(block.high_regex, domain) == None
        assert match(block.low_regex, domain) == None


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

low_no_match = ["www.google.ad", "www.google.movie"]

high_no_match = []


if __name__ == "__main__":
    main()
