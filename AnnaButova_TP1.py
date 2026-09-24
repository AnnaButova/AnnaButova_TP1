import PySide6
import os # importer la librairie pour communiquer avec le système d'exploitation
import json

print("Yo! I work!")

if os.path.exists("data_small.json"): # with os check if json file exists, show message accordingly
    print("The file exists.") 
else:
    print("The file does not exist.")

with open("data_small.json", "r", -1, "UTF-8") as json_file: # opens the file
    data = json.load(json_file) # converts file to .json format

print(data[0]) # prints the first "block" of the json file