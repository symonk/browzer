import http.server
import os
import socketserver
import threading
from typing import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


@pytest.fixture
def default_driver(default_session) -> RemoteWebDriver:
    return default_session.get_driver()


@pytest.fixture
def webserver() -> Generator[socketserver.BaseServer, None, None]:
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("localhost", 8080), handler) as server:
        os.chdir(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "http_content")
        )
        print("Http server started for integration testing")
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        yield server
