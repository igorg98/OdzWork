

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QMessageBox,QApplication, QPushButton, QRadioButton, QCheckBox)



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.SavBool = False
        self.SaveChk =0
        self.chkMin = QCheckBox('-', self)
        self.chkSave = QCheckBox('Save', self)
        self.s = 0
        self.lbl = QLabel(self)
        self.lblCheck = QLabel(self)
        self.txtNum = QLineEdit(self)
        self.btnAdd = QRadioButton('+',self)
        self.btnCon = QRadioButton('*', self)
        self.btnDiv = QRadioButton('/', self)
        btnReturn = QPushButton('Return', self)
        btnOk = QPushButton('Ok', self)
        btnEnd = QPushButton('Закончить ввод', self)
        self.btnAdd.setGeometry(170, 30, 50, 50)
        self.btnCon.setGeometry(170, 60, 50, 50)
        self.btnDiv.setGeometry(170, 90, 50, 50)
        btnOk.setGeometry(70, 80, 50, 20)
        self.chkMin.move(20, 50)
        self.chkSave.move(20, 100)
        btnReturn.setGeometry(20, 120, 70, 20)
        btnEnd.setGeometry(50, 180, 100, 30)
        self.txtNum.setGeometry(60,50,70,20)
        btnOk.clicked.connect(self.btnOkClicked)
        btnEnd.clicked.connect(self.btnEndClicked)
        btnReturn.clicked.connect(self.btnReturnClicked)
        self.txtNum.textChanged.connect(self.textChange)
        self.chkSave.toggled.connect(self.SaveVal)
        self.lbl.setText('Введите число')
        self.lbl.move(60,30)
        self.lblCheck.setGeometry(60, 100,100,100)
        self.setGeometry(300, 300, 250, 220)
        self.setWindowTitle('MyApp')
        self.txtNum.setText("0")
        self.btnAdd.toggle()
        self.lblCheck.setText(str(self.s))
        self.show()
    def textChange(self):
        if self.txtNum.text().isnumeric() == False:
            self.txtNum.setText("")
    def SaveVal(self):
        if self.chkSave.isChecked():
            self.SaveChk = self.s
            self.chkSave.setDisabled(True)
            self.s = 0
            self.txtNum.setText("0")
            self.lblCheck.setText(str(self.s))
    def btnOkClicked(self):
        OutDate = int(self.txtNum.text())
        if self.SavBool:
            OutDate = self.SaveChk
            self.txtNum.setEnabled(True)
            self.btnDiv.setEnabled(True)
            self.btnCon.setEnabled(True)
            self.SaveChk =0
            self.SavBool= False
        if self.chkMin.isChecked():
            OutDate = -OutDate
        if self.btnAdd.isChecked():
            self.s = self.s + OutDate
        elif self.btnCon.isChecked():
            self.s = self.s * OutDate
        elif self.btnDiv.isChecked():
            self.s = self.s // OutDate
        self.lblCheck.setText(str(self.s))

    def btnReturnClicked(self):
        self.chkSave.setChecked(False)
        self.chkSave.setEnabled(True)
        self.SavBool = True
        self.btnAdd.toggle()
        self.txtNum.setDisabled(True)
        self.btnDiv.setDisabled(True)
        self.btnCon.setDisabled(True)
    def btnEndClicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if self.s <= -32768 or self.s >= 32767:
             msg =QMessageBox.question(self, 'Переполнение', "Вы вышли за пределы 16й ОДЗ!",
                                               QMessageBox.Ok)
        else: msg1= QMessageBox.question(self, 'Все в порядке', "Ваш результат формулы подходит для 16й ОДЗ!",
                                               QMessageBox.Ok)
        self.s = 0
        self.lblCheck.setText(str(self.s))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())