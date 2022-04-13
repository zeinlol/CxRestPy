from core import cli_arguments
from core.teams import choose_team, get_team
from core.utils.randomiser import generate_random_string


def create_project(checkmarx, project_name, team=None) -> dict:
    team = team or choose_team(checkmarx=checkmarx)
    print(f"* generate new project:\n\tname: {project_name}\n\tteam: {team['fullName']}")
    team_id = team.get("id")
    return checkmarx.create_project_with_default_configuration(name=project_name, owning_team=team_id).json()


def generate_new_temp_project(checkmarx) -> dict:
    team = get_team(checkmarx=checkmarx, name=cli_arguments.team)
    print(f"* using team {team['fullName']}")
    name: str = cli_arguments.project or generate_random_string()
    return create_project(checkmarx=checkmarx, project_name=name, team=team)
