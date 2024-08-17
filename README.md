# Mafazaa-dns-list

This repo is basicly for storing blocklists and zones for mafazaa dns servers. Also I coded some python scripts along with some tests to increase productivity and reduce the amount of errors that could occur while updating the list

the dns servers source code exists at [https://github.com/ahmed-elbehairy7/mafazaa-dns](https://github.com/ahmed-elbehairy7/mafazaa-dns)

## Usage

after cloning the repository, installing dependencies if exists, the `run.bat` command should do it's job perfectely if you run it from the root of the repo, and the same goes for `pytest` if you have it installed

## editing lists

first of all I implemented two levels of protection to the servers, so almost everything you will read should apply to the high and low levels as you can see in `_block.py` and `_zones.py` that there are two variables, high and low

## block lists

as you can see in the `_block.py` file there's two variables, if we focused on any of them we will see that they have the following schema

```json
{
	"list": ["example.com", "another_example.com"],
	"regex": {
		"contains": ["example"],
		"subdomains": ["another_example"]
	}
}
```

So, let's dive into them one by one

### list

the list array contains of specific domains to block, the example above causes the domain example.com to be blocked while allowing another.example.com. It is not implemented yet but probably I will implement the server to ignore the subdomain if it's 'www', which means that the example above will only block www.example.com and example.com, while allowing hello.example.com or any other subdomains

### regex

the regex dict contains two key-values 'contains' and 'subdomains'

#### contains

the 'contains' list means that any domain having a keyword in this list will automaticly be blocked! to for example if we added the `porn` keyword to this list our server is now blocking any domain that include the word 'porn' in it like porhub.com, theporndude.com, pornaddictsanonymous.org, and any other domain contains this keyword

this also means that this list is dangerous, so use it with caution and check if a normal english words contains the keyword you want to add

#### subdomains

some regex patterns like 'ads?' will cause a huge trouble if added to the contains list, and that's exactly why the subdomains list exists to block a domain have the word 'ad' or 'ads' as a subdomain like ads.gadsme.com or ad.doubleclick.net and ...etc.

to demonstrate how dangerous the contains list is than the subdomains, let's put the ads? pattern in the contains list and we will be surprised that `ad`obe.com, `ad`just.com, playstore-network`ad`apter and many other websites are blocked although they're normal websites

## zones list

the zones list schema is as follows

```json
[
	{
		"host": "(www.)?google.+",
		"answers": [
			{ "type": "A", "answer": "1.2.3.4" },
			{ "type": "AAAA", "answer": "1.2.3.4" }
		]
	}
]
```

as you probably noticed the previous example uses regex also! that's because google.com have a lot of domains, and to force them all to safe search in one go without wasting time searching among 150+ google domains like google.cat, google.ea, google.us ...etc.
since the current hosts aren't big we are not conserened with sorting the list or something since it only contains three elements, but this should be addressed in the future if this list grew

## fetching the lists

I belive the easiest way to get the lists from the server is by requesting the raw json file from github directly, so if you need the high level blocklist for the production environment you can fetch this link [https://raw.githubusercontent.com/ahmed-elbehairy7/mafazaa-dns-lists/dev/high/blocklist.json](https://raw.githubusercontent.com/ahmed-elbehairy7/mafazaa-dns-lists/dev/high/blocklist.json)

so the formula is as follows:

https://raw.githubusercontent.com/ahmed-elbehairy7/mafazaa-dns-lists/`{branch}`/`{level}`/`{file}`

for development and testing environments, `exampleblock.com` and `examplezone.com` are added to lists

## py scripts

the python scripts here do some pretty nice stuff automaticly for us like:

-   add the low lists to the high ones programaticlly
-   validate the lists although it's not a very dependable validation but it helps a little
-   generate regex from lists for block lists
-   sorts the data so it's easy to use log n search algorithms on them for the server

## TODO

Add the ability to communicate with the server and fetch the new updated lists from it, then add programaticly add it to the lists here
