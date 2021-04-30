import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.bing.com/images/search?q=ayam+goreng&qs=n&form=QBIDMH&sp=-1&pq=ayam+gore&sc=8-9&cvid=5EBA5651E32A4DBC8C139E46CD8808E7&first=1&tsc=ImageBasicHover") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])
