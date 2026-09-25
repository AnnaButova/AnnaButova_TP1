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

if path_small.exists() or path_large.exists():
    print("I HAVE BEEN FOUND")
else:
    print("LOL NOPE")
# ------------------------------------------

# Open json small file ---------------------
with open("data_small.json", "r", -1, "utf-8") as json_file_small:
    data_small = json.load(json_file_small)
# ------------------------------------------

# Open json large file ---------------------
with open("data_large.json", "r", -1, "utf-8") as json_file_large:
    data_large = json.load(json_file_large)
# ------------------------------------------

for i in data_small:
    for key, value in i.items():
        print(key, value)


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

table2.show()
sys.exit(app.exec())

'''
for i in data_small:
    for key in i.keys():
        print (key)
        
    for value in i.values():
        print(value)
'''
