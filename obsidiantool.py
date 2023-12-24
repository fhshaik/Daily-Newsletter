import os
import random
import re
import config
import json
from datetime import datetime, timedelta
dir =os.path.dirname(os.path.abspath(__file__))
path=dir+"\\data.json"





def newTagGetter(path, tag, date):
    result_lines = []
    # Convert the specified date to a datetime object
    specified_date = date
    # Iterate through all files in the folder
    
    for root, _, files in os.walk(path):
        for file_name in files:
            if file_name.endswith('.md'):
                # Extract the date portion from the file name (assuming it's in YYYY-MM-DD format)
                file_date_str = file_name.split('.')[0]
                
                try:
                    file_date = datetime.strptime(file_date_str, '%Y-%m-%d')
                    
                    # Check if the file date is greater than or equal to the specified date
                    if file_date >= specified_date:

                        file_path = os.path.join(root, file_name)

                        with open(file_path, 'r', encoding='utf-8') as file:
                            lines = file.readlines()
                            # Search for the target tag in each line of the file
                            for line in lines:
                                if tag in line:
                                    result_lines.append((line.strip(),file_path))
                except ValueError:
                    # Handle cases where the file name doesn't match the expected format
                    pass
                
    return result_lines

def getSemiRandomTag(*paths, tag):
    ListChecker(tag)
    for path in paths:
        ListAdder(path, tag=tag)

    with open(dir+'\\taglist.json', 'r') as json_file:
        data = json.load(json_file)

    list=data[tag][:len(data[tag]) // 2]
    choice=random.choice(list)
    element = data[tag].pop(list.index(choice))
    data[tag].append(element)
    with open(dir + '\\taglist.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return choice[0]

def ListChecker(tag):
    with open(dir+'\\taglist.json', 'r') as json_file:
        data = json.load(json_file)
    index_to_remove = []

    if tag not in data:
        data[tag] = []

    for i in range(len(data[tag])):
        found=False
        with open(data[tag][i][1], 'r', encoding='utf-8') as file:
            lines = file.readlines()
            word=data[tag][i][0]
            for line in lines:
                    if word in line:
                        found=True
                        break
            if not found:
                index_to_remove.append(i)
    for index in reversed(index_to_remove):
        data[tag].pop(index)
    with open(dir + '\\taglist.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return

def ListAdder(path, tag):
    try:
        with open(dir+'\\lastdate.json', 'r') as file:
            lastdate = json.load(file)
    except FileNotFoundError:
        lastdate = None
    #need to convert lastdate to date object
    file_path = dir+'\\taglist.json'
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    if(tag not in lastdate):
        lastdate[tag]="2000-1-1"
    
    result_lines=newTagGetter(path, tag, datetime.strptime(lastdate[tag], '%Y-%m-%d')-timedelta(2))
    for tuple in result_lines:
        wordlist=[]
        wordlist.extend(cleanStringList(tuple[0]))
        if tag not in data:
            data[tag] = []
        for a in wordlist:
            if not [a,tuple[1]] in data[tag]:
                data[tag].append([a,tuple[1]])
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # indent for pretty formatting


    lastdate[tag]=datetime.now().strftime('%Y-%m-%d')

    # Update the last date in the JSON file
    with open(dir+'\\lastdate.json', 'w') as file:
        json.dump(lastdate, file)
    

def cleanStringList(string):
    # Split the input string by commas and choose a random element

    cleanString=[]
    cleanString = string.split(",")
    cleanedList=[]
    if len(cleanString)>0:
        for a in cleanString:
            # Remove hashtags, text within parentheses, and links
            a = re.sub(r'#\w+\s*', '', a)
            a = re.sub(r'\([^)]*\)', '', a)
            a = re.sub(r'\[([^\]]+)\]\([^)]+\)', '', a)
            newa = re.sub(r'https?://\S+', '', a)

            # If the cleaned string is empty, return the original input string

            if not newa.strip():
                # Find all links in the cleaned string
                links = re.findall(r'https?://\S+', a)
                # If there are multiple links, choose a random one
                if links:
                    links=[element.strip() for element in links]
                    cleanedList.extend(links)
                #handle case
            else:
                cleanedList.append(newa)
    return cleanedList

def tagFileGetter(number):
    dict=config.read_config()
    tag=dict["FILE_SEARCHTAG"][number]
    file_path=dict["OBSIDIAN_FILE"][0]
    result_lines=[]
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Search for the target tag in each line of the file
        for line in lines:
            if tag in line:
                result_lines.extend(cleanStringList(line.strip()))

    return result_lines

dict=config.read_config()
tag=dict["FOLDER_SEARCHTAG"][0]
file_path=dict["OBSIDIAN_FOLDERS"][0]
getSemiRandomTag(file_path, tag=tag)
