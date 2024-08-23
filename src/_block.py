low = {
    "list": [
        # porn
        "motherless.com",
        "4chan.com",
        # vpn
        "surfshark.com",
        "privateinternetaccess.com",
        "mullvad.net",
        "www.tunnelbear.com",
    ],
    "regex": {
        "contains": [
            # porn | nudity
            "porn",
            "sex",
            "xnxx",
            "strip",
            "sweet(chicks|kisses|xladies)",
            "phncdn",
            "undress",
            "sxccdn",
            # nfsw
            "devianart",
            # vpn
            "vpn",
            # ads
            "adsystem",
            # anime/manga/webtoon
            "anime",
            "webtoon",
            # alcohol
            "beer",
            # unwanted
            "lgbt",
            "likee",
            "kwai",
            # malware
            "(wmail|fairu|bideo|privatproxy|ahoravideo)-(endpoint|blog|chat|cdn)",
        ],
        "subdomains": [
            # ads
            "ads?",
            "xvideos",
        ],
    },
}


high = {
    "list": [],
    "regex": {
        "contains": [
            # tiktok
            "tiktok",
            # movies
            "netflix",
            "egybest",
            "cimaclub",
            "imdb",
            "cinema",
            "watch",
            "tv",
            "film",
            "movie",
            # music
            "spotify",
            "music",
            "soundcloud",
        ],
        "subdomains": [],
    },
}
