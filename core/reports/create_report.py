import os
import time

from core.reports import get_report_data


def create_report(checkmarx, report_type, scan_id):
    return checkmarx.register_scan_report(report_type=report_type, scan_id=scan_id).json()


def generate_new_report_file(checkmarx, report_type, scan_id, file_name: str):
    report = create_report(checkmarx=checkmarx, report_type=report_type, scan_id=scan_id)
    report_id = report.get("reportId")
    while True:
        report_status = get_report_data(checkmarx=checkmarx, report_id=report_id).get("status").get("value")
        print("\tReport status：[", report_status, "]", end=" ")
        if report_status == "Created":
            print()
            break
        print("Re-Check after 5s ...")
        time.sleep(5)
    reports = checkmarx.get_reports_by_id(report_id, report_type).content
    with open(os.path.expanduser(file_name), 'wb') as f:
        f.write(reports)
