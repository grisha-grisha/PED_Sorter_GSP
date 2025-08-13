# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PED_design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1340, 808)
        MainWindow.setMinimumSize(QSize(1250, 710))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1321, 751))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 20, 761, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.DirectoryName = QLabel(self.frame_2)
        self.DirectoryName.setObjectName(u"DirectoryName")
        self.DirectoryName.setGeometry(QRect(160, 40, 591, 31))
        font = QFont()
        font.setBold(True)
        self.DirectoryName.setFont(font)
        self.DirectoryName.setWordWrap(False)
        self.DirectoryName.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.ChoosePEDButton = QPushButton(self.frame_2)
        self.ChoosePEDButton.setObjectName(u"ChoosePEDButton")
        self.ChoosePEDButton.setGeometry(QRect(10, 10, 91, 31))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 40, 141, 31))
        self.files_frame = QFrame(self.frame)
        self.files_frame.setObjectName(u"files_frame")
        self.files_frame.setEnabled(True)
        self.files_frame.setGeometry(QRect(20, 100, 1291, 641))
        self.files_frame.setFrameShape(QFrame.StyledPanel)
        self.files_frame.setFrameShadow(QFrame.Plain)
        self.files_frame.setLineWidth(3)
        self.files_frame.setMidLineWidth(3)
        self.label_8 = QLabel(self.files_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 261, 21))
        self.label_9 = QLabel(self.files_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 10, 141, 21))
        self.Table = QTableWidget(self.files_frame)
        if (self.Table.columnCount() < 5):
            self.Table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(199, 199, 199));
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(199, 199, 199));
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        __qtablewidgetitem3.setBackground(QColor(199, 199, 199));
        self.Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Table.setObjectName(u"Table")
        self.Table.setGeometry(QRect(290, 40, 991, 591))
        self.Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Table.setAlternatingRowColors(True)
        self.Table.horizontalHeader().setDefaultSectionSize(180)
        self.FilesList = QListWidget(self.files_frame)
        QListWidgetItem(self.FilesList)
        self.FilesList.setObjectName(u"FilesList")
        self.FilesList.setGeometry(QRect(10, 40, 271, 551))
        self.SearchButton_2 = QPushButton(self.files_frame)
        self.SearchButton_2.setObjectName(u"SearchButton_2")
        self.SearchButton_2.setEnabled(False)
        self.SearchButton_2.setGeometry(QRect(190, 600, 91, 31))
        self.SearchButton = QPushButton(self.files_frame)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setEnabled(False)
        self.SearchButton.setGeometry(QRect(90, 600, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1340, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a \u043f\u0430\u043a\u0435\u0442\u043e\u0432 \u0441\u043c\u0435\u0442\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438", None))
        self.DirectoryName.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ChoosePEDButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u041f\u0421\u0414", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u0434\u0438\u0440\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0444\u0430\u0439\u043b\u043e\u0432 \u043f\u0430\u043a\u0435\u0442\u0430 \u0441\u043c\u0435\u0442\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b:", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f (\u0434\u0432\u043e\u0439\u043d\u043e\u0435 \u043d\u0430\u0436\u0430\u0442\u0438\u0435 - \u043e\u0442\u043a\u0440\u044b\u0442\u044c)", None));
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u043c\u044b\u0439 \u0442\u0438\u043f", None));
        ___qtablewidgetitem2 = self.Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u043a\u0430", None));
        ___qtablewidgetitem3 = self.Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0435 \u0438\u043c\u044f", None));
        ___qtablewidgetitem4 = self.Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c?", None));

        __sortingEnabled = self.FilesList.isSortingEnabled()
        self.FilesList.setSortingEnabled(False)
        ___qlistwidgetitem = self.FilesList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"...", None));
        self.FilesList.setSortingEnabled(__sortingEnabled)

        self.SearchButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043a\u0430\u0442\u044c", None))
    # retranslateUi

