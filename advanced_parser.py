import pandas as pd
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Advanced Stats Parser
URL = 'https://www.basketball-reference.com/players/e/embiijo01/gamelog-advanced/2021/'
soup = BeautifulSoup(urlopen(URL), "html.parser")
for elem in soup.findAll("tr", {"id":"pgl_advanced"}):
    print(str(elem))
data = []