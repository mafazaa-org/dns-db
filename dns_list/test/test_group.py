from dns_list.src.group import Group
from pytest import raises
from os.path import join
from json import dump, load


def test_initializing():

    group = __init__()

    assert group.low_list == GroupTest.low_list_init
    assert group.high_list == GroupTest.high_list_init


def test_set():
    group = __init__()
    extra = "www.google.com"
    group.low_list.append(extra)

    with raises(
        Exception,
    ) as excep_info:
        group.validate()

    assert excep_info.type == Exception
    assert (
        excep_info.value.args[0]
        == f"dublicate of '{extra}' in low list \n[{group.group_name}]"
    )


def test_sort():

    for prefix in ["www.", ""]:
        group = __init__()
        host = prefix + "ant.com"

        group.high_list.append(host)

        group.sort()
        assert group.high_list == [host] + group.high_list_init


def test_valid_zones():

    for invalid_domain in [[], 3232, ["hello", "world"], ["hello.com"]]:
        group = __init__()

        group.high_list.append(invalid_domain)

        with raises(Exception) as excep_info:
            group.valid_zones()

        assert excep_info.type == Exception
        assert (
            excep_info.value.args[0]
            == f"Can't make a zone for the domain {invalid_domain} in high list with data: A    127.0.0.1   \n[{group.group_name}]"
        )


def test_valid():
    for invalid_domain in [[], 2323, ["hello"], "hwllo", "", None, "goooooooo"]:
        group = __init__()

        group.high_list.append(invalid_domain)

        with raises(Exception, match=f"found invalid host '.*' in high list"):
            group.valid()


def test_dump():
    group = GroupTest()

    group.dump()


class GroupTest(Group):

    low_list_init = ["www.google.com"]
    high_list_init = low_list_init + ["www.youtube.com"]

    def __init__(self) -> None:
        self.low_list = GroupTest.low_list_init.copy()
        self.high_list = GroupTest.high_list_init.copy()

        self.to_string = lambda x: x
        self.to_records = lambda x: [{"host": x, "type": "A", "answer": "127.0.0.1"}]
        self.group_name = "GroupTest"

        super().__init__()

    def dump(self):
        LEVELS = ["high", "low"]
        jsons = self.jsons
        for level in LEVELS:

            with open(
                join("dns_list", "test", level, self.group_name + ".json"),
                "w",
                encoding="utf-8",
            ) as f:
                dump(jsons[level], f)


def __init__() -> GroupTest:
    return GroupTest()
