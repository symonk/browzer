from browzer.configuration.browzer_configuration import BrowzerConfiguration


class HeadlessConfig(BrowzerConfiguration):
    def __init__(self):
        super().__init__(
            headless=True,
            chrome_options=["--headless", "no-sandbox", "--disable-extensions"],
        )
