def get_all_teams(checkmarx):
    return checkmarx.get_all_teams().json()


def get_team(checkmarx):
    pass


def choose_team(checkmarx):
    teams = get_all_teams(checkmarx=checkmarx)
    num = 0
    for team in teams:
        print("\t[{}] ".format(num), team.get("fullName"))
        num += 1
    num = int(input("- Choose a team to create project:"))
    return teams[num].get("id")
