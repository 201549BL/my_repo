import bs4
import requests



def make_soup(url):
    webpage = requests.get(url)
    if webpage.status_code == 200:
        soup = bs4.BeautifulSoup(webpage.text, 'html.parser')
        title = soup.find(id='ctitle')
        return title, True
    else:
        return False

def get_str_title(soup):
    str_title = str(soup)
    str_title = str_title[18:-13]
    return str_title

def store_title(title):
    list_of_titles.append(title)

counter = 1
list_of_titles = []
#dictionary_of_titles = {
#    "title":
#}
while True:
    soup = make_soup(f'https://www.xkcd.com/{counter}')
    a = get_str_title(soup)
    store_title(a)
    print(a)
    counter += 1


