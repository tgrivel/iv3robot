Nieuw project gestart in Pycharm
Vervolens in settings/project interpreter gekozen voor new Virtual environment
om die venv_robot (naam zelf verzonnen) te starten in ../venv_robot/scripts 
de .bat activate gestart.
Nu moeten de belangrijke hulpprogs worden geinstalleerd op die venv.
In dit geval QT. dus  
pip install PyQt5==5.9.2
zie hiervoor ook https://build-system.fman.io/pyqt5-tutorial
om pycharm de diverse libs te laten herkennen, klik met rechts op de map
waar de venv in staat en kies voor Mark Directory As Source root
daarna Pycharm opnieuw starten en hij kan daadwerkeiljk de libs vinden

voor de test zijn dit de bestandsnamen, de urls komen uit de json lijst
all_hour.geojson
all_day.geojson