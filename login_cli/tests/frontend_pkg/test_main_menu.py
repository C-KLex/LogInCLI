from unittest.mock import patch, MagicMock
import pytest
from login_cli.frontend.frontend import Frontend

@pytest.fixture
def frontend():
    return Frontend()

def test_main_menu_page_with_valid_choice(frontend, monkeypatch, capsys):
    # Mock the input value
    monkeypatch.setattr('builtins.input', MagicMock(return_value='1'))

    choice = frontend.main_menu_page()

    assert choice == 1

def test_main_menu_page_with_invalid_choice(frontend, monkeypatch, capsys):
    # Mock the input value
    monkeypatch.setattr('builtins.input', MagicMock(return_value='4'))

    choice = frontend.main_menu_page()

    assert choice == 4

def test_main_menu_page_with_nonnumeric_choice(frontend, monkeypatch, capsys):
    # Mock the input value
    monkeypatch.setattr('builtins.input', MagicMock(return_value='abc'))

    with pytest.raises(ValueError):
        frontend.main_menu_page()

def test_main_menu_page_logged_with_valid_choice(frontend, monkeypatch, capsys):
    # Mock the input value
    monkeypatch.setattr('builtins.input', MagicMock(return_value='1'))

    choice = frontend.main_menu_after_logged_page()

    assert choice == 1

def test_main_menu_page_logged_with_invalid_choice(frontend, monkeypatch, capsys):
    # Mock the input value
    monkeypatch.setattr('builtins.input', MagicMock(return_value='4'))

    choice = frontend.main_menu_after_logged_page()

    assert choice == 4

def test_main_menu_page_logged_with_nonnumeric_choice(frontend, monkeypatch, capsys):
    # Mock the input value
    monkeypatch.setattr('builtins.input', MagicMock(return_value='abc'))

    with pytest.raises(ValueError):
        frontend.main_menu_after_logged_page()

