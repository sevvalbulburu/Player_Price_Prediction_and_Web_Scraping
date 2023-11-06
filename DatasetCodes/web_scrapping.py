import csv
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib


def add_to_dict_from_response(data, dicti, player_name):
    response_str_list = str(data.content.decode('utf-8').encode('utf-8')).split("\"position\"")
    selected_string = ''
    hata = 1
    for response_str_part in response_str_list:
        subnames = player_name.split()
        c = 0
        for sn in subnames:
            if sn in response_str_part:
                c += 1
        if c >= len(subnames):
            hata += 1
            if hata == 3:
                return -1
            selected_string += response_str_part[response_str_part.find('['):response_str_part.find(']')+1]
    if selected_string == '':
        return -1
    # Parse the string as a JSON object
    data = json.loads(selected_string)
    # Iterate over the items in the data and print the names and values
    for item in data:
        #set_trace()
        key = item['name']
        if '(' in key:
            key = key.split('(')[0]
        key = key.strip()
        value = float(item['value'])
        dicti[key] = value
    return 1


def get_player_id(url, url_api, player_name):
    r = {}
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        height, weight, foot = [i.get_text(strip=True) for i in soup.findAll("div", {"class": "p0c-person-information__value"})]
        r["height"] = float(height.replace('cm', ''))/100
        r['weight'] = float(weight.replace('kg', ''))
        r['body_mass_index'] = round(float(r['weight']/(r["height"]**2)), 3)
        r['foot'] = foot

        r['age'] = 2023 - int(soup.findAll("span", {"class": "p0c-person-information__date-of-birth"})[2].get_text(strip=True))
        r['position'] = soup.find("span", {"class": "p0c-person-information__label"}).get_text(strip=True)
        r['team_name'] = soup.find('a', {'class': 'p0c-person-information__club-name'}).text
        r['nationality'] = soup.find('span', {'class': 'p0c-person-information__nationality'}).text
    except Exception as e:
        return -1
    session = requests.Session()
    session.headers.update({
       "Referer": url,
    })

    data = session.get(url=url_api)
    if -1 == add_to_dict_from_response(data, r, player_name):
        return -1

    return r


def get_player_statics(url_apis):
    result = {}
    count = 0
    df = pd.read_csv('player_statistics_latest.csv', encoding='utf-8')
    readed_names = df['full_name'].tolist()
    for name, urls in url_apis.items():
        if name not in readed_names:
            info = get_player_id(urls['url'], urls['url_api'], name)
            if info != -1:
                result[name] = info
                count += 1
                print(count, name)
        else:
            count += 1
            print(count)
    return result



def read_player_url_apis():
    headers = ['Name', 'Url', 'UrlApi']
    result = {}

    # Open the CSV file for reading
    with open('players_url_api.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=headers)
        # Skip the header row
        next(reader)
        
        # Iterate over the remaining rows
        for row in reader:
            name = row['Name']
            url = row['Url']
            url_api = row['UrlApi']
            
            # Store the data in a dictionary
            result[name] = {
                'url': url,
                'url_api': url_api
            }

    return result

url_apis = read_player_url_apis()
r = get_player_statics(url_apis)

column_names = []
for name, values in r.items():
    for key, value in values.items():
        if key not in column_names:
            column_names.append(key)

df = pd.read_csv('player_price_data.csv', encoding='utf-8')
with open('player_statistics.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['label', 'full_name', 'dateA', 'priceA', 'dateB', 'priceB']+column_names)
    dicti = {'label':'label',
            'full_name':'full_name',
            'dateA':'dateA',
            'priceA':'priceA',
            'dateB':'dateB',
            'priceB':'priceB'
            }
    for h in column_names:
        dicti[h] = h
    writer.writerow(dicti)

    for name, values in r.items():
        row = df[df['full_name'] == name]
        if len(row.index) == 0:
            label = 'Unknown'
            dicti = {
                'label':label,
                'full_name': name,
                'dateA': 0,
                'priceA':0,
                'dateB': 0,
                'priceB':0
            }
            for h in column_names:
                if h in values:
                    dicti[h]=values[h]
                else:
                    dicti[h] = None
            writer.writerow(dicti)
        else:
            label = ''
            if row.at[row.index[0], 'priceB']>row.at[row.index[0], 'priceA']:
                label += 'Increased'
            else:
                label += 'Decreased'

            dicti = {
                'label':label,
                'full_name': name,
                'dateA': row.at[row.index[0], 'dateA'],
                'priceA':row.at[row.index[0], 'priceA'],
                'dateB': row.at[row.index[0], 'dateB'],
                'priceB':row.at[row.index[0], 'priceB']
            }
            for h in column_names:
                if h in values:
                    dicti[h]=values[h]
                else:
                    dicti[h] = None
            writer.writerow(dicti)

print("Finished Successfully.")
