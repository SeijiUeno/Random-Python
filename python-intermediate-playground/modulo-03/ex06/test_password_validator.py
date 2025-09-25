import pytest
from password_validator import is_valid_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Sh0rt!P", False, id="Password is too short"),
        pytest.param("L0ngValid!Password", False, id="Password is too long"),
        pytest.param("Valid@ Pass1", False, id="Contains white space"),
        pytest.param("", False, id="Empty string"),
        pytest.param("valid@pass1", False, id="Missing uppercase"),
        pytest.param("VALID@PASS1", False, id="Missing lowercase"),
        pytest.param("Valid@Password", False, id="Missing digit"),
        pytest.param("ValidPass1", False, id="Missing special char"),
        pytest.param("Valid@Pass1", True, id="Valid Password"),
        pytest.param("Sh0rt!P@ss", True, id="Valid Password"),
        pytest.param("L0ngValid!Passwd", True, id="Valid Password"),
    ],
)
def test_password_validation(password: str, expected_result: bool) -> None:
    """Tests the is_valid_password function with various inputs."""
    assert is_valid_password(password) == expected_result
