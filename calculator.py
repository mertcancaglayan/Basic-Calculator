import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText('Sayı 1: ')
        self.lbl_num1.move(50,50)
        
        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150,50)
        self.txt_num1.resize(150,25)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText('Sayı 2: ')
        self.lbl_num2.move(50,80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150,80)
        self.txt_num2.resize(150,25)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapma)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkar')
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapma)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('Böl')
        self.btn_bol.move(150,210)
        self.btn_bol.clicked.connect(self.hesapma)


        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Çarp')
        self.btn_carp.move(150,250)
        self.btn_carp.clicked.connect(self.hesapma)


        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('Sonuç: ')
        self.lbl_sonuc.move(150,290)

    def hesapma(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Topla':
            result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == 'Çıkar':
            result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == 'Böl':
            result = int(self.txt_num1.text()) / int(self.txt_num2.text())
        elif sender == 'Çarp':
            result = int(self.txt_num1.text()) * int(self.txt_num2.text())

        self.lbl_sonuc.setText('Sonuç: '+ str(result)) 

    # def toplama(self):
    #     result = int(self.txt_num1.text()) + int(self.txt_num2.text())
    #     self.lbl_sonuc.setText('Sonuç: '+ str(result))

    # def cikarma(self):
    #     result = int(self.txt_num1.text()) - int(self.txt_num2.text())
    #     self.lbl_sonuc.setText('Sonuç: '+ str(result)) 

    # def bolme(self):
    #     result = int(self.txt_num1.text()) / int(self.txt_num2.text())
    #     self.lbl_sonuc.setText('Sonuç: '+ str(result))

    # def carpma(self):
    #     result = int(self.txt_num1.text()) * int(self.txt_num2.text())
    #     self.lbl_sonuc.setText('Sonuç: '+ str(result))


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()


