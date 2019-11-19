import sys
from PySide import QtCore, QtGui
from ui1 import Ui_MainWindow
import sqlite3

conn = sqlite3.connect("datacoff.db")
cursor = conn.cursor()
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def pb():
    nametab = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
               'описание вкуса', 'цена', 'объем упаковки']
    sql = "SELECT * FROM Coffe WHERE ID=?"
    cursor.execute(sql, '1')
    tab = str(cursor.fetchall()[0])[1:-1]
    for i in range(len(tab.split(','))):
        ui.textEdit.append(nametab[i] + ' - ' + tab.split(',')[i])


ui.pushButton.clicked.connect(pb)
sys.exit(app.exec_())
