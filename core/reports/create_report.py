import os
import time
from pathlib import Path

from core import cli_arguments
from core.reports.get_reports import get_report_data, get_reports_results
from etc.constants import REPORT_CHECK_SLEEP_TIME, BASE_DIR


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
        print(f"Re-Check after {REPORT_CHECK_SLEEP_TIME}s ...")
        time.sleep(REPORT_CHECK_SLEEP_TIME)
    reports = get_reports_results(checkmarx, report_id, report_type)
    report_path = Path(cli_arguments.output) or Path(BASE_DIR).joinpath(f'Report.{report_type}')
    if report_path.is_dir():
        file_name = f'Report.{report_type}'
    else:
        file_name = report_path.name
        report_path = report_path.parent
    write_to_file(path=report_path, file_name=file_name, data=reports)


def write_to_file(path, file_name, data):
    full_path = f"{path}/{file_name}"
    print(f"* Writing data to file: {full_path}")
    with open(os.path.expanduser(full_path), 'wb') as f:
        f.write(data)
