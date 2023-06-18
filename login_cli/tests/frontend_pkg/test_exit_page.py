from unittest.mock import patch
import pytest
from login_cli.frontend.frontend import Frontend

@patch("login_cli.frontend.frontend.Frontend._logout_page")
def test_exit_app_page_when_logged_in(mock_logout_page, monkeypatch, capsys):
    
    Frontend.is_logged_in = True
    Frontend.exit_app_page() 

    mock_logout_page.assert_called_once()
    assert Frontend.should_exit == True 

def test_exit_app_page_when_not_logged_in(monkeypatch, capsys):
    
    Frontend.is_logged_in = False
    
    Frontend.exit_app_page()
    
    captured = capsys.readouterr()
    output = captured.out.strip() 

    assert output == "!! CLOSING APP !!"
    assert Frontend.should_exit == True 

def test_logout_page(capsys):
    Frontend._logout_page()

    # Assert the output
    captured = capsys.readouterr()
    assert captured.out.strip() == "!! LOGOUT SUCCESSFULLY !!"
    assert Frontend.is_logged_in == False
