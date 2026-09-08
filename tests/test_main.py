import pytest
from src.main import get_user_input, print_personalized_message

def test_get_user_input():
    with pytest.raises(SystemExit):
        get_user_input()

def test_print_personalized_message():
    print_personalized_message("Juan", 30)
    assert True