from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys
import os
import json


#Werkdirectory instellen (voor relatieve applicatie locatiereferenties)
werkdirectory = os.path.dirname(os.path.realpath(__file__))

class Startscherm(QMainWindow):
    def __init__(self):

        super(Startscherm, self).__init__()

        loadUi(werkdirectory + '\\UI\\' + 'QuakeMain.ui', self)
        self.setWindowTitle('Shakes from Mother Earth')
        self.show()

        #Knoppen instellen
        self.Btn_GetData.clicked.connect(self.VulText)
        self.Btn_Quit.clicked.connect(self.close)
        self.cbo_KiesBestand.currentIndexChanged.connect(self.cbo_kiesbestand_is_gewijzigd)
        self.cbo_Country.currentIndexChanged.connect(self.cbo_Country_is_gewijzigd)
        #uitklaplijsten vullen met info...

    def spreek(self):
        # functie als test of iets werkt
        print('ik spreek')


if __name__ == '__main__':
#     main()
    app = QApplication(sys.argv)
    window = Startscherm()
    sys.exit(app.exec_())