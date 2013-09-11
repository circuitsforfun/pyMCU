#!/usr/bin/env python
 
# Requires pwmForm.py for QT Gui form

import sys
from PyQt4 import QtCore, QtGui   # Import pyqt
from pwmForm import Ui_Form       # Import our cutstom pwmForm
import pymcu                      # Import pymcu
 
mb = pymcu.mcuModule()  # Find and initialize first found pymcu board.
mb.pwmOn(1)             # Turn on PWM1
 
 
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.quit )
        QtCore.QObject.connect(self.ui.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"), self.pwmUpdate)
 
    def pwmUpdate(self):
        mb.pwmDuty(1, self.ui.horizontalSlider.value())
 
    def quit(self):
        sys.exit(0)
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
