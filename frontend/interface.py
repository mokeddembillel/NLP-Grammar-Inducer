# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName("shadow_layout")
        self.shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.shadow_frame.setStyleSheet("border-radius: 10px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 62, 81, 255), stop:1 rgba(7, 34, 56, 255));")
        self.shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shadow_frame.setObjectName("shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color:none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        font = QtGui.QFont()
        font.setFamily("MT Extra")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(22, 210, 152)")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(227, 229, 79);\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: rgba(227, 229, 79,150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(17, 17))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(110, 214, 113);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgba(110, 214, 113,150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(235, 78, 78);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgba(235, 78, 78,150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.shadow_frame)
        self.content_bar.setStyleSheet("background-color:none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.content_bar)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.side_bar = QtWidgets.QFrame(self.content_bar)
        self.side_bar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.side_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.side_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar.setObjectName("side_bar")
        self.formLayout = QtWidgets.QFormLayout(self.side_bar)
        self.formLayout.setContentsMargins(10, 50, 10, 0)
        self.formLayout.setObjectName("formLayout")
        self.btn_training = QtWidgets.QPushButton(self.side_bar)
        self.btn_training.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_training.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_training.setFont(font)
        self.btn_training.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_training.setStyleSheet("QPushButton {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}\n"
"")
        self.btn_training.setObjectName("btn_training")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_training)
        self.btn_inference = QtWidgets.QPushButton(self.side_bar)
        self.btn_inference.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_inference.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_inference.setFont(font)
        self.btn_inference.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_inference.setStyleSheet("QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"")
        self.btn_inference.setObjectName("btn_inference")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.btn_inference)
        self.horizontalLayout_6.addWidget(self.side_bar)
        self.conent_training = QtWidgets.QFrame(self.content_bar)
        self.conent_training.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conent_training.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conent_training.setObjectName("conent_training")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.conent_training)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.conent_training)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.training = QtWidgets.QWidget()
        self.training.setStyleSheet("background-color: none;")
        self.training.setObjectName("training")
        self.label_2 = QtWidgets.QLabel(self.training)
        self.label_2.setGeometry(QtCore.QRect(280, 145, 341, 141))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.training)
        self.inference = QtWidgets.QWidget()
        self.inference.setStyleSheet("background-color: none;")
        self.inference.setObjectName("inference")
        self.label = QtWidgets.QLabel(self.inference)
        self.label.setGeometry(QtCore.QRect(300, 145, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.inference)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.horizontalLayout_6.addWidget(self.conent_training)
        self.verticalLayout.addWidget(self.content_bar)
        self.credits_bar = QtWidgets.QFrame(self.shadow_frame)
        self.credits_bar.setMinimumSize(QtCore.QSize(0, 30))
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setStyleSheet("background-color:none;")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_5.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_credits = QtWidgets.QLabel(self.frame_label_credits)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(9)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(150,150,150);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_5.addWidget(self.label_credits)
        self.horizontalLayout_4.addWidget(self.frame_label_credits)
        self.frame_grip = QtWidgets.QFrame(self.credits_bar)
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding:5px")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_4.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.credits_bar)
        self.shadow_layout.addWidget(self.shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Automatic Grammar Inducer"))
        self.btn_training.setText(_translate("MainWindow", "Training"))
        self.btn_inference.setText(_translate("MainWindow", "Inference"))
        self.label_2.setText(_translate("MainWindow", "Page 2"))
        self.label.setText(_translate("MainWindow", "Page 1"))
        self.label_credits.setText(_translate("MainWindow", "By: Billel Mokeddem and Ryad Boudrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
