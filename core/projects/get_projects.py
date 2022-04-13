def get_all_projects(checkmarx):
    return checkmarx.get_all_project_details()


def get_project(checkmarx):
    ...


def choose_project(checkmarx):
    num = 0
    project_list = get_all_projects(checkmarx=checkmarx)
    for project in project_list:
        print("\t[{}] ".format(num), project.get("name"))
        num += 1
    num = int(input("- Choose a project:"))
    return project_list[num].get("id"), project_list[num].get("name")
