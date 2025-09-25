import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[Error] - Usage: Python3 convert.py <Number>")
        sys.exit(1)
    arg = sys.argv[1]
    try:
        print(f"{float(arg)}")
    except ValueError:
        print("[Error] - Esse não é um número válido!")
