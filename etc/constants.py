import pathlib

REPORT_TYPES = ["PDF", "RTF", "CSV", "XML"]

BASE_DIR = pathlib.Path().absolute()

SCAN_CHECK_SLEEP_TIME = 5  # in seconds
REPORT_CHECK_SLEEP_TIME = 2  # in seconds
