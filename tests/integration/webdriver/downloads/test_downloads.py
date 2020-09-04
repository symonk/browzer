import os
import time

from assertpy import assert_that

from sylenium import Configuration


def test_download_file(sy_session, tmpdir):
    with sy_session(Configuration(downloads_directory=str(tmpdir))) as session:
        session.get_driver().get("http://ipv4.download.thinkbroadband.com/1MB.zip")
        # TODO => Add a wait_until method or library and wait until .crdownload is no more.
        time.sleep(5)
        assert_that(os.listdir(tmpdir)).contains("1MB.zip")
