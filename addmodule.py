from bs4 import BeautifulSoup
import html
def createunit(newsfile, h, unit, style=None):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a heading (e.g., <h1>) element
    node = soup.new_tag(h)
    node.string = html.unescape(unit)
    node["class"]=style

    # Find the <div> element with the class "container" and append the heading and paragraph to it
    div_container = soup.find('div', class_='container')
    div_container.append(node)
    modified_html = soup.prettify()
    # Write the modified content back to the same HTML file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
    return
def createimage(newsfile, link, unit=""):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a heading (e.g., <h1>) element
    node = soup.new_tag('img')
    node["src"]=link
    node.string=html.unescape(unit)

    # Find the <div> element with the class "container" and append the heading and paragraph to it
    div_container = soup.find('div', class_='container')
    div_container.append(node)
    modified_html = soup.prettify()
    # Write the modified content back to the same HTML file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
    return


def createlink(newsfile, link, unit):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a heading (e.g., <h1>) element
    node = soup.new_tag('a')
    node["href"]=link
    node.string=html.unescape(unit)

    # Find the <div> element with the class "container" and append the heading and paragraph to it
    div_container = soup.find('div', class_='container')
    div_container.append(node)
    modified_html = soup.prettify()
    # Write the modified content back to the same HTML file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
    return

def createdivider(newsfile):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a heading (e.g., <h1>) element
    node = soup.new_tag('hr')

    # Find the <div> element with the class "container" and append the heading and paragraph to it
    div_container = soup.find('div', class_='container')
    div_container.append(node)
    modified_html = soup.prettify()
    # Write the modified content back to the same HTML file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
    return

def createiframe(newsfile, src):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a heading (e.g., <h1>) element
    node = soup.new_tag('iframe')
    node["src"]=src
    # Find the <div> element with the class "container" and append the heading and paragraph to it
    div_container = soup.find('div', class_='container')
    div_container.append(node)
    modified_html = soup.prettify()
    # Write the modified content back to the same HTML file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
    return
def createbreak(newsfile):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a heading (e.g., <h1>) element
    node = soup.new_tag('br')

    # Find the <div> element with the class "container" and append the heading and paragraph to it
    div_container = soup.find('div', class_='container')
    div_container.append(node)
    modified_html = soup.prettify()
    # Write the modified content back to the same HTML file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
    return

def createColumns(newsfile, para1, para2, style=None):
    with open(newsfile, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()


    soup = BeautifulSoup(html_content, 'html.parser')
    

    container = soup.find('div', class_='container')


    two_columns = soup.new_tag("div")
    two_columns["class"]="two-columns"
    

    column1 = soup.new_tag("pre")
    column1["class"]="poetry"
    column1.string = html.unescape(para1)
    two_columns.append(column1)
    

    column2 = soup.new_tag("pre")
    column2["class"]="poetry"
    column2.string = html.unescape(para2)
    two_columns.append(column2)
    

    container.append(two_columns)
    
    # Get the modified HTML content
    modified_html = soup.prettify()
    
    # Write the modified HTML back to the file
    with open(newsfile, "w", encoding="utf-8") as html_file:
        html_file.write(modified_html)
