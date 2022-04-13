from core.projects import get_all_projects


def delete_project(checkmarx, project):
    print("* Remove project:"
          f"\n\tName: {project['name']}"
          f"\n\tId: {project['id']}"
          )
    checkmarx.delete_project_by_id(target_id=project['id'])


def delete_all_projects(checkmarx):
    print('* Cleaning previous projects')
    for project in get_all_projects(checkmarx=checkmarx):
        if 'whitebox_' in project['name']:
            delete_project(checkmarx=checkmarx, project=project)
    print('* Cleaning finished successfully')
