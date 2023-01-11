

import sys
import platform
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# > SPLASH SCREEN UI
from gui.ui_splash_screen import Ui_SplashScreen

# > MAIN WINDOW UI
from gui.ui_main import Ui_MainWindow

from modules import HandGestureModule

# Global Variables
counter = 0
GestureModule = HandGestureModule()

# CONNECTED UI
class MainWindow(QMainWindow):
    global GestureModule

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon('.\gui\icon\drone.png'))
        self.ui = Ui_MainWindow(window=self, GestureModule=GestureModule)
        self.ui.setupUi(self)

    def closeEvent(self, a0: QCloseEvent) -> None:
        # CLOSE SOCKET HERE
        GestureModule.mapper.close_socket() # Close the sockets
        GestureModule.stop() # Stop Gesture Module thread
        a0.accept() # let the window close

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon('.\gui\icon\drone.png'))
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(30)

        # CHANGE LOADING TEXT

        # Initial Text
        self.ui.label_loading.setText("Loading...")

        # Change Texts
        # QTimer.singleShot(1500, lambda: self.ui.label_loading.setText('Downloading dependencies...'))
        QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("Setting up application..."))
        QTimer.singleShot(4500, lambda: self.ui.label_loading.setText("Done!"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_()) 