# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'pwmTest.ui'
#
# Created: Tue Nov  1 22:50:32 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!
 
from PyQt4 import QtCore, QtGui
 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
 
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 149)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "pyMCU - PWM Test", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 60, 351, 20))
        self.horizontalSlider.setMaximum(1023)
        self.horizontalSlider.setProperty("value", 500)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 97, 27))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 81, 21))
        self.label.setText(QtGui.QApplication.translate("Form", "PWM Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
 
    def retranslateUi(self, Form):
        pass
