
import sys

from PyQt5.QtWidgets import *

# GUI FILE
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PAGES
        ########################################################################

        # PAGE Training
        self.ui.btn_training.clicked.connect(self.training_btn_clicked)
        
        # PAGE Training
        self.ui.btn_inference.clicked.connect(self.inference_btn_clicked)
        
        
        
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        
        

    def training_btn_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.training)
        self.ui.btn_training.setStyleSheet("background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n")
        self.ui.btn_inference.setStyleSheet("QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"")
        
        
    def inference_btn_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.inference)
        self.ui.btn_inference.setStyleSheet("background-color: rgb(22, 210, 152);\n"
"    color: rgb(38, 62, 81);\n")
        
        self.ui.btn_training.setStyleSheet("QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"")
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())





















