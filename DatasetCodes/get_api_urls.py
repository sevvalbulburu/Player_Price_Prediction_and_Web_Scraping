import time
from bs4 import BeautifulSoup
import requests
import csv
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import urllib.parse
from get_player_urls import liste_U22_23, liste_U21_22, liste_U20_21, liste_U19_20, liste_U18_19

temp = list(set(liste_U22_23 + liste_U21_22 + liste_U20_21 + liste_U19_20 + liste_U18_19))
#print("Player Page Url Count:", len(temp))

df = pd.read_csv('players_url_api_all_save.csv', encoding='utf-8')
readed_urls = [urllib.parse.unquote(x.replace("sezon/", "")) for x in df['url'].tolist()]
player_page_urls = [x for x in temp if x not in readed_urls]
print("Player Page Url Count:", len(player_page_urls))
print()
# Start the browsermob-proxy server
server = Server("C:\\Users\\alper\\Desktop\\playerPrediction\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()

# Configure the Chrome driver with the proxy
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
driver = webdriver.Chrome("C:\\Users\\alper\\Desktop\\playerPrediction\\chromeDriver\\chromedriver.exe", options=chrome_options)

#url = "https://www.mackolik.com/perform/p0/ajax/components/competition/player/ranking/list?ajaxViewName=list&page" \
#        "={}&hasNextPage=true&playerFilter=topscorers&seasonId=dffn22be69d945d62hmqc2qdw&teamId="
result = {}

for url in player_page_urls:
    try:
        parts = url.split("/")
        modified_url = "/".join(parts[:5]) + "/sezon/" + parts[-1]
        modified_url = "/".join(parts[:5]) + "/sezon/" + parts[-1]

        response = requests.get(url=modified_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find("span", {"class": "p0c-person-information__full-name"}).get_text(strip=True)
        # Enable network capturing
        proxy.new_har()

        # Load the page
        driver.get(modified_url)

        # Wait for the page to load (you can adjust the sleep duration as needed)
        time.sleep(3)

        # Get the captured network traffic
        har = proxy.har

        url_api = ''
        latest_time = 0
        # Iterate through the network requests and print headers and URLs
        for entry in har['log']['entries']:
            request = entry['request']
            headers = request['headers']
            url = request['url']
            if 'performfeeds' in url and latest_time < entry['time']:
                latest_time = entry['time']
                url_api = url

        if url_api != '':
            result[name]={"url":modified_url, "url_api":url_api}
    except Exception as e:
        print("Exception", e)


headers = ['Name', 'Url', 'UrlApi']
with open('players_url_api_all.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    for key, value in result.items():
        dicti = {
            'Name': key,
            'Url': value["url"],
            'UrlApi': value["url_api"]
        }
        writer.writerow(dicti)

# Stop the browsermob-proxy server and quit the driver
proxy.close()
server.stop()
driver.quit()