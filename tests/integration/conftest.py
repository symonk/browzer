import http.server
import os
import threading
from typing import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from tests.integration.webserver.tcp_server import IntegrationTCPServer


@pytest.fixture
def default_driver(default_session) -> RemoteWebDriver:
    return default_session.get_driver()


@pytest.fixture
def webserver() -> Generator[IntegrationTCPServer, None, None]:
    handler = http.server.SimpleHTTPRequestHandler
    server = IntegrationTCPServer(("localhost", 8080), handler)
    os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "http_content"))
    print("Http server started for integration testing")
    try:
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        yield server
    except Exception:
        pass
