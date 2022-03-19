import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QLineEdit, QMessageBox, QCheckBox



class Example(QMainWindow):

    data = {'VL':['очень низкий'],
        'L':['низкий'],
        'N':['Номинальный'],
        'H':['высокий'],
        'VH':['очень высоко']}

    def __init__(self):
        super().__init__()
        #labels
        self.label = QLabel("КОЛИЧЕСТВО СТРОК КОДА:" , self)
        self.label.resize(200,20)
        self.label.move(10,10)
        self.label1 = QLabel("атрибуты продукта",self)
        self.label1.resize(200, 20)
        self.label1.move(10, 60)
        self.label1_1 = QLabel("1. НЕОБХОДИМОЕ_ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ_НАДЕЖНОСТЬ", self)
        self.label1_1.resize(400, 20)
        self.label1_1.move(10, 80)
        self.label1_2 = QLabel("2. РАЗМЕР БАЗЫ ДАННЫХ ПРИЛОЖЕНИЯ", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 120)
        self.label1_2 = QLabel("3. СЛОЖНОСТЬ ПРОДУКТА", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 160)
        self.label1_2 = QLabel("Атрибуты персонала", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 200)
        self.label1_2 = QLabel("1. ВОЗМОЖНОСТИ АНАЛИТИКА", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 240)
        self.label1_2 = QLabel("2. ПРИЛОЖЕНИЯ ОПЫТ", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 280)
        self.label1_2 = QLabel("3. ВОЗМОЖНОСТИ ПРОГРАММНОГО ИНЖЕНЕРА", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 320)
        self.label1_2 = QLabel("4. ОПЫТ РАБОТЫ С ВИРТУАЛЬНОЙ МАШИНОЙ", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 360)
        self.label1_2 = QLabel("5. ОПЫТ ЯЗЫКА ПРОГРАММИРОВАНИЯ", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 400)


        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 40)
        self.textbox.resize(200, 20)
        self.onlyInt = QIntValidator()
        self.textbox.setValidator(self.onlyInt)
        #create checkout box 1
        self.c = QCheckBox("VL", self)
        self.c.move(10, 90)
        self.c.resize(320, 40)
        self.c.connect(self.clickBox)
        self.c = QCheckBox("L", self)
        self.c.move(50, 90)
        self.c.resize(320, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 90)
        self.c.resize(320, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 90)
        self.c.resize(320, 40)
        #create checkout 2
        self.c = QCheckBox("VL", self)
        self.c.move(10, 130)
        self.c.resize(320, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 130)
        self.c.resize(320, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 130)
        self.c.resize(320, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 130)
        self.c.resize(320, 40)
        #labels checkout 3
        self.c = QCheckBox("VL", self)
        self.c.move(10, 170)
        self.c.resize(320, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 170)
        self.c.resize(320, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 170)
        self.c.resize(320, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 170)
        self.c.resize(320, 40)
    #checkout 2.1
        self.c = QCheckBox("VL", self)
        self.c.move(10, 250)
        self.c.resize(360, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 250)
        self.c.resize(360, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 250)
        self.c.resize(360, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 250)
        self.c.resize(360, 40)
        #labels 2.2
        self.c = QCheckBox("VL", self)
        self.c.move(10, 290)
        self.c.resize(360, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 290)
        self.c.resize(360, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 290)
        self.c.resize(360, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 290)
        self.c.resize(360, 40)
        self.setGeometry(80, 80, 500, 500)
        #check 2.3
        self.c = QCheckBox("VL", self)
        self.c.move(10, 330)
        self.c.resize(360, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 330)
        self.c.resize(360, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 330)
        self.c.resize(360, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 330)
        self.c.resize(360, 40)
        #chek0 2.4
        self.c = QCheckBox("VL", self)
        self.c.move(10, 370)
        self.c.resize(360, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 370)
        self.c.resize(360, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 370)
        self.c.resize(360, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 370)
        self.c.resize(360, 40)
        self.setGeometry(80, 80, 500, 500)
        self.setGeometry(80, 80, 500, 500)
        #label 2.5
        self.c = QCheckBox("VL", self)
        self.c.move(10, 410)
        self.c.resize(360, 40)
        self.c = QCheckBox("L", self)
        self.c.move(50, 410)
        self.c.resize(360, 40)
        self.c = QCheckBox("N", self)
        self.c.move(90, 410)
        self.c.resize(360, 40)
        self.c = QCheckBox("VH", self)
        self.c.move(130, 410)
        self.c.resize(360, 40)
        button = QPushButton('submit', self)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)
        button.move(200, 450)
        self.setGeometry(80, 80, 500, 500)
        #self.setWindowTitle("QLineEdit Example")
        self.show()

    @pyqtSlot()
    def on_click(self):
        print(self.textbox.text())
        
    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())