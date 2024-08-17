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
            # WARNING!! inapropriate keywords!!
            "porn",
            "sex",
            "naked",
            "nude",
            "ass",
            "boob",
            "tities",
            "a55hole",
            "breast",
            "dick",
            "pussy",
            "bitch",
            "butt",
            "fuck",
            "anal",
            "blowjob",
            "dildo",
            "xnxx",
            "strip",
            "sweet(chicks|kisses|xladies)",
            "lesbian",
            "phcdn",
            "undress",
            "sxccdn",
            "hentai",
            "ecchi",
            "plus18",
            # nfsw
            "devianart",
            # vpn
            "vpn",
            # ads
            "adsystem",
            # anime/manga/webtoon
            "anime",
            "manga",
            "manhwa",
            "webtoon",
            # alcohol | drugs
            "cocaine",
            "alcohol",
            "beer",
            # unwanted
            "lgbt",
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
