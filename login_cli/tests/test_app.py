import pytest
from unittest.mock import patch, MagicMock
import subprocess

from login_cli.app import App

@pytest.fixture
def app():
    subprocess.run(["python3", "setup.py"], text=True, input="y\ny\n")
    return App()

class Test_Db_error:

    @patch("login_cli.app.path.exists")
    @patch("login_cli.app.Frontend.DB_error_page")
    def test_db_error1(self, mock_error_page, mock_exists, app):
        # Mock path.exists to simulate both files not existing
        mock_exists.side_effect = [False, False]
        app.run()
        mock_error_page.assert_called_once()

    @patch("login_cli.app.path.exists")
    @patch("login_cli.app.Frontend.DB_error_page")
    def test_db_error2(self, mock_error_page, mock_exists, app):
        # Mock path.exists to simulate DB1_PATH existing and DB2_PATH not existing
        mock_exists.side_effect = [True, False]
        app.run()
        mock_error_page.assert_called_once()

    @patch("login_cli.app.path.exists")
    @patch("login_cli.app.Frontend.DB_error_page")
    def test_db_error3(self, mock_error_page, mock_exists, app):
        # Mock path.exists to simulate DB1_PATH not existing and DB2_PATH existing
        mock_exists.side_effect = [False, True]
        app.run()
        mock_error_page.assert_called_once()



class Test_Integration_Test:

    def test_exit(self, app, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "3")
        app.run()

    def test_register_login_exit(self, app, monkeypatch):
        inputs = iter(["2", "username", "password", "1", "username", "password", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        app.run()
    
    def test_register_login_login_login_exit(self, app, monkeypatch):
        inputs = iter(["2", 
                       "username", "password", 
                       "1", 
                       "username", "wrong_password",
                       "username", "wrong_password", 
                       "username", "password", 
                       "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        app.run()

    def test_login_register_register_login_exit(self, app, monkeypatch):
        inputs = iter(["1", 
                       "foo", "bar", 
                       "2", 
                       "foo", "bar", 
                       "2", 
                       "foo", "bar", 
                       "1", 
                       "foo", "bar", 
                       "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        app.run()

 