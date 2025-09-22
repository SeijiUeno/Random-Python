import sys
from typing import List


def square_even_numbers(numbers: List[int]) -> List[int]:
    """Return the pairs numvers squared in the list"""
    return [x**2 if x % 2 == 0 else x for x in numbers]


#   return list(map(lambda x: x**2 if x % 2 == 0 else x, numbers))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[ERROR] - Usage: transform <[numeric list]>")
        sys.exit(1)
    string = sys.argv[1].strip()
    if not string:
        print([])
        sys.exit(0)
    numbers = [int(args) for args in string.split()]
    print(square_even_numbers(numbers))
    print(numbers)
