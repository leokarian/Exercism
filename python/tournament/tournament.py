def draw_table(team_names: list, data: dict) -> list:
    table = ['Team                           | MP |  W |  D |  L |  P']
    for team in team_names:
        line = [(data[team][0]).ljust(31),
                str(data[team][1]).rjust(3).ljust(4), str(data[team][2]).rjust(3).ljust(4),
                str(data[team][3]).rjust(3).ljust(4), str(data[team][4]).rjust(3).ljust(4),
                str(data[team][5]).rjust(3)]
        table.append("|".join(line))
    return table


def tally(rows: list) -> list:
    table = {}

    def save_res(team_name, result, visitor=False):
        table[team_name][1] += 1
        win = "win"
        if visitor:
            win = "loss"
        if result == win:
            table[team_name][2] += 1
            table[team_name][5] += 3
        elif result == "draw":
            table[team_name][3] += 1
            table[team_name][5] += 1
        else:
            table[team_name][4] += 1

    for match in rows:
        res = match.split(";")
        team = res[0]
        if not table.get(team):
            table[team] = [team, 0, 0, 0, 0, 0]
        save_res(team, res[2])
        team = res[1]
        if not table.get(team):
            table[team] = [team, 0, 0, 0, 0, 0]
        save_res(team, res[2], True)

    team_names = sorted(table, key=lambda t: (-table[t][5], table[t][0]))
    return draw_table(team_names, table)
