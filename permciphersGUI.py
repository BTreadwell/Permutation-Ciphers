from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
import permmanager

class CipherMainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        #create gui elements
        ##label, input field
        self.source_row = (QLabel('Source File: '), QLineEdit())
        self.dest_row = (QLabel('Output Destination: '), QLineEdit())
        self.key_row = (QLabel('Key'), QLineEdit())
        ##encr, decr
        self.perm_buttons = (QPushButton("Encrypt"), QPushButton("Decrypt"))

        #Connect buttons to functions
        ##
        self.perm_buttons[0].clicked.connect(self.do_permutate)
        self.perm_buttons[1].clicked.connect(self.do_inv_permutate)

        #assign elements to layout
        layout = QGridLayout()
        #add by row using enumerate to track row index
        for row_index, row in enumerate([self.source_row, self.dest_row, self.key_row, self.perm_buttons]):
            layout.addWidget(row[0], row_index, 0)
            layout.addWidget(row[1], row_index, 1)

        #create container and set as central widget
        container = QWidget()
        container.setLayout(layout)

        self.setWindowTitle("Permutation Ciphers >:)")
        self.setCentralWidget(container)

    #runs when encrypt or decrypt button is clicked, passes data in fields to
    #GUIhelper function in permutationciphers module.
    def do_permutate(self, key_or_inv=0):
        source = self.source_row[1].text
        dest = self.dest_row[1].text
        key = 'DEFAULT'
        if self.key_row[1].text != None:
            key = self.key_row[1].text

        if permmanager.validate(a_key=key, a_source=source, a_dest=dest):
            permmanager.process_request(mode=key_or_inv, a_key=key, a_source=source, a_dest=dest)


    def do_inv_permutate(self):
        self.do_permutate(key_or_inv=1)

def run_GUI():
    new_qapp = QApplication([])
    new_window = CipherMainWindow()
    new_window.show()
    new_qapp.exec()

def main():
    run_GUI()

if __name__ == "__main__":
    main()
