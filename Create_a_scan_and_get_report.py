import RestAPI
import time
import os

cx = RestAPI.CxRestAPI()


def choose_a_project():
    num = 0
    project_list = cx.get_all_project_details()
    for project in project_list:
        print("\t[{}] ".format(num), project.get("name"))
        num += 1
    num = int(input("- Choose a project:"))
    return project_list[num].get("id"), project_list[num].get("name")


def main():
    global project_name, team_id
    print("* Welcome to use this scripts! *")
    flag = input("- Do you want to create a new project?(Y/N)")
    if flag.upper() == "Y":
        teams = cx.get_all_teams().json()
        num = 0
        for team in teams:
            print("\t[{}] ".format(num), team.get("fullName"))
            num += 1
        num = int(input("- Choose a team to create project:"))
        team_id = teams[num].get("id")
        project_name = input("- Set your project name:")
        project_id = cx.create_project_with_default_configuration(name=project_name, owning_team=team_id).json().get("id")
    else:
        project_id, project_name = choose_a_project()
    zip_path = input("- Set the zip file path:")
    report_types = ["PDF", "RTF", "CSV", "XML"]
    report_code = 0
    for type in report_types:
        print("\t[{}]".format(report_code), type)
        report_code += 1
    report_code = int(input("- Choose a report type:"))
    cx.upload_source_code_zip_file(project_id=project_id, zip_path=zip_path)
    print("* Creating a new scan...")
    scan = cx.create_new_scan(project_id)
    scan_id = scan.json().get("id")
    while True:
        scan_status = cx.get_sast_scan_details_by_scan_id(id=scan_id).json().get("status").get("name")
        print("\tScan status：[", scan_status, "]", end=" ")
        if scan_status == "Finished":
            print()
            break
        print("Re-Check after 10s ...")
        time.sleep(10)
    print("* Creating report...")
    report_type = report_types[report_code].lower()
    report = cx.register_scan_report(report_type=report_type, scan_id=scan_id)
    report_id = report.json().get("reportId")
    while True:
        report_status = cx.get_report_status_by_id(report_id).json().get("status").get("value")
        print("\tReport status：[", report_status, "]", end=" ")
        if report_status == "Created":
            print()
            break
        print("Re-Check after 5s ...")
        time.sleep(5)
    report_name = project_name + "." + report_type
    reports = cx.get_reports_by_id(report_id, report_type).content
    with open(os.path.expanduser(report_name), 'wb') as f:
        f.write(reports)
    print("* Successful! Thanks for use. *")


if __name__ == '__main__':
    main()
