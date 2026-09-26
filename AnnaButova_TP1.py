import os
import json
import sys
from pathlib import Path

# Imports for UI
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit
) 

# Find the json files ----------------------
path_small = Path("data_small.json")
path_large = Path("data_large.json")

if path_small.exists() or path_large.exists(): # verification to see if json file exists/can be found
    print("Json file found!:)")
else:
    print("Json file not found! :(")
# ------------------------------------------

# Open json small file ---------------------
try:
    with open("data_small.json", "r", -1, "utf-8") as json_file_small: # opens data_small as a json file
        data_small = json.load(json_file_small)
except(ValueError, FileNotFoundError): # if file contains an error, show error message
    print("File contains an error! Please check your json file and try again.")
# ------------------------------------------

# Open json large file ---------------------
try:
    with open("data_large.json", "r", -1, "utf-8") as json_file_large: # opens data_large as a json file
        data_large = json.load(json_file_large)
except(ValueError, FileNotFoundError): # if file contains an error, show error message
    print("File contains an error! Please check your json file and try again.")
# ------------------------------------------

'''for i in data_small:
    for key, value in i.items():
        print(key, value)
'''
'''id_s = [item["polygones"] for item in data_small]
id_l = [item["id"] for item in data_large]
id_s.sort(reverse=True)
'''

def my_function():
    data_small.sort(key=lambda item: item["id"], reverse=True)
    print("yay!")


# --------------
'''if input("Yes") or input("yes") or input("YES"):
    is_reversed = True
elif input("No") or input("no") or input("NO"):
    is_reversed = False
else:
    print("Please enter yes or no")
'''

app = QApplication([]) 
# window = QMainWindow()


# Table setup ------------------------------------------------------------------------------
table = QTableWidget()
table.setRowCount(len(data_small))
table.setColumnCount(6)
table.setHorizontalHeaderLabels(["Id", "Nom", "Categorie", "Format", "Polygones", "Statut"])
# ------------------------------------------------------------------------------------------

# Table2 setup -----------------------------------------------------------------------------
table2 = QTableWidget()
table2.setRowCount(len(data_large))
table2.setColumnCount(10)
table2.setHorizontalHeaderLabels(["Id", "Nom", "Categorie", "Format", "Polygones", "Statut", "Auteur", "Date de Creation", "Prix", "Taille du Fichier"])
# ------------------------------------------------------------------------------------------

# makes a table for data_small.json --------------------------------------------------------
def table_update_small():
    for i in range(len(data_small)):
        item = data_small[i]
        table.setItem(i, 0, QTableWidgetItem(item["id"])) # shows json elements in the row "id"
        table.setItem(i, 1, QTableWidgetItem(item["nom"]))
        table.setItem(i, 2, QTableWidgetItem(item["categorie"]))
        table.setItem(i, 3, QTableWidgetItem(item["format"]))
        table.setItem(i, 4, QTableWidgetItem(str(item["polygones"]))) # shows polygons (int) as a string (str)
        table.setItem(i, 5, QTableWidgetItem(item["statut"]))
# ------------------------------------------------------------------------------------------

# makes a table for data_large.json --------------------------------------------------------
def table_update_large():
    for i in range(len(data_large)):
        item = data_large[i]
        table2.setItem(i, 0, QTableWidgetItem(item["id"])) # shows json elements in the row "id"
        table2.setItem(i, 1, QTableWidgetItem(item["nom"]))
        table2.setItem(i, 2, QTableWidgetItem(item["categorie"]))
        table2.setItem(i, 3, QTableWidgetItem(item["format"]))
        table2.setItem(i, 4, QTableWidgetItem(str(item["polygones"]))) # shows polygons (int) as a string (str)
        table2.setItem(i, 5, QTableWidgetItem(item["statut"]))
        table2.setItem(i, 6, QTableWidgetItem(item["auteur"]))
        table2.setItem(i, 7, QTableWidgetItem(item["date_creation"]))
        table2.setItem(i, 8, QTableWidgetItem(str(item["prix"])))
        table2.setItem(i, 9, QTableWidgetItem(item["taille_fichier"]))
# ------------------------------------------------------------------------------------------

table_update_small()
table.show()
#table2.show()

def header_clicked(index):
    if index == 0:
        data_small.sort(key=lambda item: item["id"])
    elif index == 1:
        data_small.sort(key=lambda item: item["nom"])
    elif index == 2:
        data_small.sort(key=lambda item: item["categorie"])
    elif index == 3:
        data_small.sort(key=lambda item: item["format"])
    elif index == 4:
        data_small.sort(key=lambda item: item["polygones"])
    elif index == 5:
        data_small.sort(key=lambda item: item["statut"])
    elif index == 6:
        data_small.sort(key=lambda item: item["auteur"])
    elif index == 7:
        data_small.sort(key=lambda item: item["date_creation"])
    elif index == 8:
        data_small.sort(key=lambda item: item["prix"])
    elif index == 9:
        data_small.sort(key=lambda item: item["taille_fichier"])

    table_update_small()
    table.show()
    
table.horizontalHeader().sectionClicked.connect(header_clicked)


sys.exit(app.exec())

'''
for i in data_small:
    for key in i.keys():
        print (key)
        
    for value in i.values():
        print(value)
'''
