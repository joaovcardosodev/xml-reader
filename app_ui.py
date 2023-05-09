# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 556)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color:rgb(229, 245, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_excel = QPushButton(self.frame)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color:rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.btn_excel, 0, 5, 1, 1)

        self.btn_import = QPushButton(self.frame)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color:rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.btn_import, 0, 3, 1, 1)

        self.insert_path = QLineEdit(self.frame)
        self.insert_path.setObjectName(u"insert_path")
        self.insert_path.setFocusPolicy(Qt.StrongFocus)
        self.insert_path.setStyleSheet(u"QPushButton{\n"
"	color:rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.insert_path, 0, 1, 1, 1)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	color:rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.btn_open, 0, 2, 1, 1)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 0, 4, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.db_nfs = QTreeWidget(self.frame)
        self.db_nfs.setObjectName(u"db_nfs")
        sizePolicy.setHeightForWidth(self.db_nfs.sizePolicy().hasHeightForWidth())
        self.db_nfs.setSizePolicy(sizePolicy)
        self.db_nfs.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.db_nfs, 3, 0, 1, 2)

        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.title, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.insert_path.setText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtreewidgetitem = self.db_nfs.headerItem()
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("MainWindow", u"Valor ICMS ST", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Al\u00edquota ICMS ST", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor IPI", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Al\u00edquota IPI", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Valor ICMS", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Al\u00edquota ICMS", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Origem", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"NCM", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Fornecedor", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.title.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#000000;\">LEITOR DE XML</span></p></body></html>", None))
    # retranslateUi

