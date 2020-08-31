from socketserver import TCPServer
from typing import Tuple


class IntegrationTCPServer(TCPServer):
    def __init__(
        self, server_address: Tuple[str, int], handler, bind_and_activate: bool = True
    ):
        super().__init__(server_address, handler, bind_and_activate)

    @property
    def server_url(self) -> str:
        addr, port = self.server_address
        return f"http://{addr}:{port}/"

    def page_url(self, page_name: str) -> str:
        return f"{self.server_url}{page_name}.html"
