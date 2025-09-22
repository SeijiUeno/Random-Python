import sys

def is_positive(number: int) -> bool:
    """Check if a number is positive."""
    return number > 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[Error] - Usage: python3 classify_number.py <number>")
        sys.exit(1)
    print(is_positive(int(sys.argv[1])))

    
