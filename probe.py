import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QLineEdit, QMessageBox, QCheckBox
from math_functions import *

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.label = QLabel("КОЛИЧЕСТВО СТРОК КОДА:" , self)
        self.label.setStyleSheet("QLabel { color : red; }")

        self.label.resize(200,20)
        self.label.move(10,10)
        self.label1 = QLabel("атрибуты продукта",self)
        self.label1.setStyleSheet("QLabel { color : green; }")
        self.label1.resize(200, 20)
        self.label1.move(10, 60)
        self.label1_1 = QLabel("1. НЕОБХОДИМОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ НАДЕЖНОСТЬ", self)
        self.label1_1.resize(450, 20)
        self.label1_1.move(10, 80)
        self.label1_2 = QLabel("2. РАЗМЕР БАЗЫ ДАННЫХ ПРИЛОЖЕНИЯ", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 120)
        self.label1_2 = QLabel("3. СЛОЖНОСТЬ ПРОДУКТА", self)
        self.label1_2.resize(400, 20)
        self.label1_2.move(10, 160)
        self.label1_2 = QLabel("Атрибуты персонала", self)
        self.label1_2.setStyleSheet("QLabel { color : green; }")
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


        self.textbox = QLineEdit(self)
        self.textbox.move(10, 40)
        self.textbox.resize(200, 20)
        self.onlyInt = QIntValidator()
        self.textbox.setValidator(self.onlyInt)

        combo1_1 = QComboBox(self)
        combo1_1.setObjectName("a1")
        combo1_1.addItem("Номинальный")
        combo1_1.addItem("очень низкий")
        combo1_1.addItem("низкий")
        combo1_1.addItem("высокий")
        combo1_1.addItem("очень высокий")
    
        combo1_2 =QComboBox(self)
        combo1_2.setObjectName("a2")
        combo1_2.addItem("Номинальный")
        combo1_2.addItem("очень низкий")
        combo1_2.addItem("низкий")
        combo1_2.addItem("высокий")
        combo1_2.addItem("очень высокий") 

        combo1_3 = QComboBox(self)
        combo1_3.setObjectName("a3")
        combo1_3.addItem("Номинальный")
        combo1_3.addItem("очень низкий")
        combo1_3.addItem("низкий")
        combo1_3.addItem("высокий")
        combo1_3.addItem("очень высокий")

        combo2_1 = QComboBox(self) 
        combo2_1.setObjectName("a4")
        combo2_1.addItem("Номинальный")
        combo2_1.addItem("очень низкий")
        combo2_1.addItem("низкий")
        combo2_1.addItem("высокий")
        combo2_1.addItem("очень высокий")

        combo2_2 = QComboBox(self) 
        combo2_2.setObjectName("a5")
        combo2_2.addItem("Номинальный")
        combo2_2.addItem("очень низкий")
        combo2_2.addItem("низкий")
        combo2_2.addItem("высокий")
        combo2_2.addItem("очень высокий")

        combo2_3 =QComboBox(self) 
        combo2_3.setObjectName("a6")
        combo2_3.addItem("Номинальный")
        combo2_3.addItem("очень низкий")
        combo2_3.addItem("низкий")
        combo2_3.addItem("высокий")
        combo2_3.addItem("очень высокий")

        combo2_4 =QComboBox(self) 
        combo2_4.setObjectName("a7")
        combo2_4.addItem("Номинальный")
        combo2_4.addItem("очень низкий")
        combo2_4.addItem("низкий")
        combo2_4.addItem("высокий")
        combo2_4.addItem("очень высокий")

        combo2_5 = QComboBox(self)
        combo2_5.setObjectName("a8")
        combo2_5.addItem("Номинальный")
        combo2_5.addItem("очень низкий")
        combo2_5.addItem("низкий")
        combo2_5.addItem("высокий")
        combo2_5.addItem("очень высокий")

        combo1_1.move(500, 80)
        combo1_1.resize(130,30)
        combo1_2.move(500, 120)
        combo1_2.resize(130,30)
        combo1_3.move(500, 160)
        combo1_3.resize(130,30)
        combo2_1.move(500, 240)
        combo2_1.resize(130,30)
        combo2_2.move(500, 280)
        combo2_2.resize(130,30)
        combo2_3.move(500, 320)
        combo2_3.resize(130,30)
        combo2_4.move(500, 360)
        combo2_4.resize(130,30)
        combo2_5.move(500, 400)
        combo2_5.resize(130,30)

        self.qlabel = QLabel(self)
        self.qlabel.move(500,450)
        
        
        combo1_1.activated[str].connect(self.onChanged)
        combo1_2.activated[str].connect(self.onChanged)
        combo1_3.activated[str].connect(self.onChanged)
        combo2_1.activated[str].connect(self.onChanged)
        combo2_2.activated[str].connect(self.onChanged)
        combo2_3.activated[str].connect(self.onChanged)
        combo2_4.activated[str].connect(self.onChanged)
        combo2_5.activated[str].connect(self.onChanged)



        self.setGeometry(80, 80, 700, 700)
        self.setWindowTitle("QLineEdit Example")
        self.show()
    def onChanged(self, text):
        print(self.focusWidget().objectName(), text)
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
