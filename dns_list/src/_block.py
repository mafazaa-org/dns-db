low = {
    "list": [
        # porn
        "motherless.com",
        "4chan.com",
        "xvideos.com",
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
        ],
        "subdomains": [
            # ads
            "ads?"
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
