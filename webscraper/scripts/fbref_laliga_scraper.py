import requests
from bs4 import BeautifulSoup
import pandas as pnd

def scrape_laliga_season(season):
    url = f"https://fbref.com/en/comps/12/{season}/{season}-La-Liga-Stats"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    table = soup.find('table', {'id': f'results{season}121_overall'})


    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    team_stats = []

    for row in rows:
        cells = row.find_all('td')
        rank_cell = row.find('th')
        if not cells or not rank_cell:
            continue
        match = {
            'rank in league': rank_cell.text.strip(),
            'team': cells[0].text.strip(),
            'matches': cells[1].text.strip(),
            'goals for': cells[5].text.strip(),
            'goals against': cells[6].text.strip(),
            'team goal scorer': cells[15].text.strip(),
        }
        team_stats.append(match)
    
    df = pnd.DataFrame(team_stats)
    df.to_csv(f'data/raw/laliga_{season}_teamstats.csv', index=False)
    print(f"Data for La Liga {season} season saved to laliga_{season}_teamstats.csv")

scrape_laliga_season('2023-2024')