def get_report_data(checkmarx, report_id) -> dict:
    return checkmarx.get_report_status_by_id(report_id).json()
