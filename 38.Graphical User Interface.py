import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700 , 300 , 500, 500)      #setGeometry(x , y ,weight,height)
        self.setWindowIcon(QIcon("icon logo for GUI.png"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Aerial", 30))
        label.setGeometry(0 ,0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
       # label.setAlignment(Qt.AlignBottom)  #vertically Bottom
        #label.setAlignment(Qt.AlignTop)      # vertically  Top
       # label.setAlignment(Qt.AlignVCenter)  # vertically Center

       # label.setAlignment(Qt.AlignRight)   #Horizontally Right
       # label.setAlignment(Qt.AlignHCenter)   #Horizontally Center
       # label.setAlignment(Qt.AlignLeft)           # Horizontally Left
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)   #Center & Top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   #Center & Center
        label.setAlignment(Qt.AlignCenter)                  #Center & Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    # QApplication it manages application-wide resources, the event loop, and settings
    # sys.argv passes command-line arguments to the application
    # (if you want to run your program with options like python myapp.py --dark-mode).
    # If you don’t need arguments, you could just use QApplication([])
    #app.exec_() starts the Qt event loop. This loop waits for user actions (like clicks, typing, resizing)
# and dispatches them to the appropriate widgets.The program will keep running until the user closes the window or calls app.quit().
#Wrapping it in sys.exit() ensures that when the event loop ends, the program exits cleanly with the correct status code.




if __name__ == '__main__':
    main()

