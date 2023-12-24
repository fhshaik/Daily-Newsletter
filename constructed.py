import addmodule
import artimage
import addpoetry
import youtubePlaylist
import config
import searcher
import obsidiantool
import re
def poetryfoundationmodule(path):
    tuple=addpoetry.addpoetryfoundation()
    addmodule.createunit(path,"h2",tuple[0])
    addmodule.createunit(path,"h4",tuple[1])
    addmodule.createunit(path,"pre",tuple[2], "poetry")
    addmodule.createbreak(path)
    addmodule.createlink(path,tuple[3], tuple[3])
    addmodule.createdivider(path)
    return

def urduPoemModule(path):
    tuple=addpoetry.urduPoem()
    addmodule.createunit(path,"h2",tuple[0])
    addmodule.createunit(path,"h4",tuple[1])
    addmodule.createColumns(path,tuple[2],tuple[3])
    addmodule.createbreak(path)
    addmodule.createlink(path,tuple[4], tuple[4])
    addmodule.createdivider(path)
    return

def artvee(path):
    tuple=artimage.getrandomimagelinkname()
    addmodule.createunit(path,"h2",tuple[2])
    addmodule.createimage(path,tuple[1])
    addmodule.createlink(path,tuple[0],tuple[0])
    addmodule.createdivider(path)
    return

def youtubeVideo(path, heading, id):
    addmodule.createunit(path, "h2",heading)
    dict=config.read_config()
    link=youtubePlaylist.getVideo(id,dict["API_KEY"][0])
    addmodule.createiframe(path, link)
    addmodule.createdivider(path)
    return

def ObsidianBookRec(path):
    addmodule.createunit(path, "h2","Book Recommendation")
    dict=config.read_config()
    tuple=searcher.findSummary(obsidiantool.getSemiRandomTag(*dict["OBSIDIAN_FOLDERS"], tag="#books")+" book")
    addmodule.createunit(path, "p", tuple[3])
    addmodule.createbreak(path)
    addmodule.createlink(path, tuple[1], tuple[1])
    addmodule.createunit(path, "p", tuple[0])
    addmodule.createdivider(path)
    return

def titleSection(path, heading):
    addmodule.createunit(path, "h1", heading)

def ObsidianMovieRec(path):
    addmodule.createunit(path, "h2","Movie Recommendation")
    dict=config.read_config()
    tuple=searcher.findSummary(obsidiantool.getSemiRandomTag(*dict["OBSIDIAN_FOLDERS"], tag="#movies")+" movie")
    addmodule.createunit(path, "p", tuple[3])
    addmodule.createbreak(path)
    addmodule.createlink(path, tuple[1], tuple[1])
    addmodule.createunit(path, "p", tuple[0])
    addmodule.createdivider(path)
    return

def ObsidianWikiRec(path, number):
    dict=config.read_config()
    currenttag=dict["FOLDER_SEARCHTAG"][number]
    titletag = str.capitalize(re.sub(r'#', '', currenttag))
    addmodule.createunit(path, "h2","Recommendations for "+titletag)
    tuple=searcher.findSummary(obsidiantool.getSemiRandomTag(*dict["OBSIDIAN_FOLDERS"], tag=currenttag))
    addmodule.createunit(path, "p", tuple[3])
    addmodule.createbreak(path)
    addmodule.createlink(path, tuple[1], tuple[1])
    addmodule.createunit(path, "p", tuple[0])
    addmodule.createdivider(path)
    return
def ObsidianFileCurrently(path, number):
    dict=config.read_config()
    currenttag=dict["FILE_SEARCHTAG"][number]
    titletag = str.capitalize(re.sub(r'#', '', currenttag))
    addmodule.createunit(path, "h2","Currently "+titletag)
    parastring=", ".join(obsidiantool.tagFileGetter(number))
    addmodule.createunit(path, "p", parastring)
    addmodule.createbreak(path)
    addmodule.createdivider(path)
    return

