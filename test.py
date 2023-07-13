import requests
from bs4 import BeautifulSoup
 
url = "https://pokeka-search.com/search_list.php?card_name=&paku=&hp=0&waza1energy1=0&waza1energy2=0&waza1energy3=0&waza1energy4=0&waza1energy5=0&waza1iryoku=0&waza1iryokumaku=0&waza2energy1=0&waza2energy2=0&waza2energy3=0&waza2energy4=0&waza2energy5=0&waza2iryoku=0&waza2iryokumaku=0&waza3energy1=0&waza3energy2=0&waza3energy3=0&waza3energy4=0&waza3energy5=0&waza3iryoku=0&waza3iryokumaku=0&zyakuten=0&teikouryoku=0"
 
r = requests.get(url)
r.encoding = r.apparent_encoding
 
soup = BeautifulSoup(r.text, 'html.parser')
cards = soup.find('tbody').find_all('tr')
 
for card in cards:
    name = card.find('a').text

    print('*****************')
    print(name)
    print()