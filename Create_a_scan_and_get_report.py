from core.api import RestAPI
from core.projects import choose_project, create_project
from core.reports import generate_new_report_file
from core.scans import create_scan, wait_for_finishing_scan
from etc.constants import REPORT_TYPES

checkmarx = RestAPI.CxRestAPI()


def main():
    print("* Welcome to Checkmarx Rest api! *")

    flag = input("- Do you want to create new project?(Y/N)")
    if flag.upper() == "Y":
        project = create_project(checkmarx=checkmarx)
        project_id = project.get("id")
        project_name = project.get("name")
    else:
        project_id, project_name = choose_project(checkmarx)

    target_path = input("- Set target path:")
    if target_path[:-3] == 'zip':
        checkmarx.upload_source_code_zip_file(target_id=project_id, zip_path=target_path)
    else:
        checkmarx.upload_source_code_folder(target_id=project_id, target_path=target_path)
    print("* Creating new scan...")
    scan = create_scan(checkmarx=checkmarx, project_id=project_id)
    scan_id = scan.get("id")
    wait_for_finishing_scan(checkmarx=checkmarx, scan_id=scan_id)

    report_code = 0
    for types in REPORT_TYPES:
        print("\t[{}]".format(report_code), types)
        report_code += 1
    report_code = int(input("- Choose report type:"))
    report_type = REPORT_TYPES[report_code].lower()
    print("* Creating report...")
    report_name = f'{project_name}.{report_type}'
    generate_new_report_file(checkmarx=checkmarx, report_type=report_type, scan_id=scan_id, file_name=report_name)
    print("* Successful! Thanks for use. *")


if __name__ == '__main__':
    main()
