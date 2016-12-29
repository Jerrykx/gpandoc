import io
import os
import sys
import glob
import recipe
import pypandoc
import datetime
import configparser


from os import path
import subprocess 
from subprocess import call
from zipfile import ZipFile

from PIL import Image,ImageQt
from ui import recipe_ui
from ui import variables_ui
from ui.mainwindow_ui import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QFile, QFileDevice, QFileSelector, QFileInfo, QDirIterator, pyqtWrapperType, qDebug, Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QSlider, QTextEdit, QDialog, QDialogButtonBox, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView,QMouseEventTransition, QSizePolicy, \
                            QSpacerItem, QAction, QDialog, QComboBox, QListView



# <<< SETTINGS Variables >>> # 
listPaths=[]
class CurrentConfig():
    
    def __init__(self):
        super(CurrentConfig, self).__init__()
        File = open("conf.py", "r+")
        self.load_conf(File)
        
    def load_conf(self, File):  
        pass

    def save_conf(self,File):
        pass

# <<< END of: SETTINGS Variables >>> # 

        
# <<< MAINWINDOW >>> #

class MyListWidgetItem(QListWidgetItem):
    # << Custom Main Widget >> #
    def __init__(self, text):
        super(MyListWidgetItem, self).__init__()
        self.path=""
    def showPath(self):
        return self.path

    def setPath(self,text):
        self.path = text

class MainWindow(QMainWindow, Ui_MainWindow):

  # << Custom Main Widget >> #
    def __init__(self, app):
        super(MainWindow, self).__init__()
              
        Ui_MainWindow.setupUi(self, self)
        self.line_edit_1.setToolTip("Nazwa dokumentu bez rozszerzenia. Wynik konwersji zostanie zapisany w folderze\"/outputs\"."+
                                    "Wiele plików będzie posiadać jedną nazwę z dopisanym numerem np. book_1")
        now = datetime.datetime.now()
        self.line_edit_1.setText(str(now.strftime("%Y-%m-%d_%H:%M_book")))
        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_2.clicked.connect(self.select_recipe)
        self.push_button_3.clicked.connect(self.conf_variables)
        self.push_button_4.clicked.connect(self.clear_selected_items)
        self.push_button_5.clicked.connect(self.clear_all_items)
        self.show()
                   
        self.list_widget_1.setAcceptDrops(True)
        self.list_widget_1.setMouseTracking(True)
        self.list_widget_1.verticalScrollBar()
        self.list_widget_1.horizontalScrollBar()
        self.list_widget_1.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_widget_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.list_widget_1.currentItemChanged.connect(self.items_changed)

    # Actions for mouse right click #
        quit_action_1 = QAction("Zamknij", self, shortcut="Ctrl+Q", triggered=QApplication.instance().quit)
        quit_action_2 = QAction("Czyść", self, triggered=self.clear_all_items)
        quit_action_3 = QAction("Zaznacz wszystko", self, shortcut="Ctrl+A", triggered=self.select_items)
        quit_action_4 = QAction("Usuń zaznaczone", self, shortcut="Del", triggered=self.clear_selected_items)
        self.list_widget_1.addAction(quit_action_4)
        self.list_widget_1.addAction(quit_action_3)
        self.list_widget_1.addAction(quit_action_2)
        self.list_widget_1.addAction(quit_action_1)

    # Info for users how to add files
        self.list_widget_1.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.push_button_1.setToolTip("Kliknij, aby dodać pliki do listy")
        self.push_button_2.setToolTip("Kliknij, aby wybrać przepis")

        self.push_button_3.setToolTip("Kliknij, aby przejść do wygenerowania dokumentu")
        self.push_button_4.setToolTip("Kliknij, aby usunać zaznaczone elementy")
        self.push_button_5.setToolTip("Kliknij, aby wyczyścić liste")

        self.returnedFiles = []
        self.boxIsChecked = False
        self.selectedRecipe = None
        self.pathDirectory = os.path.dirname(__file__) 
        self.items_changed()

 # << END of: Custom Main Widget >> #
 # << Listwidget handling >> #2

    # clear current selected item
    def clear_selected_items(self):
        for select in self.list_widget_1.selectedItems():    
            self.list_widget_1.takeItem(self.list_widget_1.row(select))
        self.items_changed()
       
         
    def items_changed(self):
        if self.selectedRecipe == None or self.list_widget_1.count()==0:
            self.push_button_3.setEnabled(False)
        else:
            self.push_button_3.setEnabled(True)
     
    # clear all files on the list
    def clear_all_items(self):
        self.list_widget_1.clear()
        self.items_changed()

    # select all files on the list
    def select_items(self):
        self.list_widget_1.selectAll();
        #print("\n" + str(listPaths)) # chcek list values: listPaths
        for x in range(self.list_widget_1.count()):
            print(self.list_widget_1.item(x).showPath())

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.items_changed()

 # << ADD paths on list_widget_1 from listPaths used pop()  >> #
    def add_to_list_widget(self, listPaths):
        for path in listPaths:
            fileName = str(path).split("/")     
            item = MyListWidgetItem(path)   
            item.setText(fileName[-1])
            item.setPath(str(path))
            self.list_widget_1.addItem(item)
     
 # << Load files on >> #

    def infoFormats(self):
        print(pypandoc.get_pandoc_formats())

    def load_files(self):
        listPaths = []
        files, _ = QFileDialog.getOpenFileNames(self, "Wybierz pliki", '',
                                                "Wszystkie (*);;"+"commonmark (*.commonmark);;"+
                                                "docbook (*.docbook);;"+"docx (*.docx);;"+"epub (*.epub);;"+
                                                "haddock (*.haddock);;"+"html (*.html);;"+"json (*.json);;"+
                                                "latex (*.latex);;"+"markdown (*.markdown *.md);;"+"markdown_github (*.markdown_github);;"+
                                                "markdown_mmd (*.markdown_mmd);;"+"markdown_phpextra (*.markdown_phpextra);;"+
                                                "markdown_strict (*.markdown_strict);;"+"mediawiki (*.mediawiki);;"+
                                                "native (*.native);;"+"odt (*.odt);;"+"opml (*.opml);;"+"org (*.org);;"+
                                                "rst (*.rst);;"+"t2t (*.t2t);;"+"textile (*.textile);;"+"twiki (*.twiki)")

        for file in files:
            listPaths.append(file)
        print(listPaths)
        self.infoFormats()
        self.add_to_list_widget(listPaths)
        self.items_changed()
   
 # << END of: Load files on >> #
    def return_boxIsChecked(self):
        self.isChecked =  self.check_box_1.checkState() 
        return self.isChecked
     
    def return_files(self):
        self.returnedFiles = []
        for x in range(self.list_widget_1.count()):
            self.returnedFiles.append(self.list_widget_1.item(x).showPath())
        print("Return files: ", self.returnedFiles)
        return self.returnedFiles
 # << >>
  
 # << Select recipe - handling >> # 
    def select_recipe(self):
        recipeDialog=None
        recipeDialog = RecipeDialog(recipeDialog, self.selectedRecipe) 
        self.selectedRecipe = recipeDialog.retRecipe()
        self.items_changed()
        print(self.selectedRecipe)
        
 # << END of: Select recipe - handling >> #with ZipFile('spam.zip') as myzip:
 

    def conf_variables(self):
        bookName = str(self.line_edit_1.text())
        variablesDialog = VariablesDialog(self.selectedRecipe, self.return_files(), self.return_boxIsChecked(), self.pathDirectory, bookName)
        variablesDialog.exec_()
        self.shellCommand()
    
    def shellCommand(self):
        command = None


# <<< END OF MAINWINDOW >>> #


# <<< CONFIG VARIABLES >>> #

class Table(QtWidgets.QTableWidget):

    def __init__(self):
        super(Table, self).__init__()
        self.rows_number = 0
        self.columns_number = 1
        self.setRowCount(self.rows_number)
        self.setColumnCount(self.columns_number)
        self.setup_empty_table()

        # < ADD PushButton and connect with function add_cell > #
        self.button_form = QtWidgets.QPushButton()
        self.button_form.setText("Nowe pole")
        self.button_form.clicked.connect(self.add_cell)      
        
        self.button_form2 = QtWidgets.QPushButton()
        self.button_form2.setText("Usuń pole")
        self.button_form2.clicked.connect(self.remove_cell)


    def setup_empty_table(self):
        self.horizontalHeader().setStretchLastSection(True)
        self.setMinimumHeight(120)
        self.setMaximumHeight(180)
        self.add_cell()
        for x in range(self.rows_number):
            self.setRowHeight(x, 30)

    def add_cell(self):
        self.rows_number = (self.rowCount())
        self.insertRow(self.rows_number)
        self.setItem(self.rows_number, 0, QtWidgets.QTableWidgetItem(""))
        if int(self.rows_number) > 3:
            self.setMinimumHeight(150)
            self.setMaximumHeight(300)
            for x in range(self.rowCount()):
                self.setRowHeight(x, 20)
        self.show()
        
    def remove_cell(self):
        self.current_row = self.currentRow()
        self.removeRow(self.currentRow())
        self.show()
         
        
class RecipeDialog(QtWidgets.QDialog, recipe_ui.Ui_Dialog):
    def __init__(self,app,selectedRecipe):
        super(RecipeDialog, self).__init__()
        recipe_ui.Ui_Dialog.setupUi(self, self)
        
        self.zipPackages =[]
        self.loadedRecipe = selectedRecipe
        self.path = os.path.dirname(__file__)     
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = recipe_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.label_1.setScaledContents(True);
        
        self.zipPackages  = [os.path.basename(x) for x in glob.glob(self.path+'/zips/*.zip')]
        print (self.zipPackages)
        
        self.dialog.ui.combo_box_1.addItems(self.zipPackages)
        print(self.dialog.ui.combo_box_1.currentText())
        self.dialog.ui.combo_box_1.currentIndexChanged[str].connect(self.changeRecipe)   
        self.dialog.ui.button_box_1.accepted.connect(self.accept)
        self.dialog.ui.button_box_1.rejected.connect(self.reject)
        self.dialog.exec_()
        
    def accept(self): 
        self.loadedRecipe = str(self.path+ "/zips/" + str(self.dialog.ui.combo_box_1.currentText()))
        print("Current loaded recipe: "+ self.loadedRecipe)
        self.retRecipe()
        super().accept()
    
    def reject(self):
        super().reject()
    
    def retRecipe(self):
        return (self.loadedRecipe)

    def setRecipe(self):
        self.dialog.ui.combo_box_1.setCurrentText(str(self.loadedRecipe))
    def changeRecipe(self): 
        print (str('zips/'+self.dialog.ui.combo_box_1.currentText()))
        zippedImgs = ZipFile(self.path+'/zips/'+str(self.dialog.ui.combo_box_1.currentText()))
        for i in range(len(zippedImgs.namelist())):
            file_in_zip = zippedImgs.namelist()[i]
            if (".png" in file_in_zip or ".PNG" in file_in_zip):
                print ("Found image: ", file_in_zip, " -- ")
                data = zippedImgs.read(file_in_zip)       # read bits to variable                                                      
                dataEnc = io.BytesIO(data)                # save bytes like io              
                dataImgEnc = Image.open(dataEnc)          # convert bytes on Image file            
                qimage = ImageQt.ImageQt(dataImgEnc)      # create QtImage from Image
                pixmap = QtGui.QPixmap.fromImage(qimage)  # convert QtImage to QPixmap      
                print(pixmap)
                self.dialog.ui.label_2.setPixmap(pixmap)  
                self.dialog.ui.label_2.setScaledContents(True)
            else:
                self.dialog.ui.label_2.setText("Brak podglądu")
                 
        
class VariablesDialog(QDialog, variables_ui.Ui_Dialog):
    def __init__(self, loadedRecipe, gfiles, boxIsChecked, pathDirectory, bookName):
        super(VariablesDialog,  self).__init__()
        variables_ui.Ui_Dialog.setupUi(self,self)
      
        self.form=[]
        self.bookName = bookName
        self.attributes = {}  
        self.getFiles = gfiles
        self.saveDir = pathDirectory
        self.boxIsChecked = boxIsChecked
        self.loadedRecipe = loadedRecipe
        self.names_of_lists = recipe.Recipe(loadedRecipe).list
        self.names_of_texts = recipe.Recipe(loadedRecipe).text
        self.names_of_variables = recipe.Recipe(loadedRecipe).string
        self.template_name = recipe.Recipe(loadedRecipe).template  
        self.output_format = recipe.Recipe(loadedRecipe).outputFormat


        self.load_table_of_lists(self.names_of_lists)
        self.load_table_of_variables(self.names_of_variables)
        self.load_table_of_texts(self.names_of_texts)
        self.make_temp_template()
    #    self.load_name_of_book()

    def get_values(self):
        self.getsTable = []
        for box in self.form:
            items = (box.itemAt(i).widget() for i in range(box.count())) 
         
            for w in items:
                if isinstance (w, QtWidgets.QLabel):
                    self.getsTable = []
                    self.getsTable.append(w.text().encode('utf-8').decode('utf-8'))
                    key_value = True
            
                if isinstance (w, Table):
                    for i in range(w.rowCount()):
                        itm = w.item(i,0)
                        self.getsTable.append(itm.text().encode('utf-8').decode('utf-8'))

                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False
 
                if isinstance (w, QtWidgets.QLineEdit):
                    self.getsTable.append(w.text().encode('utf-8').decode('utf-8'))
                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

                if isinstance (w, QtWidgets.QPlainTextEdit):
                    self.getsTable.append(w.toPlainText().encode('utf-8').decode('utf-8')) 
                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False 

    # << Set elements on form >> #
    def drawInterface(self):
        for elem in self.form:
            self.form_layout.addRow(elem)

    def load_table_of_lists(self,names_of_lists):
        #for element in name_of_lists:
        for name_of_list in names_of_lists: 
            self.label= QtWidgets.QLabel(name_of_list)
            self.label.setMinimumWidth(100)
            self.label.setText(str(name_of_list))
            self.label.setObjectName(str(name_of_list) + "_label")

            self.table_widget = Table()
            self.table_widget.setHorizontalHeaderLabels([str(name_of_list)])
            self.table_widget.setObjectName(self.label.text() + "_table_widget")
        
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.table_widget)
                       
            self.b_box = QtWidgets.QHBoxLayout()
            self.b_box.addSpacing(108)
            self.b_box.addWidget(self.table_widget.button_form)
            self.b_box.addWidget(self.table_widget.button_form2)
            self.form.append(self.box)
            self.form.append(self.b_box)
          
            
        self.drawInterface()   

    def load_table_of_variables(self, names_of_variables): 
        for variable in names_of_variables: 
      
            self.label= QtWidgets.QLabel(variable)
            self.label.setMinimumWidth(100)
            self.label.setText(str(variable))
            self.label.setObjectName(self.label.text()+ "_label")
            self.line_edit= QtWidgets.QLineEdit("Wartość")     
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.line_edit)
            self.form.append(self.box)

        self.drawInterface()

    def load_table_of_texts(self, names_of_texts):
            
        for text in names_of_texts: 
            
            self.label= QtWidgets.QLabel(text)
            self.label.setText(str(text))
            self.label.setMinimumWidth(100)
            self.label.setMinimumHeight(100)
            self.label.setScaledContents(True)
            self.label.setObjectName(self.label.text()+ "_label")
            
            self.plain_text= QtWidgets.QPlainTextEdit("Wartość tekstowa")     

            # create layout vertical for label and list(at the moment still combobox)
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.plain_text)
            self.form.append(self.box)

            #self.form.append(self.combobox)

        self.drawInterface()   

    def make_temp_template(self):
        with ZipFile(self.loadedRecipe) as myzip:
            with myzip.open(*self.template_name) as myfile:
                print(str(myfile.read())) # for debugging
                
    def reject(self):
        self.form
        super(VariablesDialog, self).reject()
  
    def accept(self):

        variables = []
        outputFile = ""
        templateFile = ""

        self.get_values()   
        pandoc = pypandoc.get_pandoc_path()   

        if(self.boxIsChecked):
            inputFile = []
            for path in self.getFiles:
                inputFile.append(str(path))    #input file

            if(self.template_name): #template file
                templateFile+=' --template=' + str(self.template_name[0])
            for attr in self.attributes.keys(): 
                for e in self.attributes[attr]:    #variables skime ex.: -V authors = "Szymborska"
                    variables.append('-V')
                    variables.append(attr+ '=' + e)

            outputFile+='--output='+ self.saveDir+'/outputs/'+self.bookName+'.'+self.output_format[0]
                                
                #print([pandoc,inputFile,templateFile,variables,outputFile])
            
            if(templateFile!=""):
                #print([pandoc,inputFile,templateFile,*variables,outputFile])  # for debugging
                subprocess.run([pandoc,*inputFile,templateFile,*variables,outputFile])
                print("[*] Done -used temp file"+str(templateFile))  # for debugging
            else:
                    #print([pandoc,inputFile,*variables,outputFile])  # for debugging
                subprocess.run([pandoc,*inputFile,*variables,outputFile])
                print("[*] Done - use default template file ")  # for debugging
                
            
            inputFile = []
            templateFile = ""
            variables =[]
            outputFile=""
        else:
            num = 0
            inputFile =""
            for path in self.getFiles:
                num+=1
                inputFile=str(path)    #input file

                if(self.template_name): #template file
                    templateFile+=' --template=' + str(self.template_name[0])
                for attr in self.attributes.keys(): 
                    for e in self.attributes[attr]:    #variables skime ex.: -V authors = "Szymborska"
                        variables.append('-V')
                        variables.append(attr+ '=' + e)

                outputFile+='--output='+ self.saveDir+'/outputs/'+self.bookName+"_"+str(num)+'.'+self.output_format[0]
                                       
                if(templateFile!=""):
                    #print([pandoc,inputFile,templateFile,*variables,outputFile])  # for debugging
                    subprocess.run([pandoc,inputFile,templateFile,*variables,outputFile])
                    print("[*] Done -used temp file"+str(templateFile))  # for debugging
                else:
                    #print([pandoc,inputFile,*variables,outputFile])  # for debugging
                    subprocess.run([pandoc,inputFile,*variables,outputFile])
                    print("[*] Done - use default template file ")  # for debugging
                
                templateFile = ""
                variables =[]
                outputFile=""

        super(VariablesDialog, self).accept()


# <<< END of: CONFIG VARIABLES >>> #



      







