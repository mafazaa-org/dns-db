from test.test_block import main as test_block
from test.test_zones import main as test_zones
from test.test_group import main as test_group


def main():
    test_block()
    test_zones()
    test_group()


if __name__ == "__main__":
    main()
