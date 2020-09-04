from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from pyfields import field
from pyfields import init_fields
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from valid8.validation_lib import is_in
from valid8.validation_lib import subclass_of

from sylenium.constants import SUPPORTED_BROWSERS
from sylenium.mixins import SimpleEQMixin
from sylenium.mixins import SimpleReprMixin


class Configuration(SimpleReprMixin, SimpleEQMixin):
    """
    This is the core configuration class for sylenium.
    This is the core instance that is required to create a new session, fully customisable by the client.
    """

    browser: str = field(
        check_type=True,
        default="chrome",
        doc="Browser type to instantiate within sessions",
        converters=str.lower,
        validators=is_in(SUPPORTED_BROWSERS),
    )

    headless: bool = field(
        check_type=True,
        default=True,
        doc="Browser instantiated will be headless or not",
    )

    remote: bool = field(
        check_type=True,
        default=False,
        doc="Browser is a remote web driver for a selenium grid",
    )

    page_loading_strategy: str = field(
        check_type=True,
        default="fast",
        doc="Strategy applied by sylenium when waiting for page loading",
        converters=lambda x: x.lower(),
        validators=is_in({"fast"}),
    )

    selenium_grid_url: str = field(
        check_type=True,
        default="http://localhost",
        doc="Selenium grid address (without port)",
        converters=lambda x: x.lower(),
        validators=lambda x: x.startswith("http"),
    )

    selenium_grid_port: int = field(
        check_type=True, default=4444, doc="Selenium grid port"
    )

    browser_resolution: Optional[str] = field(
        check_type=True,
        default=None,
        doc="Set the browser resolution when instantiating a driver",
        nonable=True,
        validators=lambda x: "x" in x,
    )

    browser_position: Optional[str] = field(
        check_type=True,
        default=None,
        doc="Set the browser position when instantiating a driver",
        nonable=True,
        validators=lambda x: "x" in x,
    )

    browser_version: str = field(
        check_type=True, default="latest", doc="Version of the driver to use"
    )

    downloads_directory: Optional[str] = field(
        check_type=True,
        default=None,
        doc="Sets the download directory that browser downloads are saved in",
        nonable=True,
    )

    proxy_enabled: bool = field(
        check_type=True,
        default=False,
        doc="Use the sylenium proxy at runtime (useful for request/response inspection",
    )

    driver_binary_path: str = field(
        check_type=True,
        default="acquire",
        doc="Should sylenium download the driver binaries automatically without $path",
        converters=lambda x: x.lower(),
    )

    browser_capabilities: Optional[Dict[str, str]] = field(
        check_type=False,
        default_factory=lambda x: {},
        doc="Desired capabilities to merge with appropriate options",
        nonable=True,
    )

    chrome_options: Optional[List[str]] = field(
        check_type=False,
        default_factory=lambda x: [],
        doc="Chrome options to control chrome browser instantiation",
    )

    base_url: Optional[str] = field(
        check_type=True,
        default=None,
        doc="base url to automatically launch when browsers are instantiated",
        validators=lambda x: x != "",
    )

    explicit_waiting: float = field(
        check_type=True,
        default=30.00,
        doc="Default time to wait for element checks before raising exceptions",
        validators=lambda x: x > 0,
    )

    polling_interval: float = field(
        check_type=True,
        default=00.50,
        doc="How often should element checks be performed to continue",
        validators=lambda x: x > 0,
    )

    page_source_capturing: bool = field(
        check_type=True,
        default=False,
        doc="Automatically store page source .html during the driver lifetime",
    )

    page_screenshot_capturing: bool = field(
        check_type=True,
        default=False,
        doc="Automatically store page screenshots during the driver lifetime",
    )

    stack_trace_capturing: bool = field(
        check_type=True,
        default=False,
        doc="Automatically store stack trace information when things go wrong",
    )

    javascript_clicks: bool = field(
        check_type=True,
        default=False,
        doc="Execute javascript to perform clicking actions",
    )

    javascript_sendkeys: bool = field(
        check_type=True,
        default=False,
        doc="Execute javascript to perform sending key actions",
    )

    driver_event_firing_wrapper: Optional[Type[AbstractEventListener]] = field(
        check_type=False,
        default=None,
        doc="Event firing driver wrapper class",
        validators=subclass_of(AbstractEventListener),
    )

    default_selector: str = field(
        check_type=True,
        default="css",
        doc="Default selector for finding elements when not specified explicitly",
        validators=is_in({"css"}),
        converters=lambda x: x.lower(),
    )

    chrome_service_log_path: Optional[str] = field(
        check_type=True,
        default=None,
        doc="Custom path to write for chrome log / debug output",
    )

    maximized: bool = field(
        check_type=True,
        default=True,
        doc="Should the browser be maximized when instantiated",
    )

    @init_fields
    def __init__(self):
        ...

    def full_hub_endpoint(self) -> str:
        """
        The getter for the full hub endpoint that nodes are registered to and tests should be launched to.
        """
        return f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"
