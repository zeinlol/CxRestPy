def create_scan(checkmarx, project_id) -> dict:
    return checkmarx.create_new_scan(project_id).json()
