import requests
from bs4 import BeautifulSoup
import pandas as pnd

def scrape_season_teams(season):
    url = f"https://fbref.com/en/comps/12/{season}/{season}-Premier-League-Stats"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')

    table = soup.find('table', {'id': f'results{season}121_overall'})

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    teams = []
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        team_info = {
            'team':  cells[0].text.strip(),
            'season': season
        }
        teams.append(team_info)
    df = pnd.DataFrame(teams)
    df.to_csv(f'data/raw/laliga_{season}_teams.csv', index=False)
    print(f"Data for La Liga {season} season saved to laliga_{season}_teams.csv")

scrape_season_teams('2025-2026')
