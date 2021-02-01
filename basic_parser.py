import pandas as pd
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Basic Stats Parser
URL = 'https://www.basketball-reference.com/players/e/embiijo01/gamelog/2021/'
soup = BeautifulSoup(urlopen(URL), "html.parser")
for elem in soup.findAll("table", {"id":"pgl_basic"}):
    print(str(elem))
data = []