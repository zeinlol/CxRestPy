def get_report_data(checkmarx, report_id) -> dict:
    return checkmarx.get_report_status_by_id(report_id).json()


def get_reports_results(checkmarx, report_id, report_type) -> dict:
    return checkmarx.get_reports_by_id(report_id, report_type).content
