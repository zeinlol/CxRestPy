import time


def wait_for_finishing_scan(checkmarx, scan_id):
    while True:
        scan_status = get_scan_details(checkmarx=checkmarx, scan_id=scan_id).get("status").get("name")
        print("\tScan status：[", scan_status, "]", end=" ")
        if scan_status == "Finished":
            print()
            break
        print("Re-Check after 10s ...")
        time.sleep(10)


def get_scan_details(checkmarx, scan_id) -> dict:
    return checkmarx.get_sast_scan_details_by_scan_id(target_id=scan_id).json()
