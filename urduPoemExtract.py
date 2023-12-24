import os
import random

def urduPoemGet():
    # Define the path to the "dataset" folder
    dataset_folder = 'dataset'

    dir =os.path.dirname(os.path.abspath(__file__))+"\\urdupoetry"

    path=dir+"\\" +dataset_folder
    # List all subfolders (languages) in the "dataset" folder

    if os.path.isdir(path):
        # List all subdirectories in the directory
        subdirectories = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]

        if subdirectories:
            # Randomly select a subdirectory
            selected_folder = random.choice(subdirectories)

    folderpath=path+"\\"+selected_folder+"\\"+"en"
    print(folderpath)
    if os.path.isdir(folderpath):
        # List all files in the folder
        files = [file for file in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, file))]

        if files:
            # Randomly select a file from the list
            selected_file = random.choice(files)

    titlelist=selected_file.split("-")
    title = ' '.join(word.capitalize() for word in titlelist)

    poetlist=selected_folder.split("-")
    poet = ' '.join(word.capitalize() for word in poetlist)


    filepathEnglish=path+"\\"+selected_folder+"\\"+"en"+"\\"+selected_file
    filepathUrdu=path+"\\"+selected_folder+"\\"+"ur"+"\\"+selected_file
    filepathHindi=path+"\\"+selected_folder+"\\"+"hi"+"\\"+selected_file

    poemType=selected_file.split("-")[-1]
    link="https://www.rekhta.org"

    if poemType=="ghazals":
        link+="/ghazals/"+selected_file
    elif poemType=="nazms":
        link+="/nazms/"+selected_file
    elif poemType=="sher":
        link+="/sher/"+selected_file
    else: 
        pass


    urdu_text = ""
    hindi_text=""
    english_text=""
    try:
        with open(filepathUrdu, 'r', errors='ignore', encoding="utf-8") as file:
            # Read and print each line in the file
            for line in file:
                urdu_text += line.strip() + "\n"
    except:
        pass
    try:
        with open(filepathEnglish, 'r', errors='ignore', encoding="utf-8") as file:
            # Read and print each line in the file
            for line in file:
                english_text += line.strip() + "\n"
    
    except:
        pass
    return (title,"By: "+ poet, urdu_text, english_text, link)

