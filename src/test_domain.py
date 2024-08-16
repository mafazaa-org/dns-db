def test_domain(domain: str, func: str, test):
    if not test:
        raise Exception(
            f"testing '{domain}' wasn't successfull with the function {func}"
        )
