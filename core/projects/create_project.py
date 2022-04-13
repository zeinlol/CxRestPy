from core import cli_arguments
from core.teams import choose_team


def create_project(checkmarx):
    team_id = choose_team(checkmarx=checkmarx)
    project_name = cli_arguments.project or input("- Set your project name:")
    return checkmarx.create_project_with_default_configuration(name=project_name, owning_team=team_id).json()
