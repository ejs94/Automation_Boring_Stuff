import bs4
import requests
res = requests.get(
    'https://www.amazon.com.br/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elem = soup.select('#a-autoid-5-announce > span:nth-child(3)')
print(elem[0].text.strip())
