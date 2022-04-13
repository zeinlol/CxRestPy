import time
from datetime import datetime

from etc.constants import SCAN_CHECK_SLEEP_TIME


def wait_for_finishing_scan(checkmarx, scan_id):
    while True:
        scan_status = get_scan_details(checkmarx=checkmarx, scan_id=scan_id).get("status").get("name")
        print(f"\t[{datetime.now()}] Scan status：[", scan_status, "]", end=" ")
        if scan_status == "Finished":
            print()
            break
        print(f"Re-Check after {SCAN_CHECK_SLEEP_TIME}s ...")
        time.sleep(SCAN_CHECK_SLEEP_TIME)


def get_scan_details(checkmarx, scan_id) -> dict:
    return checkmarx.get_sast_scan_details_by_scan_id(target_id=scan_id).json()
