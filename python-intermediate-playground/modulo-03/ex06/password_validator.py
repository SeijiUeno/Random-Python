def is_valid_password(password: str) -> bool:
    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False

    MIN_SIZE = 8
    MAX_SIZE = 16
    valid_chars = {"-", "_", "!", "@", "#", "$", "&"}

    if not (MIN_SIZE <= len(password) <= MAX_SIZE):
        return False

    for char in password:
        if char.isspace():
            return False
        elif char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in valid_chars:
            has_special = True

    return has_digit and has_upper and has_lower and has_special
