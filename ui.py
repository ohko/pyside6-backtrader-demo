# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 659)
        self.actiona = QAction(MainWindow)
        self.actiona.setObjectName(u"actiona")
        self.actionb = QAction(MainWindow)
        self.actionb.setObjectName(u"actionb")
        self.actionc = QAction(MainWindow)
        self.actionc.setObjectName(u"actionc")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listStrategy = QListWidget(self.centralwidget)
        QListWidgetItem(self.listStrategy)
        QListWidgetItem(self.listStrategy)
        self.listStrategy.setObjectName(u"listStrategy")
        self.listStrategy.setGeometry(QRect(12, 12, 231, 611))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listStrategy.sizePolicy().hasHeightForWidth())
        self.listStrategy.setSizePolicy(sizePolicy)
        self.textName = QLineEdit(self.centralwidget)
        self.textName.setObjectName(u"textName")
        self.textName.setGeometry(QRect(330, 13, 461, 21))
        self.textContent = QTextEdit(self.centralwidget)
        self.textContent.setObjectName(u"textContent")
        self.textContent.setGeometry(QRect(330, 41, 461, 201))
        self.btnNew = QPushButton(self.centralwidget)
        self.btnNew.setObjectName(u"btnNew")
        self.btnNew.setGeometry(QRect(250, 10, 57, 35))
        self.btnRemove = QPushButton(self.centralwidget)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setGeometry(QRect(250, 40, 57, 35))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 80, 57, 35))
        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(260, 210, 57, 35))
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(260, 250, 57, 35))
        self.btnQuit = QPushButton(self.centralwidget)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setGeometry(QRect(250, 580, 57, 35))
        self.btnQuit.setAutoDefault(False)
        self.btnQuit.setFlat(False)
        self.textLog = QTextEdit(self.centralwidget)
        self.textLog.setObjectName(u"textLog")
        self.textLog.setGeometry(QRect(330, 250, 461, 371))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuabc = QMenu(self.menubar)
        self.menuabc.setObjectName(u"menuabc")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuabc.menuAction())
        self.menuabc.addAction(self.actiona)
        self.menuabc.addAction(self.actionb)
        self.menuabc.addSeparator()
        self.menuabc.addAction(self.actionc)

        self.retranslateUi(MainWindow)
        self.listStrategy.currentItemChanged.connect(MainWindow.listStrategyItemChange)
        self.pushButton.clicked.connect(MainWindow.btnRefreshClicked)
        self.btnQuit.clicked.connect(MainWindow.quit)
        self.btnRemove.clicked.connect(MainWindow.btnRemoveClicked)
        self.btnSave.clicked.connect(MainWindow.btnSaveClicked)
        self.btnRun.clicked.connect(MainWindow.btnRunClicked)
        self.btnNew.clicked.connect(MainWindow.btnNewClicked)

        self.btnQuit.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiona.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.actionb.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.actionc.setText(QCoreApplication.translate("MainWindow", u"c", None))

        __sortingEnabled = self.listStrategy.isSortingEnabled()
        self.listStrategy.setSortingEnabled(False)
        ___qlistwidgetitem = self.listStrategy.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1111", u"1"));
        ___qlistwidgetitem1 = self.listStrategy.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2222", None));
        self.listStrategy.setSortingEnabled(__sortingEnabled)

        self.btnNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuabc.setTitle(QCoreApplication.translate("MainWindow", u"abc", None))
    # retranslateUi

