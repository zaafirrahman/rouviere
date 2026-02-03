from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from second_win import *


     
class MainWin(QWidget):
   def __init__(self):
       ''' the window which the greeting is located in '''
       super().__init__()


       # sets what the window will look like (label, size, location)
       self.set_appear()


       # creating and configuring graphic elements:
       self.initUI()


       #establishes connections between elements
       self.connects()


       # start:
       self.show()


   def initUI(self):
       ''' creates graphic elements '''
       self.btn_next = QPushButton(txt_next)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)


       self.layout = QVBoxLayout()
       self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout)


  
   def next_click(self):
       self.tw = TestWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   ''' sets what the window will look like (label, size, location) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


def main():
   app = QApplication([])
   mw = MainWin()
   app.exec_()


main()
