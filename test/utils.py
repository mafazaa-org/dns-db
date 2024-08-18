def with_ending(func):
    def wrapper(*args, **kwargs):
        for ending in ["", "."]:
            func(*args, **kwargs, ending=ending)

    return wrapper
