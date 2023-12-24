from googlesearch import search
import wikipedia
import wikipediaapi
import re
import random
import urllib
useragent="My Wikipedia API Client/1.0 (livetigan@gmail.com)"
wiki_wiki = wikipediaapi.Wikipedia( user_agent=useragent) 
defaultList=["https://en.wikipedia.org/wiki/A_Thousand_Splendid_Suns"]
def findLink(input_text):
    for result in search(input_text, tld="com", lang="en", num=5, stop=5, pause=1):
        # Check if the result is a YouTube link
        if "youtu.be" in result or "youtube.com" in result:
            return result

        # Check if the result is a Wikipedia link
        if "wikipedia.org" in result:
            return result
    return random.choice(defaultList)

def findWikiLink(input_text):
    for result in search(input_text, tld="com", lang="en", num=10, stop=10, pause=1):
        # Check if the result is a Wikipedia link
        if "wikipedia.org" in result:
            return (input_text, result)
    return (input_text, random.choice(defaultList))

def summarizeWiki(link):
    wikiname=urllib.parse.unquote(link[1].split('/')[-1]).replace("_", " ")
    
    wikitext=wiki_wiki.page(wikiname).summary
    return(link[0], link[1],wikiname,wikitext)

def findSummary(input_text):
    return summarizeWiki(findWikiLink(input_text))

