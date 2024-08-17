from dns_list.src.group import Group


def test_group():
    group = TestGroup()
    _test_initializing()


def _test_initializing():

    group = TestGroup()

    assert group.low_list == ["www.google.com"]
    assert group.high_list == ["www.google.com", "www.youtube.com"]


class TestGroup(Group):

    def __init__(self) -> None:
        self.low_list = ["www.google.com"]
        self.high_list = self.low_list + ["www.youtube.com"]

        self.to_string = lambda x: x
        self.to_records = lambda x: [{"host": x, "type": "A", "answer": "127.0.0.1"}]
        self.group_name = "zones list"

        super().__init__()
