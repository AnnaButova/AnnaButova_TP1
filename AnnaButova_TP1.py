import os
import json
import sys
from pathlib import Path

# Imports for UI
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem
) 

# Find the json files ----------------------
path_small = Path("data_small.json")
path_large = Path("data_large.json")

if path_small.exists() or path_large.exists():
    print("I HAVE BEEN FOUND")
else:
    print("LOL NOPE")
# ------------------------------------------

# Open json file ---------------
with open("data_small.json", "r", -1, "utf-8") as json_file_small:
    data_small = json.load(json_file_small)
# ------------------------------------------

for i in data_small:
    for key, value in i.items():
        print(key, value)


app = QApplication([])
window = QMainWindow()

table = QTableWidget()
table.setRowCount(len(data_small))
table.setColumnCount(6)
table.setHorizontalHeaderLabels(["Id", "Nom", "Categorie", "Format", "Polygones", "Statut"])

for i in range(len(data_small)):
    item = data_small[i]
    table.setItem(i, 0, QTableWidgetItem(item["id"])) # shows json elements in the row "id"
    table.setItem(i, 1, QTableWidgetItem(item["nom"]))
    table.setItem(i, 2, QTableWidgetItem(item["categorie"]))
    table.setItem(i, 3, QTableWidgetItem(item["format"]))
    table.setItem(i, 4, QTableWidgetItem(str(item["polygones"]))) # shows polygons (int) as a string (str)
    table.setItem(i, 5, QTableWidgetItem(item["statut"]))

table.show()
sys.exit(app.exec())

'''
for i in data_small:
    for key in i.keys():
        print (key)
        
    for value in i.values():
        print(value)
'''
