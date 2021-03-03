
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from interface import Ui_MainWindow

GLOBAL_STATE = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## UI functions
        ########################################################################
        
        # Define a frameless UI
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Implementing the Dragging feature
        def move_window(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        
        self.ui.title_bar.mouseMoveEvent = move_window
    
        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        
        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        # PAGE Training
        self.ui.btn_training.clicked.connect(self.training_btn_clicked)
        
        # PAGE Inference
        self.ui.btn_inference.clicked.connect(self.inference_btn_clicked)
        
        # Show window
        self.show()
        

    def training_btn_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.training)
        self.ui.btn_training.setStyleSheet("background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n")
        self.ui.btn_inference.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"")
        
    def inference_btn_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.inference)
        self.ui.btn_inference.setStyleSheet("background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n")
        
        self.ui.btn_training.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(255, 255, 255, 1);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"")
        
    def mousePressEvent(self, event):
            self.dragPos = event.globalPos()
    
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
    
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
    
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
    
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 62, 81, 255), stop:1 rgba(7, 34, 56, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.shadow_layout.setContentsMargins(10, 10, 10, 10)
            #self.ui.shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 62, 81, 255), stop:1 rgba(7, 34, 56, 255)); border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())