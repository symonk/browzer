from sylenium import session_manager


def go(url: str) -> None:
    driver = session_manager.fetch().get_driver()
    driver.get(url)
