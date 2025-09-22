import sys


def shrink(string: str) -> str:
    """Returns the first 8 characters of the string (str->str)"""
    return string[0:8]


def enlarge(string: str) -> str:
    """Return a string bigger than 8, if is smaller it fills with Z until 8"""
    return string.ljust(8, "z")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[Error] - Usage: python3 functions_everywhere.py <str>")
        sys.exit(1)
    args = sys.argv[1:]
    for words in args:
        size = len(words)
        if size > 8:
            print(shrink(words))
        elif size < 8:
            print(enlarge(words))
        else:
            print(words)
