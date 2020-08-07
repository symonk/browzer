from sylenium.configuration.sylenium_configuration import syleniumConfiguration


class HeadlessConfig(syleniumConfiguration):
    def __init__(self):
        super().__init__(
            headless=True,
            chrome_options=["--headless", "no-sandbox", "--disable-extensions"],
        )
