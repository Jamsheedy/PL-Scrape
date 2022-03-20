import requests
from bs4 import BeautifulSoup


link = 'https://www.skysports.com/premier-league-table'

teams = {
    'Rick': ['Manchester United', 'Leicester City', 'Wolverhampton Wanderers', 'Brighton and Hove Albion', 'Watford'],
    'Dan': ['Tottenham Hotspur', 'Chelsea', 'West Ham United', 'Crystal Palace', 'Norwich City'],
    'Drew': ['Liverpool', 'Arsenal', 'Aston Villa', 'Southampton', 'Brentford'],
    'Andrew': ['Manchester City', 'Everton', 'Leeds United', 'Newcastle United', 'Burnley']
}

def scrape():
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')

    table = [team for team in soup.find('tbody').find_all('tr')]

    data = {}
    for k in teams.keys():
        data[k] = []


    for row in table:
        teamName = row.find('td', class_='standing-table__cell standing-table__cell--name').a.text

        for k, v in teams.items():
            if teamName in v:
                teamData = {}
                teamData['Name'] = teamName

                metrics = [x.text for x in row.find_all('td', class_='standing-table__cell')]

                teamData['Pos'] = metrics[0]
                teamData['Pl'] = metrics[2]
                teamData['W'] = metrics[3]
                teamData['D'] = metrics[4]
                teamData['L'] = metrics[5]
                teamData['Pts'] = metrics[-2]
                teamData['GD'] = metrics[-3]

                data[k].append(teamData)

    for k, v in data.items():
        print(k)
        for val in v:
            print(val)

    return data


if __name__ == '__main__':
    scrape()
