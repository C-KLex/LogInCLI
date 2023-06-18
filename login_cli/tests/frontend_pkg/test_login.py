from unittest.mock import patch, MagicMock
import pytest
from login_cli.frontend.frontend import Frontend


@patch('login_cli.frontend.frontend.Backend.account_exist', return_value=True)
@patch('login_cli.frontend.frontend.Backend.login_validation', return_value=True)
@patch("login_cli.frontend.frontend.Frontend.login_success_page")
def test_login_page_with_valid_credentials(mock_account_exist, mock_login_validation, mock_login_success_page, monkeypatch):
    # Mock the input values
    monkeypatch.setattr("builtins.input", MagicMock(side_effect = ["john_doe", "password123"]))
        
    Frontend.login_page()

    mock_account_exist.assert_called_once_with("john_doe")
    mock_login_validation.assert_called_once_with("john_doe", "password123")
    mock_login_success_page.assert_called_once_with("john_doe")
    assert Frontend.is_logged_in == True

    # Manual Log Out
    Frontend.is_logged_in = False 



def test_login_invalid_credentials():

    pass
    
    
@patch("login_cli.frontend.frontend.Backend.account_exist", return_value = False)
def test_login_acc_not_exist(mock_acc_exist, monkeypatch):
    monkeypatch.setattr("builtins.input", MagicMock(side_effect=["john_doe", "password123"]))
    
    Frontend.login_page()
    
    mock_acc_exist.assert_called_once_with("john_doe")
    assert Frontend.is_logged_in == False 


