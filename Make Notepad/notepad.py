import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
form_class = uic.loadUiType("C:\\Users\\whanh\\재즐보프\\Make Notepad\\notepad.ui")[0]

class findWindow(QDialog):
    def __init__(self, parent):
        super(findWindow, self).__init__(parent)
        uic.loadUi("C:\\Users\\whanh\\재즐보프\\Make Notepad\\find.ui", self)
        self.show()


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFuntion)
        self.action_close.triggered.connect(self.close)

        self.action_undo.triggered.connect(self.undoFunction)
        self.action_cut.triggered.connect(self.cutFunction)
        self.action_copy.triggered.connect(self.copyFunction)
        self.action_paste.triggered.connect(self.pasteFunction)

        self.action_find.triggered.connect(self.findFunction)

        self.opened = False
        self.opened_file_path = '제목 없음'
    
    def ischanged(self):
        if not self.opened: 
            if self.plainTextEdit.toPlainText().strip(): # 열린적은 없는데 에디터 내용이 있으면
                return True
            return False
        
        # 현재 데이터
        current_data = self.plainTextEdit.toPlainText()
        
        # 파일에 저장된 데이터
        with open(fname, encoding='UTF8') as f:
            file_data = f.read()
        
        if current_data==file_data:# 열린적이 있고 변경사항이 없으면
            return False
        else:# 열린적이 있고 변경사항이 있으면 
            return True
        
    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {}에 저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton("저장", QMessageBox.YesRole) #0
        msgBox.addButton("저장 안 함", QMessageBox.NoRole) #1
        msgBox.addButton("취소", QMessageBox.RejectRole) #2
        ret = msgBox.exec_()
        
        if ret == 0:
            self.saveFunction()
        else:
            return ret

    def undoFunction(self):
        self.plainTextEdit.undo()

    def cutFunction(self):
        self.plainTextEdit.cut()

    def copyFunction(self):
        self.plainTextEdit.copy()
        
    def pasteFunction(self):
        self.plainTextEdit.paste()


    def closeEvent(self, event):
        if self.ischanged(): 
            ret = self.save_changed_data()

            if ret == 2:
                event.ignore()
        print("close test")
        # event.ignore()

    
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
        if self.ischanged(): 
            ret = self.save_changed_data()        

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
    
    def findFunction(self):
        findWindow(self)

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
