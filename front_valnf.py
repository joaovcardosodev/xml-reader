from PySide2.QtWidgets import (QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem)
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from ui_app import Ui_MainWindow
from xml_import import (read_xml)
import sys
from bd import DataBase
import sqlite3
import pandas as pd


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Leitor de XML")
        appIcon = QIcon('img/icon.png')
        self.setWindowIcon(appIcon)

        self.btn_open.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)
        self.btn_excel.clicked.connect(self.excel)
        self.table_notas()

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str("Open Directory"),
                                                          "/home",
                                                          QFileDialog.ShowDirsOnly
                                       
                                                          | QFileDialog.DontResolveSymlinks)
        self.insert_path.setText(self.path)
   
    def import_xml_files(self):
        xml = read_xml(self.insert_path.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.conecta()
        c = 1 

        for i in all:
            self.progressBar.setValue(c)
            fullDataSet = xml.nf_data(i)
            db.insert_data(fullDataSet)
            c+=1
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("importação concluída!")
        msg.exec_()
        self.progressBar.setValue(0)

    def table_notas(self):
        self.db_nfs
        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM NOTAS", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.db_nfs, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.db_nfs.setSortingEnabled(True)

        for i in range(1,15):
            self.db_nfs.resizeColumnToContents(i)

    def excel(self):
        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM NOTAS", cn)
        result.to_excel("Base Notas.xlsx", sheet_name='Base', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Base Notas")
        msg.setText("Relatório gerado!")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_() 
