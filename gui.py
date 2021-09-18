import sys 
from PyQt5 import QtCore 
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton, QLineEdit, QLabel, QGridLayout,QHBoxLayout 
from get_aktie import get_aktie


class MyGui(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("GetAktie GUI mit GridLayout") 
        self.resize(600, 300)
        self.move(100,100)
        self.labelName = QLabel("Aktien WKN:", self)
        self.labelGetAktie = QLabel("Aktien Kurs:", self)
        self.textBoxName = QLineEdit(self) 
        self.textBoxName.setText("")
        self.textBoxGetAktie = QLineEdit(self) 
        self.textBoxGetAktie.setText("") 
        self.buttonGetAktie = QPushButton("Get Aktie", self) 
        self.buttonClear = QPushButton("Clear", self) 
        self.buttonQuit = QPushButton("Quit", self)
        self.buttonGetAktie.clicked.connect( self.onGetAktieClicked) 
        self.buttonClear.clicked.connect( self.onClearClicked) 
        self.buttonQuit.clicked.connect( self.onQuitClicked) 

        self.mainLayout = QGridLayout() 
        self.subLeftLayout = QHBoxLayout() 
        self.subRightLayout = QHBoxLayout() 
        self.subLeftLayout.addWidget(self.buttonGetAktie) 
        self.subLeftLayout.addWidget(self.buttonClear) 
        self.mainLayout.addWidget(self.labelName, 0, 0, QtCore.Qt.AlignRight) 
        self.mainLayout.addWidget(self.textBoxName, 0, 1) 
        self.mainLayout.addWidget(self.labelGetAktie, 1,0, QtCore.Qt.AlignRight) 
        self.mainLayout.addWidget(self.textBoxGetAktie, 1, 1) 
        self.mainLayout.addLayout(self.subLeftLayout, 2, 0) 
        self.subRightLayout.addStretch() 
        self.subRightLayout.addWidget(self.buttonQuit) 
        self.mainLayout.addLayout(self.subRightLayout, 2, 1) 
        self.setLayout(self.mainLayout) 
        self.show() 

    def onGetAktieClicked(self):
        aktien_name = self.textBoxName.text()
        aktien_kurs = get_aktie(aktien_name)
        aktien_kurs = str(aktien_kurs)
        self.textBoxGetAktie.setText(aktien_kurs) 

    def onClearClicked(self): 
        self.textBoxGetAktie.setText("") 
        self.textBoxName.setText("") 

    def onQuitClicked(self): 
        self.close() 
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myGui = MyGui() 
    app.exec_() 