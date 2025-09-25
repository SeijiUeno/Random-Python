from namebook import format_names


persons = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}


def test_namebook():
    given = persons
    expected = ["Jean Valjean", "Grace Hopper", "Xavier Niel", "Fifi Brindacier"]
    result = format_names(given)
    assert expected == result


def test_empty_dict():
    given = {}
    expected = []
    result = format_names(given)
    assert expected == result


def test_one_person():
    given = {"ana": "silva"}
    expected = ["Ana Silva"]
    result = format_names(given)
    assert expected == result


def test_mixed_case():
    given = {"jOhn": "doE"}
    expected = ["John Doe"]
    result = format_names(given)
    assert expected == result
