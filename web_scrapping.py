import sys, os
import requests
import timeit
from PIL import Image
from bs4 import BeautifulSoup


def get_soup_image(url):
    webpage = requests.get(url)
    soup = bs4.BeautifulSoup(webpage.text, 'html.parser')
    image = soup.find(id='img src')
    return image


counter = 1
while True:
    image = get_soup_image(f'https://www.xkcd.com/{counter}')


# Web scrapping program.
# Write your code here. Have fun!

