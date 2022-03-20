from prem import *
import ezsheets

sheetID = '1MVStXePPkmqxZEM79Qux5vBTfwFLJ30SZWB8vniigQQ'
ss = ezsheets.Spreadsheet(sheetID)

data = ss[0]

headerRow = data.getRow(1)
teamCol = data.getColumn(5)


def get_col_index(val):
    try:
        return headerRow.index(val)
    except ValueError:
        return None


def get_row_index(val):
    try:
        return teamCol.index(val)
    except ValueError:
        return None


def update_sheet():
    standings = scrape()
    update_teams(standings)
    update_stats(standings)


def update_teams(standings):
    index = get_col_index('Team')
    column = data.getColumn(index + 1)

    for k, v in standings.items():
        for team in v:
            if team['Name'] not in column:
                column.append(team['Name'])

    data.updateColumn(index + 1, column)


def update_stats(standings):
    cols = {
        'Player': {},
        'Pos': {},
        'Pl': {},
        'W': {},
        'D': {},
        'L': {},
        'Pts': {},
        'GD': {}
    }

    for k, v in cols.items():
        v['index'] = get_col_index(k) + 1
        v['column'] = data.getColumn(v['index'])


    # teamCol = data.getColumn(5)
    # print(teamCol)
    for row, tname in enumerate(teamCol):
        for k, v in standings.items():
            for team in v:
                if team['Name'] == tname:
                    for k1, v1 in cols.items():
                        if k1 == 'Player':
                            v1['column'][row] = k
                        else:
                            print(team)
                            v1['column'][row] = team[k1]

    for k, v in cols.items():
        print(k, v)
        data.updateColumn(v['index'], v['column'])


if __name__ == '__main__':
    update_sheet()
