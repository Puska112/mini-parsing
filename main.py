import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://sneakerstudio.pl/pol_m_Meskie_BUTY-MESKIE_Sneakersy-meskie-2475.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
quoters = soup.find_all('strong', class_='price')
for i in quoters:
    print(i.text)
