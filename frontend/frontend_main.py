import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QColor
from interface import Ui_MainWindow
import re
sys.path.append('../backend')
import backend_main

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
        
        # Set DropShadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        # Apply shadow to frame
        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

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
        
        ## Backend Variables
        ########################################################################
        
        # Corpus
        self.corpus = None 
        
        # Grammar
        self.grammar = None
        
        # S content 
        self.s_content_length = None
        
        # Corpus files list
        self.files_names = None
        
        # Test sentences with tags
        self.sents_tags_test = None
        
        # The number Of printed setntence
        self.printed_sentence = 0
        
        # precision
        self.precision = None
        
        # Rewards List
        self.rewards_precision_list = None
        
        ## UI Event Listeners
        ########################################################################
        
        # Load corpus
        self.ui.training_btn_load_corpus.clicked.connect(self.training_btn_load_corpus)
        
        # Generate Grammar
        self.ui.training_btn_generate_grammar.clicked.connect(self.training_btn_generate_grammar)
        
        # Save Grammar
        self.ui.training_btn_save_grammar.clicked.connect(self.training_btn_save_grammar)
        
        # Load Grammar
        self.ui.inference_btn_load_grammar.clicked.connect(self.inference_btn_load_grammar)
        
        # Load Text
        self.ui.inference_btn_load_text.clicked.connect(self.inference_btn_load_text)
        
        # Previous Sentence
        self.ui.inference_btn_previous.clicked.connect(self.inference_btn_previous)
        
        # Next Sentence
        self.ui.inference_btn_next.clicked.connect(self.inference_btn_next)
        
        # inference
        self.ui.inference_btn_inference.clicked.connect(self.inference_btn_inference)
        
        
        # Show window
        self.show()
    
    def inference_btn_inference(self):        
        worked, results, error = backend_main.inference_nltk(self.grammar, [word[1] for word in self.sents_tags_test[self.printed_sentence]], self.s_content_length)
        if not worked:
            file=open('../Logs/logs.txt','w')
            file.write(' '.join([word[0] for word in self.sents_tags_test[self.printed_sentence]]))
            file.close()
            if not error:
                self.ui.inference_grammar.setPlainText('No Derivation Tree for this \nsentence:\n\n Reward Factor: ' + str(self.rewards_precision_list[self.printed_sentence][0]))
            else:
                self.ui.inference_grammar.setPlainText('No Derivation Tree for this \nsentence:\n\n Error: Grammar does not \ncover some of the input \ntags')
        else:
            self.ui.inference_grammar.setPlainText('Derivation Tree:\n')
            for result in results:  
                #print(str(result))
                self.ui.inference_grammar.appendPlainText(str(result))
            #self.ui.inference_grammar.appendPlainText('\n Reward Factor: ' + str(self.rewards_list[self.printed_sentence]))

        
    def training_btn_load_corpus(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)
        dlg.setFilter(QDir.Files)
        
        if dlg.exec_():
            self.files_names = dlg.selectedFiles()
            
            file = ''
            for file_name in self.files_names:
                file += backend_main.read_file(file_name)
            self.ui.training_corpus.setPlainText(file)
            self.corpus = file
            self.ui.training_btn_generate_grammar.setEnabled(True)

    
    def training_btn_generate_grammar(self):
        self.grammar, _, self.s_content_length = backend_main.induce_grammar(self.corpus)
        self.ui.training_grammar.setPlainText('Grammar:\n')
        self.ui.inference_grammar.setPlainText('Grammar:\n')

        for rule in self.grammar:  
            self.ui.training_grammar.appendPlainText(rule[0] + ' ==> ' + rule[1])
            self.ui.inference_grammar.appendPlainText(rule[0] + ' ==> ' + rule[1])
        self.ui.training_btn_save_grammar.setEnabled(True)
        if self.sents_tags_test is not None and self.grammar is not None:
            self.ui.inference_btn_inference.setEnabled(True)
            self.precision, self.rewards_precision_list = backend_main.precision(self.files_names, self.sents_tags_test)
            #self.precision, self.rewards_precision_list = backend_main.precision(self.files_names, self.grammar, self.sents_tags_test)
            self.ui.inference_precision.setPlainText('Precision: '+ str(self.precision))

        
    def training_btn_save_grammar(self):
        import time 
        path = '../Grammars/Grammar'
        time = time.ctime()
        time = str(time).replace(' ','_').replace(':','_')
        path = path + time + '.txt'
        file=open(path,"w")
        file.write('****'.join(self.files_names) + '****\n')
        #file.write(str(self.s_content_length) + '****\n')
        for rule in self.grammar:
            file.write(rule[0] + ' ==> ' + rule[1] + '\n')
            
    def inference_btn_load_grammar(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            file_name = dlg.selectedFiles()
            file = open(file_name[0],"r")
            file = file.readlines()
            self.grammar = []
            self.ui.training_grammar.setPlainText('Grammar:\n')
            self.ui.inference_grammar.setPlainText('Grammar:\n')
            self.files_names = file[0].split('****')
            del self.files_names[-1]
            del file[0]
            # self.s_content_length = int(file[0].split('****')[0])
            # del file[0]
            for line in file:
                m = re.search(r'(NT[0-9]+) ==> (.*)',line)
                self.grammar.append((m.group(1),m.group(2)))
                self.ui.training_grammar.appendPlainText(m.group(1) + ' ==> ' + m.group(2))
                self.ui.inference_grammar.appendPlainText(m.group(1) + ' ==> ' + m.group(2))
            self.ui.training_btn_save_grammar.setEnabled(True)
            if self.sents_tags_test is not None and self.grammar is not None:
                self.ui.inference_btn_inference.setEnabled(True)
                self.precision, self.rewards_precision_list = backend_main.precision(self.files_names, self.sents_tags_test)
                #self.precision, self.rewards_precision_list = backend_main.precision(self.files_names, self.grammar, self.sents_tags_test)
                self.ui.inference_precision.setPlainText('Precision: '+ str(self.precision))
    
    def inference_btn_load_text(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        
        if dlg.exec_():
            file_name = dlg.selectedFiles()
            file = backend_main.read_file(file_name[0])
            # Check if text is already tagged
            def text_tagged(file):
                i, counter = 0,0
                while 1:
                    if file[i] == '/':
                        counter += 1
                    if counter > 3:
                        return True
                        
                    if i > 150:
                        break
                    i += 1
                return False
            
            if not text_tagged(file): 
                file = backend_main.tag_sentence(file)
            
            #print(file)
            self.sents_tags_test = backend_main.get_tags(file, words=True)
            #print(self.sents_tags_test)
            # Update Plains
            self.ui.inference_sents.setPlainText('')
            self.ui.inference_tags.setPlainText('')
            self.ui.inference_sents.appendPlainText(' '.join([word[0] for word in self.sents_tags_test[0]]))
            #print([word for word in self.sents_tags_test[0]])
            self.ui.inference_tags.appendPlainText(' '.join([word[1] for word in self.sents_tags_test[0]]))
            self.printed_sentence = 0
            # Update sentence number label
            self.ui.inference_sents_number.setText('Sentence number ' + str(self.printed_sentence + 1) + ' from ' + str(len(self.sents_tags_test)))
            # Update buttons status
            self.ui.inference_btn_previous.setEnabled(False)
            if len(self.sents_tags_test) > 1:
                self.ui.inference_btn_next.setEnabled(True)
            if self.sents_tags_test is not None and self.grammar is not None:
                self.ui.inference_btn_inference.setEnabled(True)
                self.precision, self.rewards_precision_list = backend_main.precision(self.files_names, self.sents_tags_test)
                #self.precision, self.rewards_precision_list = backend_main.precision(self.files_names, self.grammar, self.sents_tags_test)
                self.ui.inference_precision.setPlainText('Precision: '+ str(self.precision))
                
    def inference_btn_previous(self):
        self.printed_sentence -= 1
        # Update sentence plain
        self.ui.inference_sents.setPlainText('')
        self.ui.inference_sents.appendPlainText(' '.join([word[0] for word in self.sents_tags_test[self.printed_sentence]]))
        # Update tags plain
        self.ui.inference_tags.setPlainText('')
        self.ui.inference_tags.appendPlainText(' '.join([word[1] for word in self.sents_tags_test[self.printed_sentence]]))
        # Update sentence number label
        self.ui.inference_sents_number.setText('Sentence number ' + str(self.printed_sentence + 1) + ' from ' + str(len(self.sents_tags_test)))

        # Update precision plain
        if self.printed_sentence == 0:
            self.ui.inference_btn_previous.setEnabled(False)
        self.ui.inference_btn_next.setEnabled(True)
        
    def inference_btn_next(self):
        self.printed_sentence += 1
        # Update sentence plain
        self.ui.inference_sents.setPlainText('')
        self.ui.inference_sents.appendPlainText(' '.join([word[0] for word in self.sents_tags_test[self.printed_sentence]]))
        # Update tags plain
        self.ui.inference_tags.setPlainText('')
        self.ui.inference_tags.appendPlainText(' '.join([word[1] for word in self.sents_tags_test[self.printed_sentence]]))
        # Update sentence number label
        self.ui.inference_sents_number.setText('Sentence number ' + str(self.printed_sentence + 1) + ' from ' + str(len(self.sents_tags_test)))


        # Update precision plain

        if self.printed_sentence == len(self.sents_tags_test) - 1:
            self.ui.inference_btn_next.setEnabled(False)
        self.ui.inference_btn_previous.setEnabled(True)
            


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