

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
from gui.widgets.notification import Notification

# Global Variables
counter = 0
GestureModule = HandGestureModule()

# CONNECTED UI
class MainWindow(QMainWindow):
    global GestureModule

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon('.\gui\icon\drone.png'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.NOTIFICATION_LIMIT = 2
        self.notification_displayed = 0

        # CONTINUE BUTTON CLICK EVENT
        self.ui.button_proceed.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_capture))

        # Hand Gesture Module
        GestureModule.start()
        GestureModule.ImageUpdate.connect(self.UpdateVideoCapture)
        GestureModule.GesturePredictionUpdate.connect(self.UpdateGesturePrediction)
        GestureModule.mapper.emitter.GestureCapturedAndInstructionToBeExecutedLabelUpdate.connect(self.UpdateGestureCapturedAndInstructionToBeExecutedLabel)
        GestureModule.mapper.emitter.PreviousInstructionToDronesLabelUpdate.connect(self.UpdatePreviousInstructionToDrones)

        # Notification Widget
        GestureModule.mapper.emitter.SendNotification.connect(self.ShowNotification)

    def ShowNotification(self, dct):
        if self.notification_displayed < self.NOTIFICATION_LIMIT:
                self.notification = Notification(display=dct['display'])
                self.notification.setNotify(dct['title'], dct['message'])
                # Calculate the position of window, and display the notification
                rect = QRect(self.x() + round(self.width() / 2) - round(self.notification.width() / 2), 
                                                self.y() + 26, self.notification.msg.messageLabel.width() + 30, self.notification.msg.messageLabel.height())
                # rect = QtCore.QRect(0, 0, self.notification.msg.messageLabel.width() + 30, self.notification.msg.messageLabel.height())
                self.notification.setGeometry(rect)
                self.notification.emitter.NotificationDisplayed.connect(self.AllowNewNotification)
                self.notification_displayed += 1

    def AllowNewNotification(self, num):
                self.notification_displayed = num

    def UpdateVideoCapture(self, frame):
        self.ui.label_vidCapture.setPixmap(QPixmap.fromImage(frame))

    def UpdateGesturePrediction(self, prediction):
        self.ui.label_handGesture_prediction.setText(prediction)

    def UpdateGestureCapturedAndInstructionToBeExecutedLabel(self, dct):
        if dct['do_reset']:
               self.ui.label_gestureCaptured_output.setText('')
               self.ui.label_instructionToBeExecuted_output.setText('')
        else:
               self.ui.label_gestureCaptured_output.setText(dct['gesture_captured'])
               self.ui.label_instructionToBeExecuted_output.setText(dct['instruction_to_be_executed'] if dct['instruction_to_be_executed'] is not None else '')

    def UpdatePreviousInstructionToDrones(self, prev_instruction):
        self.ui.label_prevInstructionToDrones_output.setText(prev_instruction)

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