import os
import json
import sys
from pathlib import Path # for working paths

# Imports for UI
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QVBoxLayout,
    QWidget
) 
from PySide6.QtCore import Qt

# Find the json files ----------------------
path_small = Path("data_small.json") # path to small json file
path_large = Path("data_large.json") # path to large json file

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

# Create a window ---------------------
app = QApplication([]) 
window = QMainWindow()
window.setWindowTitle("Table") # name that shows at the top of the window
# -------------------------------------

# Creating a small table --------------
table = QTableWidget()
table.setRowCount(len(data_small)) # number of rows in the small table
table.setColumnCount(6) # number of columns in the small table
table.setHorizontalHeaderLabels(["Id", "Nom", "Categorie", "Format", "Polygones", "Statut"]) # header labels/column names
# -------------------------------------

# Creating a large table --------------
table2 = QTableWidget()
table2.setRowCount(len(data_large))
table2.setColumnCount(10)
table2.setHorizontalHeaderLabels(["Id", "Nom", "Categorie", "Format", "Polygones", "Statut", "Auteur", "Date de Creation", "Prix", "Taille du Fichier"])
# -------------------------------------

# Creating a search bar ---------------
searchbar = QLineEdit(placeholderText="Search...") # placeholder text for search bar
container_layout = QVBoxLayout() # creating a layout for things that will be added to the window
container_layout.addWidget(searchbar) # adding search bar to the layout
container_layout.addWidget(table) # adding small table to the layout <<<<<<<<<<<<<<<<<<<<<<<<<<
container_layout.addWidget(table2) # adding large table to the layout <<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------

# Adding search bar and table layout to the main widget --
container = QWidget() # main widget that will show both the search bar and the table
container.setLayout(container_layout) # applying earlier created layout to the widget/container
window.setCentralWidget(container) # adding main widget to the window
# --------------------------------------------------------

# Filling the small table with values -----
def table_update_small():
    for i in range(len(data_small)): # for item in data_small.json
        item = data_small[i]
        table.setItem(i, 0, QTableWidgetItem(item["id"])) # places item's "id" value in the column "id"
        table.setItem(i, 1, QTableWidgetItem(item["nom"]))
        table.setItem(i, 2, QTableWidgetItem(item["categorie"]))
        table.setItem(i, 3, QTableWidgetItem(item["format"]))
        table.setItem(i, 4, QTableWidgetItem(str(item["polygones"]))) # shows "polygons" value (int) as a string (str)
        table.setItem(i, 5, QTableWidgetItem(item["statut"]))
# -----------------------------------------

# Filling the large table with values -----
def table_update_large():
    for i in range(len(data_large)):
        item = data_large[i]
        table2.setItem(i, 0, QTableWidgetItem(item["id"])) # places item's "id" value in the column "id"
        table2.setItem(i, 1, QTableWidgetItem(item["nom"]))
        table2.setItem(i, 2, QTableWidgetItem(item["categorie"]))
        table2.setItem(i, 3, QTableWidgetItem(item["format"]))
        table2.setItem(i, 4, QTableWidgetItem(str(item["polygones"]))) # shows "polygons" value (int) as a string (str)
        table2.setItem(i, 5, QTableWidgetItem(item["statut"]))
        table2.setItem(i, 6, QTableWidgetItem(item["auteur"]))
        table2.setItem(i, 7, QTableWidgetItem(item["date_creation"]))
        table2.setItem(i, 8, QTableWidgetItem(str(item["prix"]))) # shows "prix" value (float) as a string (str)
        table2.setItem(i, 9, QTableWidgetItem(item["taille_fichier"]))
# -----------------------------------------

user_input = searchbar.text()

table_update_small() # recalculates the placement of items in the small table
table_update_large() # recalculates the placement of items in the large table


#table.item(i, column).setBackground(Qt.lightGray)

window.show()


'''columns_s = ["id", "nom", "categorie", "format", "polygones", "statut"] # column indexes
was_clicked = False

def header_clicked_s(index, was_clicked):
    if was_clicked == False:
        data_small.sort(key=lambda item:item[columns_s[index]])
        was_clicked = True
    else:
         data_small.sort(key=lambda item:item[columns_s[index]], reverse=True)
         was_clicked = False

    table_update_small()
    print(was_clicked)
'''
        
'''def header_clicked_l(index):
    if index == 0:
        data_large.sort(key=lambda item: item["id"])
    elif index == 1:
        data_large.sort(key=lambda item: item["nom"])
    elif index == 2:
        data_large.sort(key=lambda item: item["categorie"])
    elif index == 3:
        data_large.sort(key=lambda item: item["format"])
    elif index == 4:
        data_large.sort(key=lambda item: item["polygones"])
    elif index == 5:
        data_large.sort(key=lambda item: item["statut"])
    elif index == 6:
        data_large.sort(key=lambda item: item["auteur"])
    elif index == 7:
        data_large.sort(key=lambda item: item["date_creation"])
    elif index == 8:
        data_large.sort(key=lambda item: item["prix"])
    elif index == 9:
        data_large.sort(key=lambda item: item["taille_fichier"])

    table_update_large()
    window.show()
'''
#table.horizontalHeader().sectionClicked.connect(header_clicked_s)
#table2.horizontalHeader().sectionClicked.connect(header_clicked_l)


sys.exit(app.exec())

'''
for i in data_small:
    for key in i.keys():
        print (key)
        
    for value in i.values():
        print(value)
'''
