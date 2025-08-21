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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 820)
        MainWindow.setMinimumSize(QSize(1500, 820))
        MainWindow.setMaximumSize(QSize(1500, 820))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1501, 781))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 10, 721, 81))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.DirectoryName = QLabel(self.frame_2)
        self.DirectoryName.setObjectName(u"DirectoryName")
        self.DirectoryName.setGeometry(QRect(150, 40, 481, 31))
        font = QFont()
        font.setBold(True)
        self.DirectoryName.setFont(font)
        self.DirectoryName.setWordWrap(False)
        self.DirectoryName.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.ChoosePEDButton = QPushButton(self.frame_2)
        self.ChoosePEDButton.setObjectName(u"ChoosePEDButton")
        self.ChoosePEDButton.setGeometry(QRect(10, 10, 81, 31))
        self.ChoosePEDButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 40, 141, 31))
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(630, 10, 81, 31))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.files_frame = QFrame(self.frame)
        self.files_frame.setObjectName(u"files_frame")
        self.files_frame.setEnabled(True)
        self.files_frame.setGeometry(QRect(20, 100, 1461, 671))
        self.files_frame.setFrameShape(QFrame.StyledPanel)
        self.files_frame.setFrameShadow(QFrame.Plain)
        self.files_frame.setLineWidth(3)
        self.files_frame.setMidLineWidth(3)
        self.label_8 = QLabel(self.files_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 291, 16))
        self.label_9 = QLabel(self.files_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 10, 141, 21))
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
        self.Table.setGeometry(QRect(320, 50, 1131, 611))
        self.Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Table.setAlternatingRowColors(True)
        self.Table.horizontalHeader().setDefaultSectionSize(180)
        self.FilesList = QListWidget(self.files_frame)
        QListWidgetItem(self.FilesList)
        self.FilesList.setObjectName(u"FilesList")
        self.FilesList.setGeometry(QRect(10, 50, 301, 611))
        self.FilesList.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_10 = QLabel(self.files_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 30, 291, 16))
        self.loading_label = QLabel(self.files_frame)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setGeometry(QRect(460, 10, 221, 21))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.loading_label.setFont(font1)
        self.loading_label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(760, 10, 721, 81))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.SearchButton_2 = QPushButton(self.frame_3)
        self.SearchButton_2.setObjectName(u"SearchButton_2")
        self.SearchButton_2.setEnabled(False)
        self.SearchButton_2.setGeometry(QRect(410, 10, 91, 31))
        self.SearchButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SearchButton = QPushButton(self.frame_3)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setEnabled(False)
        self.SearchButton.setGeometry(QRect(10, 10, 81, 31))
        self.SearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_in_name_checkBox = QCheckBox(self.frame_3)
        self.search_in_name_checkBox.setObjectName(u"search_in_name_checkBox")
        self.search_in_name_checkBox.setGeometry(QRect(100, 10, 261, 17))
        self.search_in_name_checkBox.setChecked(True)
        self.search_in_file_checkBox = QCheckBox(self.frame_3)
        self.search_in_file_checkBox.setObjectName(u"search_in_file_checkBox")
        self.search_in_file_checkBox.setGeometry(QRect(100, 30, 261, 17))
        self.search_in_file_checkBox.setChecked(True)
        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(360, 10, 3, 61))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.rename_radioButton = QRadioButton(self.frame_3)
        self.rename_radioButton.setObjectName(u"rename_radioButton")
        self.rename_radioButton.setGeometry(QRect(510, 10, 201, 17))
        self.rename_radioButton.setChecked(False)
        self.rename_radioButton_2 = QRadioButton(self.frame_3)
        self.rename_radioButton_2.setObjectName(u"rename_radioButton_2")
        self.rename_radioButton_2.setGeometry(QRect(510, 30, 201, 17))
        self.rename_radioButton_2.setChecked(True)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 50, 81, 23))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 21))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
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

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"(\u0434\u0432\u043e\u0439\u043d\u043e\u0439 \u043a\u043b\u0438\u043a \u0434\u043b\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0442\u044d\u0433\u043e\u0432)", None))
        self.loading_label.setText("")
        self.SearchButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043a\u0430\u0442\u044c", None))
        self.search_in_name_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0438\u0441\u043a\u0430\u0442\u044c \u043f\u043e \u0442\u044d\u0433\u0430\u043c \u0432 \u0438\u043c\u0435\u043d\u0438 \u0444\u0430\u0439\u043b\u0430", None))
        self.search_in_file_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0438\u0441\u043a\u0430\u0442\u044c \u043f\u043e \u0442\u044d\u0433\u0430\u043c \u0432 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u043c \u0444\u0430\u0439\u043b\u0430", None))
        self.rename_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c \u044d\u0442\u0438 \u0444\u0430\u0439\u043b\u044b", None))
        self.rename_radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u043f\u0438\u0438 \u0441 \u043d\u043e\u0432\u044b\u043c \u0438\u043c\u0435\u043d\u0435\u043c", None))
    # retranslateUi

