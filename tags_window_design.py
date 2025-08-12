# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tags_window_design.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_TagsWindow(object):
    def setupUi(self, TagsWindow):
        if not TagsWindow.objectName():
            TagsWindow.setObjectName(u"TagsWindow")
        TagsWindow.resize(280, 250)
        TagsWindow.setMinimumSize(QSize(280, 250))
        TagsWindow.setMaximumSize(QSize(280, 250))
        self.frame = QFrame(TagsWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 261, 241))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 210, 181, 20))
        self.TagList = QListWidget(self.frame)
        self.TagList.setObjectName(u"TagList")
        self.TagList.setGeometry(QRect(0, 50, 251, 121))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 101, 16))
        self.add_tag = QPushButton(self.frame)
        self.add_tag.setObjectName(u"add_tag")
        self.add_tag.setGeometry(QRect(190, 210, 61, 23))
        self.delete_tag = QPushButton(self.frame)
        self.delete_tag.setObjectName(u"delete_tag")
        self.delete_tag.setGeometry(QRect(190, 180, 61, 23))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 30, 241, 16))
        self.type_label = QLabel(self.frame)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setGeometry(QRect(110, 10, 141, 16))

        self.retranslateUi(TagsWindow)

        QMetaObject.connectSlotsByName(TagsWindow)
    # setupUi

    def retranslateUi(self, TagsWindow):
        TagsWindow.setWindowTitle(QCoreApplication.translate("TagsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0442\u0435\u0433\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("TagsWindow", u"\u041f\u043e\u0438\u0441\u043a \u0444\u0430\u0439\u043b\u043e\u0432 \u0442\u0438\u043f\u0430", None))
        self.add_tag.setText(QCoreApplication.translate("TagsWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_tag.setText(QCoreApplication.translate("TagsWindow", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("TagsWindow", u"\u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u0442\u0441\u044f \u043f\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u0442\u0435\u0433\u0430\u043c \u0432 \u0438\u043c\u0435\u043d\u0438:", None))
        self.type_label.setText(QCoreApplication.translate("TagsWindow", u"...", None))
    # retranslateUi

