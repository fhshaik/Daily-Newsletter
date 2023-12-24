from bs4 import BeautifulSoup
import requests
import urduPoemExtract

def addpoetryfoundation():
    headers={'User-Agent':'Mozilla/5.0'}
    URL = 'https://www.poetryfoundation.org/poems/poem-of-the-day'
    response = requests.get(URL)
    html = response.text
    soup2 = BeautifulSoup(html, 'html.parser')
    title = soup2.find('div', {'class': 'c-feature-hd'}).h1.text.strip()
    URL=soup2.find('a', text="Read More")['href']
    
    response = requests.get(URL, headers=headers)
    html = response.text
    soup2 = BeautifulSoup(html, 'html.parser')
    author_name = soup2.find('span', {'class': 'c-txt_attribution'}).a.text.strip()
    poem = [line.text for line in soup2.find('div', {'class': 'o-poem'}).find_all('div')]
    poem_html="\n".join(poem)
    soup3 = BeautifulSoup(poem_html, 'html.parser')
    poem_html = str(soup3)
    return(title, "By: "+author_name," "+poem_html, URL)


def urduPoem():
    return urduPoemExtract.urduPoemGet()

