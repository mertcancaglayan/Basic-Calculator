from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_topla.clicked.connect(self.hesapma)
        self.ui.btn_cikar.clicked.connect(self.hesapma)
        self.ui.btn_carp.clicked.connect(self.hesapma)
        self.ui.btn_bol.clicked.connect(self.hesapma)

    def hesapma(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Topla':
            result = int(self.ui.txt_num1.text()) + int(self.ui.txt_num2.text())
        elif sender == 'Çıkar':
            result = int(self.ui.txt_num1.text()) - int(self.ui.txt_num2.text())
        elif sender == 'Böl':
            result = int(self.ui.txt_num1.text()) / int(self.ui.txt_num2.text())
        elif sender == 'Çarp':
            result = int(self.ui.txt_num1.text()) * int(self.ui.txt_num2.text())

        self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()
