from typing import List
import shutil

from core.utils.downloader import download_parallel
from core.config import config


def archive_urls(urls: List[str], filename: str):
    dirname = config.STATIC_DIR + filename
    download_parallel(urls, dirname, 0, -1, False)
    output_filename = dirname
    shutil.make_archive(output_filename, 'zip', dirname)
