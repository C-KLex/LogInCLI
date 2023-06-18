from unittest.mock import patch
import pytest
from login_cli.frontend.frontend import Frontend

@pytest.fixture
def frontend():
    return Frontend()

def test_exit_app_page_when_logged_in(frontend, monkeypatch, capsys):
    # Set is_logged_in to True
    frontend.is_logged_in = True

    # Mock the _logout_page method
    with patch('login_cli.frontend.frontend.Frontend._logout_page') as mock_logout_page:
        frontend.exit_app_page()

        # Assert that _logout_page was called
        mock_logout_page.assert_called_once()

# def test_exit_app_page_when_not_logged_in(frontend, monkeypatch, capsys):
#     # Set is_logged_in to False
#     frontend.is_logged_in = False

#     frontend.exit_app_page()

#     # Assert the output
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "!! CLOSING APP !!"

# def test_logout_page(frontend, capsys):
#     frontend._logout_page()

#     # Assert the output
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "!! LOGOUT SUCCESSFULLY !!"
#     assert frontend.is_logged_in == False
