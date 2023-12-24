import constructed
import os
import datetime
import webbrowser

dir =os.path.dirname(os.path.abspath(__file__))
template_file = dir +"\\newslettertemplate.html"
newfile=dir+f"\\Daily Newsletters\\{datetime.date.today()}.html"

moduleDictionary={"title": lambda: constructed.titleSection(path, datetime.date.today().strftime("%B %d, %Y")+" Newsletter"),
                  "artwork": lambda:constructed.artvee(path),
                  "poem": lambda:constructed.poetryfoundationmodule(path),
                  "youtube": lambda x,y: constructed.youtubeVideo(path,x,y),
                  "currently": lambda x: constructed.ObsidianFileCurrently(path, int(x)),
                  "obsidianWikiRec": lambda x: constructed.ObsidianWikiRec(path,int(x)),
                  "obsidianBookRec":lambda: constructed.ObsidianBookRec(path),
                  "obsidianMovieRec": lambda: constructed.ObsidianMovieRec(path),
                  "urdupoem": lambda: constructed.urduPoemModule(path)}

if not os.path.exists(newfile):
    with open(template_file, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    with open(newfile, 'w', encoding='utf-8') as updated_html_file:
            updated_html_file.write(str(html_content))

    path=newfile

    with open(dir+"\\custom.txt", "r", encoding="utf-8") as file:
        for line in file:
            try:
                currentFunc=line.split()
                if(len(currentFunc)==1):
                    moduleDictionary[currentFunc[0]]()
                else:
                    moduleDictionary[currentFunc[0]](*currentFunc[1:])
            except:
                pass

webbrowser.open('file:\\' + newfile)
