import requests
from bs4 import BeautifulSoup
import pandas as pnd

def scrape_last_5_form(team_name):
    url = "https://www.fbref.com/en/comps/12"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    
    table = soup.find('table', {'id': 'results2025-2026121_overall'})

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    forms = []

    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        if( team_name.lower() == team_name.lower()):
            last_matches_results = cells[14].text.strip().split(' ')
            team_info = {
                'team': cells[0].text.strip(),
                'last match result': last_matches_results[0],
                'last 2nd match result': last_matches_results[1],
                'last 3rd match result': last_matches_results[2],
                'last 4th match result': last_matches_results[3],
                'last 5th match result': last_matches_results[4],
            }
            forms.append(team_info)
            df = pnd.DataFrame(forms)
            df.to_csv(f'data/raw/last_5_form_{team_name.replace(" ", "_")}.csv', index=False)
            print(f"Last 5 form data for {team_name} saved to last_5_form_{team_name.replace(' ', '_')}.csv")
            return 
        # team_info = {
        #     'team': cells[0].text.strip(),

        # }
scrape_last_5_form('Real Madrid')