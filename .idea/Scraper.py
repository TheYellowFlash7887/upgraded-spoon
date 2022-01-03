import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
URL2 = 'https://www.cardmarket.com/en/Magic/Data/Weekly-Top-Cards'
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL2)
soup = BeautifulSoup(page.content, "html.parser")
tables = soup.findAll('table')
dfs = list()
#filters all retreived Divs for the Class algn-r as this is how the website floats the price next to the name of the cards
prices= soup.findAll('div',class_='algn-r')
#uses a regular expression to partial match the URL that the website uses to hyperline the card name to the sales page for that card
name= soup.findAll('a', href=re.compile(r"^/en/Magic/Products/Singles/"))
#makes a pandas dataframe for easier programatic manpulation of the page ( currently not used for anything )
for table in tables:
    df = pd.read_html(str(table))[0]
    dfs.append(df)
for index in range(0,(len(prices)-1)):
    print(name[index].text.strip(),prices[index].text.strip())

