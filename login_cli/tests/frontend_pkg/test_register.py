from unittest.mock import patch, MagicMock
import pytest
from login_cli.frontend.frontend import Frontend

@pytest.fixture
def frontend():
    return Frontend()

@patch('builtins.input', MagicMock(side_effect=['username', 'password']))
@patch("login_cli.frontend.frontend.Backend.account_exist", return_value = True)
def test_register_page_with_existing_acc(mock_account_exist, frontend, monkeypatch, capsys):

    frontend.register_page()

    assert capsys.readouterr().out.strip() == "##### REGISTER MODULE#####\n" + "!! ACCOUNT ALREADY EXISTS !!"
        
@patch("builtins.input", MagicMock(side_effect=["username", "password"]))
@patch("login_cli.frontend.frontend.Backend.account_exist", return_value = False)
@patch("login_cli.frontend.frontend.Backend.add_account", return_value = None)
def test_register_page_without_existing_acc(mock_acc_exist, mock_add_acc, frontend, capsys):
        
    frontend.register_page()

    assert capsys.readouterr().out.strip() == "##### REGISTER MODULE#####\n" +"!! REGISTER SUCCESS !!"
