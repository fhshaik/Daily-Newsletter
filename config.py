# Define a function to read the API key and playlist IDs from a file
import os

def read_config():
    config = {}
    current_directory = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(current_directory+"\\config.txt", "r", encoding="utf-8") as file:
            for line in file:
                key, value = (r''+line).strip().split(": ")
                listofids=[]
                listofids.extend(value.split(","))
                listofids = [value.strip() for value in listofids]
                config[key] = listofids
        return config
    except FileNotFoundError:
        print("File not found.")
        return None
