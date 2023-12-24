import random
from requests_html import HTMLSession
from requests_html import HTML

def getrandomimagelinkname():
    session=HTMLSession()
    r=session.get("https://artvee.com")
    links=list(r.html.links)
    artlinks=[]
    for a in links:
        if "/dl/" in a:
            artlinks.append(a)

    artlink=random.choice(artlinks)
    s=session.get(artlink)
    html = HTML(html=s.text)
    thing=s.html.find("img")
    link=""
    for a in thing:
        if "https://mdl.artvee.com/sftb" in a.html:
            link=a.html
            break
    brokenlink=link.split('"')
    truelink=brokenlink[1]
    return (artlink, truelink, brokenlink[5])