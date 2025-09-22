import sys


def downcase_it(string: str) -> str:
    """Downcase it! str to str"""
    return string.lower()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[Error] - Usage: python3 methods.py <str>")
        sys.exit(1)
    args = sys.argv[1:]
    for words in args:
        print(downcase_it(words))
