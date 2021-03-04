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
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(110, 214, 113);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgba(110, 214, 113,150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(17, 17))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(235, 78, 78);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgba(235, 78, 78,150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
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
        self.formLayout.setContentsMargins(20, 50, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(20)
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
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"")
        self.btn_inference.setObjectName("btn_inference")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.btn_inference)
        self.horizontalLayout_6.addWidget(self.side_bar)
        self.main_content = QtWidgets.QFrame(self.content_bar)
        self.main_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_content.setObjectName("main_content")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.main_content)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_content)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.training = QtWidgets.QWidget()
        self.training.setStyleSheet("background-color: none;")
        self.training.setObjectName("training")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.training)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.training_content = QtWidgets.QFrame(self.training)
        self.training_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_content.setObjectName("training_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.training_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.corpus_frame = QtWidgets.QFrame(self.training_content)
        self.corpus_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.corpus_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.corpus_frame.setObjectName("corpus_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.corpus_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.corpus_text = QtWidgets.QPlainTextEdit(self.corpus_frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.corpus_text.setFont(font)
        self.corpus_text.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}")
        self.corpus_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.corpus_text.setObjectName("corpus_text")
        self.verticalLayout_4.addWidget(self.corpus_text)
        self.verticalLayout_3.addWidget(self.corpus_frame)
        self.training_btns = QtWidgets.QFrame(self.training_content)
        self.training_btns.setMaximumSize(QtCore.QSize(16777215, 70))
        self.training_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_btns.setObjectName("training_btns")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.training_btns)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_load = QtWidgets.QPushButton(self.training_btns)
        self.btn_load.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_load.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_load.setFont(font)
        self.btn_load.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_load.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}")
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout_8.addWidget(self.btn_load)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.btn_train = QtWidgets.QPushButton(self.training_btns)
        self.btn_train.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_train.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_train.setFont(font)
        self.btn_train.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_train.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}")
        self.btn_train.setObjectName("btn_train")
        self.horizontalLayout_8.addWidget(self.btn_train)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.btn_save = QtWidgets.QPushButton(self.training_btns)
        self.btn_save.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_save.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_8.addWidget(self.btn_save)
        self.verticalLayout_3.addWidget(self.training_btns)
        self.verticalLayout_2.addWidget(self.training_content)
        self.stackedWidget.addWidget(self.training)
        self.inference = QtWidgets.QWidget()
        self.inference.setStyleSheet("background-color: none;")
        self.inference.setObjectName("inference")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.inference)
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.inference_content = QtWidgets.QFrame(self.inference)
        self.inference_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inference_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inference_content.setObjectName("inference_content")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.inference_content)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.corpus_test_frame = QtWidgets.QFrame(self.inference_content)
        self.corpus_test_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.corpus_test_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.corpus_test_frame.setObjectName("corpus_test_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.corpus_test_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.corpus_text_2 = QtWidgets.QPlainTextEdit(self.corpus_test_frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.corpus_text_2.setFont(font)
        self.corpus_text_2.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}")
        self.corpus_text_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.corpus_text_2.setObjectName("corpus_text_2")
        self.verticalLayout_7.addWidget(self.corpus_text_2)
        self.verticalLayout_6.addWidget(self.corpus_test_frame)
        self.training_btns_2 = QtWidgets.QFrame(self.inference_content)
        self.training_btns_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.training_btns_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_btns_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_btns_2.setObjectName("training_btns_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.training_btns_2)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_load_2 = QtWidgets.QPushButton(self.training_btns_2)
        self.btn_load_2.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_load_2.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_load_2.setFont(font)
        self.btn_load_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_load_2.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}")
        self.btn_load_2.setObjectName("btn_load_2")
        self.horizontalLayout_9.addWidget(self.btn_load_2)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.btn_train_2 = QtWidgets.QPushButton(self.training_btns_2)
        self.btn_train_2.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_train_2.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_train_2.setFont(font)
        self.btn_train_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_train_2.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}")
        self.btn_train_2.setObjectName("btn_train_2")
        self.horizontalLayout_9.addWidget(self.btn_train_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.btn_save_2 = QtWidgets.QPushButton(self.training_btns_2)
        self.btn_save_2.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_save_2.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.btn_save_2.setFont(font)
        self.btn_save_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save_2.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n"
"}")
        self.btn_save_2.setObjectName("btn_save_2")
        self.horizontalLayout_9.addWidget(self.btn_save_2)
        self.verticalLayout_6.addWidget(self.training_btns_2)
        self.verticalLayout_5.addWidget(self.inference_content)
        self.stackedWidget.addWidget(self.inference)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.horizontalLayout_6.addWidget(self.main_content)
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
        self.corpus_text.setPlainText(_translate("MainWindow", "Training"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.btn_train.setText(_translate("MainWindow", "Train"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.corpus_text_2.setPlainText(_translate("MainWindow", "Inference"))
        self.btn_load_2.setText(_translate("MainWindow", "Load"))
        self.btn_train_2.setText(_translate("MainWindow", "Train"))
        self.btn_save_2.setText(_translate("MainWindow", "Save"))
        self.label_credits.setText(_translate("MainWindow", "By: Billel Mokeddem and Ryad Boudrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
