from .zone import Zone
from sqlite3 import Cursor, Connection


class Group:

    def __init__(self) -> None:
        self.low_list: list
        self.high_list: list
        self.group_name: str
        self.to_string: function = self.to_string
        self.to_records: function
        self.to_db: function
        self.table_schema: list[str]
        self.table2_schema: list[str]
        self.table2_name: str
        self.validate()

    def validate(self):
        self.valid_zones()
        self.valid()

    def valid_zones(self):
        self.map_to_lists(self._valid_zones)

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
        self.map_to_lists(self._valid)

    def _valid(self, list: list, list_name: str):
        for e in list:
            try:
                domain = self.to_string(e)
                if not "." in domain or not domain:
                    raise ValueError()
            except:
                raise Exception(
                    f"found invalid host '{domain}' in {list_name} \n[{self.group_name}]"
                )

    def map_to_lists(self, func):
        func(self.low_list, "low list")
        func(self.high_list, "high list")

    def initialize_db(self, crsr: Cursor):
        crsr.execute(f"CREATE TABLE {self.group_name}({','.join(map(lambda x : f"\n {x} NOT NULL", self.table_schema))});")
        crsr.execute(f"CREATE TABLE {self.table2_name}({','.join(map(lambda x : f"\n {x} NOT NULL", self.table2_schema))});")

    def update_db(self, crsr: Cursor, level : str): ...
    
    def get_list(self, level):
        match level:
            case 'high':
                l = self.high_list
            case 'low':
                l = self.low_list
        
        return map(self.to_db, l)
