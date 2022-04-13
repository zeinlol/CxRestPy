def get_all_teams(checkmarx) -> list[dict]:
    return checkmarx.get_all_teams().json()


def get_team(checkmarx, team_id=None, name=None) -> dict:
    if not name and not team_id:
        return choose_team(checkmarx=checkmarx)
    teams = get_all_teams(checkmarx=checkmarx)
    for team in teams:
        if team['fullName'] == name or team['id'] == team_id:
            return team
    print(f'X No team with name {name}')
    exit(1)


def choose_team(checkmarx):
    teams = get_all_teams(checkmarx=checkmarx)
    num = 0
    for team in teams:
        print("\t[{}] ".format(num), team.get("fullName"))
        num += 1
    num = int(input("- Choose a team to create project:"))
    return teams[num]
