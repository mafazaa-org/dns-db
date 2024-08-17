from zone import Zone


class Group:

    def __init__(self) -> None:
        self.low_list: list
        self.high_list: list
        self.to_string: function = extract_www(self.to_string)
        self.to_records: function
        self.group_name: str
        self.validate()

    def validate(self):
        self.set()
        self.sort()
        self.valid_zones()
        self.valid()

    def set(self):
        self.do_for_lists(self._set)

    def _set(self, list: list, list_name: str):
        found = []
        for element in list:
            if self.to_string(element) in found:
                raise Exception(
                    f"dublicate of '{element}' in {list_name} \n[{self.group_name}]"
                )
            found.append(self.to_string(element))

    def sort(self):
        self.do_for_lists(lambda x, y: self._sort(x))

    def _sort(self, list: list):
        list.sort(key=self.to_string)

    def valid_zones(self):
        self.do_for_lists(self._valid_zones)

    def _valid_zones(self, list: list, list_name: str):
        for host in list:
            for record in self.to_records(host):
                try:
                    Zone.from_json(0, record)
                except:
                    raise Exception(
                        f"Can't make a zone for the domain {record['host']} in {list_name} with data: {record['type']}    {record['answer']}   \n[{self.group_name}]"
                    )

    def valid(self):
        self.do_for_lists(self._valid)

    def _valid(self, list: list, list_name: str):
        for e in list:
            domain = self.to_string(e)
            if not "." in domain:
                raise Exception(
                    f"found invalid host '{domain}' in {list_name} \n[{self.group_name}]"
                )

    def do_for_lists(self, func):
        func(self.low_list, "low list")
        func(self.high_list, "high list")


def extract_www(func):
    def wrapper(string: str):
        return func(string).removeprefix("www.")

    return wrapper
