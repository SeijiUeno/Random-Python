from password_validator import is_valid_password


def test_minimum_lenght():
    # min == 8
    assert is_valid_password("Ab1!pass")  # len == Min
    assert is_valid_password("WayB1!gerThanIT")  # len > Min
    assert not is_valid_password("Sm4!ler")  # len < Min


def test_max_lenght():
    # max = 16
    assert is_valid_password("Ab!gpasstr3erole")  # len == Min
    assert not is_valid_password("WayB!1gerThanITandwrong")  # len > Max
    assert is_valid_password("Sma!l3rrr")  # len < MAX & == MIN


def test_requires_digit():
    assert not is_valid_password("Abcdefg!")  # missing digit
    assert is_valid_password("Abcdefg1!")  # has digit


def test_requires_uppercase():
    assert not is_valid_password("abcdefg1!")  # missing uppercase
    assert is_valid_password("Abcdefg1!")  # has uppercase


def test_requires_lowercase():
    assert not is_valid_password("ABCDEFG1!")  # missing lowercase
    assert is_valid_password("Abcdefg1!")  # has lowercase


def test_requires_special():
    # '-', '_', '!', '@', '#', '$', '&'
    assert not is_valid_password("Abcdefg12")  # missing special
    assert is_valid_password("Abcdefg1!")  # has special


def test_with_white_space():
    assert not is_valid_password("Abc ef1!")  # false
    assert is_valid_password("A1b23d4!")  # ok


def test_valid_password():
    assert is_valid_password("Abcdef1!")  # ok
    assert is_valid_password("A1b2c3d4!")  # ok


def test_invalid_special_char():
    assert not is_valid_password("Abcdefg1*")  # '*' fora
