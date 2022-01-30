import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\whanh\\pyqt tutorial\\5. Notepad-SaveAs\\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFuntion)

        self.opened = False
        self.opened_file_path = ''
    
    def save_file(self, fname):
        data = self.plainTextEdit.toPlainText()

        with open(fname, 'w', encoding='UTF8') as f:
            data = f.write(data)
        
        self.opened = True
        self.opened_file_path = fname

        print("save {}!!".format(fname))
        

    def open_file(self, fname):
        with open(fname, encoding='UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)

        self.opened = True
        self.opened_file_path = fname

        print("open {}!!".format(fname))

    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.open_file(fname[0])

    def saveFunction(self):
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            self.saveAsFuntion()

    def saveAsFuntion(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            self.save_file(fname[0]) 
        
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
