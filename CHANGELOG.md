# CHANGELOG

# v2-pre-alpha

-   returned back to json
-   made a flask app to communicate with the server directly and let both stay updated
-   the db can update the cache of the server directly

## v1-beta

-   transformed from json to sqlite db
-   all data now is stored in ${level}/data.db
-   blocklist is the list of block domains as before
-   blockregex is a list of keywords with the column 'is_subdomain' to differenciate between the two types
-   zoneslist is list of zone hosts with ids
-   answers is a list of answers with a foreign key for it's host

## v0

**Initial release**

-   stores data in json files
-   store list of domains, and a regex as blocklists
-   zone object as a string host and list of answers
