from core import cli_arguments
from core.api import RestAPI
from core.projects import choose_project, create_project, generate_new_temp_project
from core.reports import generate_new_report_file
from core.scans import create_scan, wait_for_finishing_scan
from core.utils.output_format import get_format

checkmarx = RestAPI.CxRestAPI()


def main():
    print("* Welcome to Checkmarx Rest api! *")

    if cli_arguments.auto:  # check if existed or create new project
        project = generate_new_temp_project(checkmarx=checkmarx)
    elif input("- Do you want to create new project?(Y/N)").upper() == "Y":
        project = create_project(checkmarx=checkmarx,
                                 project_name=cli_arguments.project or input("- Set your project name:"))
    else:
        project = choose_project(checkmarx)
    project_id = project.get("id")
    project_name = project.get("name")
    target_path = cli_arguments.scan_folder or input("- Set target path:")
    print(f"* Target path: {target_path}")
    if target_path.name[:-3] == 'zip':
        checkmarx.upload_source_code_zip_file(target_id=project_id, zip_path=target_path)
    else:
        checkmarx.upload_source_code_folder(target_id=project_id, target_path=target_path)
    print("* Files uploaded successfully\n* Creating new scan...")
    scan = create_scan(checkmarx=checkmarx, project_id=project_id)
    scan_id = scan.get("id")
    wait_for_finishing_scan(checkmarx=checkmarx, scan_id=scan_id)

    report_type = cli_arguments.format or get_format()
    print("* Creating report...")
    report_name = f'{project_name}.{report_type}'
    generate_new_report_file(checkmarx=checkmarx, report_type=report_type, scan_id=scan_id, file_name=report_name)
    print("* Successful! Thanks for usage. *")


if __name__ == '__main__':
    main()
