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
    QWidget,
    QLabel
) 

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
# -------------------------------------

# Adding table widgets ----------------
def add_table_s():
    container_layout.addWidget(table) # adding small table to the layout
def add_table_l():
    container_layout.addWidget(table2) # adding large table to the layout
# -------------------------------------

# Bottom Info Small table -------------------------
file_name_s = Path("data_small.json").name # extracts the name of the file
file_size_s = str(float(os.path.getsize("data_small.json"))) + (" Mb") # extracts the size of the small file in Mb (int)
file_elements_s = str(len(data_small)) + (" elements in table") # extracts the number of items in the small table

size_s = QLabel(file_size_s)
name_s = QLabel(file_name_s)
elements_s = QLabel(file_elements_s)

def show_info_s(): # shows info of the small table
    container_layout.addWidget(name_s)
    container_layout.addWidget(size_s)
    container_layout.addWidget(elements_s)
# -------------------------------------

# Bottom Info Large table -------------------------
file_name_l = Path("data_large.json").name # extracts the name of the file
file_size_l = str(os.path.getsize("data_large.json")) + (" Mb") # extracts the size of the large file in Mb (int)
file_elements_l = str(len(data_large)) + (" elements in table") # extracts the number of items in the large table

size_l = QLabel(file_size_l)
name_l = QLabel(file_name_l)
elements_l = QLabel(file_elements_l)

def show_info_l(): # shows info of the large table
    container_layout.addWidget(name_l)
    container_layout.addWidget(size_l)
    container_layout.addWidget(elements_l)
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


table_update_small() # recalculates the placement of items in the small table
table_update_large() # recalculates the placement of items in the large table

table_shown = input("Which table would you like to see?\n1 - Small\n2 - Large\n").lower()

while table_shown != "1" or table_shown != "small" or table_shown != "2" or table_shown != "large":
    if table_shown == "1" or table_shown == "small":
        add_table_s()
        show_info_s() # shows small table info
        window.show() # shows the small table
        break

    elif table_shown == "2" or table_shown == "large":
        add_table_l()
        show_info_l() # shows large table info
        window.show() # shows the large table
        break
    else:
        print("Invalid answer. Please try again!") # in case of invalid answer, shows error message
        break


# Sorting system small ------------------------------------------------------
columns_s = ["id", "nom", "categorie", "format", "polygones", "statut"] # column indexes
was_clicked_s= False # state of button (if it has been clicked) for the small table

def header_clicked_s(index):

    global was_clicked_s # makes it possible to modify the variable outside of the function

    if was_clicked_s == False: # was_clicked_s is used to switch between the sorting types
        data_small.sort(key=lambda item:item[columns_s[index]]) # sorts items in the table (ascending order)
        was_clicked_s = True
    else:
         data_small.sort(key=lambda item:item[columns_s[index]], reverse=True) # sorts items in the table (descending order)
         was_clicked_s = False

    table_update_small()
# ---------------------------------------------------------------------------

# Sorting system large ------------------------------------------------------
columns_l = ["id", "nom", "categorie", "format", "polygones", "statut", "auteur", "date_creation", "prix", ] # column indexes
was_clicked_l = False # state of button (if it has been clicked) for the large table

def header_clicked_l(index):

    global was_clicked_l # makes it possible to modify the variable outside of the function

    if was_clicked_l == False: # was_clicked_l is used to switch between the sorting types
        data_large.sort(key=lambda item:item[columns_l[index]]) # sorts items in the table (ascending order)
        was_clicked_l = True
    else:
         data_large.sort(key=lambda item:item[columns_l[index]], reverse=True) # sorts items in the table (descending order)
         was_clicked_l = False

    table_update_large()
# ---------------------------------------------------------------------------

# Sort when header label has been clicked -----------------------------------
table.horizontalHeader().sectionClicked.connect(header_clicked_s)
table2.horizontalHeader().sectionClicked.connect(header_clicked_l)
# ---------------------------------------------------------------------------

def search(text):
    for row in range(table.rowCount()): # for each row in the table
        #row_match = False
        for column in range(table.columnCount()): # for each column in the table
            item = table.item(row, column) # searches for the item in row and column

            if item:
                match = text.lower() in item.text().lower()
                #row_match = True
                table.setRowHidden(row, not match)

searchbar.textChanged.connect(search)
    

sys.exit(app.exec()) # exits program when the window is closed
