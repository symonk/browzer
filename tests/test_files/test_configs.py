from sylenium.configuration.configuration import Configuration


class HeadlessConfig(Configuration):
    def __init__(self):
        super().__init__(
            headless=True,
            chrome_options=["--headless", "no-sandbox", "--disable-extensions"],
        )
