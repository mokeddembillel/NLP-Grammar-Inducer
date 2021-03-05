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
        MainWindow.resize(1030, 671)
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
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
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
        self.training_group_1 = QtWidgets.QFrame(self.training_content)
        self.training_group_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_group_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_group_1.setObjectName("training_group_1")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.training_group_1)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.training_corpus_frame = QtWidgets.QFrame(self.training_group_1)
        self.training_corpus_frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_corpus_frame.sizePolicy().hasHeightForWidth())
        self.training_corpus_frame.setSizePolicy(sizePolicy)
        self.training_corpus_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.training_corpus_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_corpus_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_corpus_frame.setObjectName("training_corpus_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.training_corpus_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.training_corpus = QtWidgets.QPlainTextEdit(self.training_corpus_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_corpus.sizePolicy().hasHeightForWidth())
        self.training_corpus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.training_corpus.setFont(font)
        self.training_corpus.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(22, 210, 152);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(22, 210, 152);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.training_corpus.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.training_corpus.setObjectName("training_corpus")
        self.verticalLayout_9.addWidget(self.training_corpus)
        self.horizontalLayout_12.addWidget(self.training_corpus_frame)
        self.training_grammar_frame = QtWidgets.QFrame(self.training_group_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_grammar_frame.sizePolicy().hasHeightForWidth())
        self.training_grammar_frame.setSizePolicy(sizePolicy)
        self.training_grammar_frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.training_grammar_frame.setSizeIncrement(QtCore.QSize(100, 0))
        self.training_grammar_frame.setBaseSize(QtCore.QSize(200, 0))
        self.training_grammar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_grammar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_grammar_frame.setObjectName("training_grammar_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.training_grammar_frame)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.training_grammar = QtWidgets.QPlainTextEdit(self.training_grammar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_grammar.sizePolicy().hasHeightForWidth())
        self.training_grammar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.training_grammar.setFont(font)
        self.training_grammar.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(22, 210, 152);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(22, 210, 152);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.training_grammar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.training_grammar.setObjectName("training_grammar")
        self.verticalLayout_8.addWidget(self.training_grammar)
        self.horizontalLayout_12.addWidget(self.training_grammar_frame)
        self.verticalLayout_3.addWidget(self.training_group_1)
        self.training_btns = QtWidgets.QFrame(self.training_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_btns.sizePolicy().hasHeightForWidth())
        self.training_btns.setSizePolicy(sizePolicy)
        self.training_btns.setMaximumSize(QtCore.QSize(16777215, 70))
        self.training_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.training_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.training_btns.setObjectName("training_btns")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.training_btns)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.training_btn_load_corpus = QtWidgets.QPushButton(self.training_btns)
        self.training_btn_load_corpus.setMinimumSize(QtCore.QSize(180, 60))
        self.training_btn_load_corpus.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.training_btn_load_corpus.setFont(font)
        self.training_btn_load_corpus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.training_btn_load_corpus.setStyleSheet("QPushButton {\n"
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
        self.training_btn_load_corpus.setObjectName("training_btn_load_corpus")
        self.horizontalLayout_8.addWidget(self.training_btn_load_corpus)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.training_btn_generate_grammar = QtWidgets.QPushButton(self.training_btns)
        self.training_btn_generate_grammar.setMinimumSize(QtCore.QSize(180, 60))
        self.training_btn_generate_grammar.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.training_btn_generate_grammar.setFont(font)
        self.training_btn_generate_grammar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.training_btn_generate_grammar.setStyleSheet("QPushButton {\n"
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
        self.training_btn_generate_grammar.setObjectName("training_btn_generate_grammar")
        self.horizontalLayout_8.addWidget(self.training_btn_generate_grammar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.training_btn_save_grammar = QtWidgets.QPushButton(self.training_btns)
        self.training_btn_save_grammar.setMinimumSize(QtCore.QSize(180, 60))
        self.training_btn_save_grammar.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.training_btn_save_grammar.setFont(font)
        self.training_btn_save_grammar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.training_btn_save_grammar.setStyleSheet("QPushButton {\n"
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
        self.training_btn_save_grammar.setObjectName("training_btn_save_grammar")
        self.horizontalLayout_8.addWidget(self.training_btn_save_grammar)
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
        self.inference_group_1 = QtWidgets.QFrame(self.inference_content)
        self.inference_group_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inference_group_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inference_group_1.setObjectName("inference_group_1")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.inference_group_1)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.inference_text_frame = QtWidgets.QFrame(self.inference_group_1)
        self.inference_text_frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference_text_frame.sizePolicy().hasHeightForWidth())
        self.inference_text_frame.setSizePolicy(sizePolicy)
        self.inference_text_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inference_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inference_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inference_text_frame.setObjectName("inference_text_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.inference_text_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.inference_text = QtWidgets.QPlainTextEdit(self.inference_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference_text.sizePolicy().hasHeightForWidth())
        self.inference_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.inference_text.setFont(font)
        self.inference_text.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(22, 210, 152);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(22, 210, 152);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.inference_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inference_text.setObjectName("inference_text")
        self.verticalLayout_7.addWidget(self.inference_text)
        self.inference_tags = QtWidgets.QPlainTextEdit(self.inference_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference_tags.sizePolicy().hasHeightForWidth())
        self.inference_tags.setSizePolicy(sizePolicy)
        self.inference_tags.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.inference_tags.setFont(font)
        self.inference_tags.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(22, 210, 152);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(22, 210, 152);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.inference_tags.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inference_tags.setObjectName("inference_tags")
        self.verticalLayout_7.addWidget(self.inference_tags)
        self.inference_precision = QtWidgets.QPlainTextEdit(self.inference_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference_precision.sizePolicy().hasHeightForWidth())
        self.inference_precision.setSizePolicy(sizePolicy)
        self.inference_precision.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.inference_precision.setFont(font)
        self.inference_precision.setStyleSheet("QPlainTextEdit {\n"
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
        self.inference_precision.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inference_precision.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inference_precision.setObjectName("inference_precision")
        self.verticalLayout_7.addWidget(self.inference_precision)
        self.inference_group_2 = QtWidgets.QFrame(self.inference_text_frame)
        self.inference_group_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.inference_group_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inference_group_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inference_group_2.setObjectName("inference_group_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.inference_group_2)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.inference_btn_previous = QtWidgets.QPushButton(self.inference_group_2)
        self.inference_btn_previous.setMinimumSize(QtCore.QSize(180, 60))
        self.inference_btn_previous.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.inference_btn_previous.setFont(font)
        self.inference_btn_previous.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inference_btn_previous.setStyleSheet("QPushButton {\n"
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
        self.inference_btn_previous.setObjectName("inference_btn_previous")
        self.horizontalLayout_14.addWidget(self.inference_btn_previous)
        self.inference_btn_next = QtWidgets.QPushButton(self.inference_group_2)
        self.inference_btn_next.setMinimumSize(QtCore.QSize(180, 60))
        self.inference_btn_next.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.inference_btn_next.setFont(font)
        self.inference_btn_next.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inference_btn_next.setStyleSheet("QPushButton {\n"
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
        self.inference_btn_next.setObjectName("inference_btn_next")
        self.horizontalLayout_14.addWidget(self.inference_btn_next)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.verticalLayout_7.addWidget(self.inference_group_2)
        self.horizontalLayout_13.addWidget(self.inference_text_frame)
        self.inference_grammar_frame = QtWidgets.QFrame(self.inference_group_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference_grammar_frame.sizePolicy().hasHeightForWidth())
        self.inference_grammar_frame.setSizePolicy(sizePolicy)
        self.inference_grammar_frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.inference_grammar_frame.setSizeIncrement(QtCore.QSize(100, 0))
        self.inference_grammar_frame.setBaseSize(QtCore.QSize(200, 0))
        self.inference_grammar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inference_grammar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inference_grammar_frame.setObjectName("inference_grammar_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.inference_grammar_frame)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.inference_grammar = QtWidgets.QPlainTextEdit(self.inference_grammar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference_grammar.sizePolicy().hasHeightForWidth())
        self.inference_grammar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.inference_grammar.setFont(font)
        self.inference_grammar.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(225,225,225,0.1);\n"
"    color: rgba(225,225,225,0.7);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(225,225,225,0.2);\n"
"    color: rgba(225,225,225,1);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(22, 210, 152);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 20px;\n"
"\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(22, 210, 152);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgba(225,225,225,0.2);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.inference_grammar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inference_grammar.setObjectName("inference_grammar")
        self.verticalLayout_11.addWidget(self.inference_grammar)
        self.horizontalLayout_13.addWidget(self.inference_grammar_frame)
        self.verticalLayout_6.addWidget(self.inference_group_1)
        self.inference_btns = QtWidgets.QFrame(self.inference_content)
        self.inference_btns.setMaximumSize(QtCore.QSize(16777215, 70))
        self.inference_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inference_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inference_btns.setObjectName("inference_btns")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.inference_btns)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.inference_btn_load_grammar = QtWidgets.QPushButton(self.inference_btns)
        self.inference_btn_load_grammar.setMinimumSize(QtCore.QSize(180, 60))
        self.inference_btn_load_grammar.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.inference_btn_load_grammar.setFont(font)
        self.inference_btn_load_grammar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inference_btn_load_grammar.setStyleSheet("QPushButton {\n"
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
        self.inference_btn_load_grammar.setObjectName("inference_btn_load_grammar")
        self.horizontalLayout_9.addWidget(self.inference_btn_load_grammar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.inference_btn_load_text = QtWidgets.QPushButton(self.inference_btns)
        self.inference_btn_load_text.setMinimumSize(QtCore.QSize(180, 60))
        self.inference_btn_load_text.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.inference_btn_load_text.setFont(font)
        self.inference_btn_load_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inference_btn_load_text.setStyleSheet("QPushButton {\n"
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
        self.inference_btn_load_text.setObjectName("inference_btn_load_text")
        self.horizontalLayout_9.addWidget(self.inference_btn_load_text)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.inference_btn_save_inference = QtWidgets.QPushButton(self.inference_btns)
        self.inference_btn_save_inference.setMinimumSize(QtCore.QSize(180, 60))
        self.inference_btn_save_inference.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.inference_btn_save_inference.setFont(font)
        self.inference_btn_save_inference.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inference_btn_save_inference.setStyleSheet("QPushButton {\n"
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
        self.inference_btn_save_inference.setObjectName("inference_btn_save_inference")
        self.horizontalLayout_9.addWidget(self.inference_btn_save_inference)
        self.verticalLayout_6.addWidget(self.inference_btns)
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
        self.training_corpus.setPlainText(_translate("MainWindow", "Corpus:"))
        self.training_grammar.setPlainText(_translate("MainWindow", "Grammar:\n"
"\n"
""))
        self.training_btn_load_corpus.setText(_translate("MainWindow", "Load Corpus"))
        self.training_btn_generate_grammar.setText(_translate("MainWindow", "Generate Grammar"))
        self.training_btn_save_grammar.setText(_translate("MainWindow", "Save Grammar"))
        self.inference_text.setPlainText(_translate("MainWindow", "Sentence:\n"
"\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."))
        self.inference_tags.setPlainText(_translate("MainWindow", "Tags:\n"
"\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
""))
        self.inference_precision.setPlainText(_translate("MainWindow", "Precision:\n"
""))
        self.inference_btn_previous.setText(_translate("MainWindow", "Previous"))
        self.inference_btn_next.setText(_translate("MainWindow", "Next "))
        self.inference_grammar.setPlainText(_translate("MainWindow", "Grammar:\n"
"\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
""))
        self.inference_btn_load_grammar.setText(_translate("MainWindow", "Load Grammar"))
        self.inference_btn_load_text.setText(_translate("MainWindow", "Load Text"))
        self.inference_btn_save_inference.setText(_translate("MainWindow", "Inference"))
        self.label_credits.setText(_translate("MainWindow", "By: Billel Mokeddem and Ryad Boudrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
