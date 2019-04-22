from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from pathlib import Path

import sys
import os
import json

data_lijst_met_urls = []

#Werkdirectory instellen (voor relatieve applicatie locatiereferenties)
werkdirectory = os.path.dirname(os.path.realpath(__file__))

class DataUrls(object):
    def __init__(self,ovlaag,nummer,naam,url):
        self.ovlaag = ovlaag
        self.nummer = nummer
        self.naam = naam
        self.url = url

class Startscherm(QMainWindow):
    def __init__(self):

        super(Startscherm, self).__init__()

        loadUi(werkdirectory + '\\UI\\' + 'Robot_main.ui', self)

        self.setWindowTitle('Asimov')
        self.show()

        #Knoppen instellen
        self.Btn_GetData.clicked.connect(self.VulText)
        self.Btn_Quit.clicked.connect(self.close)
        #uitklaplijsten vullen met info...
        # even iets wijzigen voor nieuwe push

    def VulText(self):
        pad_lijst_met_urls = geef_instelling('paden','lijst_met_urls')
        naam_lijst_met_urls = geef_instelling('bestandsnamen', 'lijst_met_urls')
        lijst_met_urls = os.path.join(pad_lijst_met_urls,naam_lijst_met_urls)
        self.VulDataLijstMetUrls(lijst_met_urls)
        self.VulTabel()

    def VulDataLijstMetUrls(self,naam_tabel):
        bronpad = naam_tabel
        with open(bronpad) as bron:
            data = json.load(bron)
            for row in data['data']:
                ovlaag = row['ovlaag']
                nummer = row['nummer']
                naam = row['naam']
                url = row['url']
                nieuw = DataUrls(ovlaag,nummer,naam,url)
                data_lijst_met_urls.append(nieuw)

    def VulTabel(self):
        # gebruiken van data uit de lijst met urls
        global data_lijst_met_urls
        print(len(data_lijst_met_urls))
        col_headers = ['ovlaag','ovnummer','naam','url']
        # rij_headers = [reg for reg in taakvelden if reg in selectie_regs]
        # selectie bevat nu alleen records van het gekozen taakveld.
        self.Overzicht_urls.setRowCount(len(data_lijst_met_urls))
        self.Overzicht_urls.setColumnCount(len(col_headers))
        self.Overzicht_urls.setHorizontalHeaderLabels(col_headers)
        # self.tabel_lasten.setVerticalHeaderLabels(rij_headers)
        rijnr = -1
        for rec in data_lijst_met_urls:
            rijnr +=1
            self.Overzicht_urls.setItem(rijnr,0, QTableWidgetItem(rec.ovlaag))
            self.Overzicht_urls.setItem(rijnr, 1, QTableWidgetItem(rec.nummer))
            self.Overzicht_urls.setItem(rijnr, 2, QTableWidgetItem(rec.naam))
            self.Overzicht_urls.setItem(rijnr, 3, QTableWidgetItem(rec.url))
        self.Overzicht_urls.resizeColumnsToContents()
        self.Overzicht_urls.verticalHeader().setDefaultSectionSize(20)

    def spreek(self):
        # functie als test of iets werkt
        print('ik spreek')


def geef_instelling(soort_instelling,naam_instelling):
    pad = Path(__file__).resolve().parents[1]
    newfile = os.path.join(pad , 'config.json')
    instellingen = json.load(open(newfile))
    data =  instellingen[soort_instelling]
    for rec in data:
        for key,val in rec.items():
            if key == naam_instelling:
                antwoord = val
    return antwoord


if __name__ == '__main__':
#     main()
    app = QApplication(sys.argv)
    window = Startscherm()
    sys.exit(app.exec_())