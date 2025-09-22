import sys

if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("[Error] - Usage: python3 methods.py <str>")
            sys.exit(1)
        args = sys.argv[1]
        print(f"Sao maiusculas? {args.isupper()}", f"E Numerico? {args.isalnum()}", f"E ascii? {args.isascii()}", f"E alphanumerico? {args.isalpha()}", sep="\n")