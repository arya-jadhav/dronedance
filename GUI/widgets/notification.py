# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import pyqtProperty
import sys

class Message(QWidget):
    def __init__(self, title, message, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.setContentsMargins(0, 0, 0 ,0)
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold; padding: 0;")
        self.titleLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.messageLabel = QLabel(message, self)
        self.messageLabel.setStyleSheet("font-size: 14px; font-weight: normal; padding: 0;")
        self.messageLabel.setWordWrap(True)
        self.buttonClose = QPushButton(self)
        self.buttonClose.setIcon(QIcon.fromTheme("window-close"))
        self.buttonClose.setFlat(True)
        self.buttonClose.setFixedSize(32, 32)
        self.buttonClose.setIconSize(QSize(16, 16))
        self.layout().addWidget(self.titleLabel)
        self.layout().addWidget(self.messageLabel, 2, 0)
        self.layout().addWidget(self.buttonClose, 0, 1)

class Notification(QDialog):
    # Change property of QDialog's opacity to window opacity instead
    def windowOpacity(self):
        return super().windowOpacity()    
    
    def setWindowOpacity(self, opacity):
        super().setWindowOpacity(opacity) 

    opacity = pyqtProperty(float, windowOpacity, setWindowOpacity)   

    def __init__(self, display='standard', *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(Stylesheet)

        self.initUi(display)

    def initUi(self, display='standard'):
        # Important: this widget is used as background and rounded corners.
        self.widget = QWidget(self)
        self.widget.setMinimumWidth(500)
        
        # Change CSS id depending on which display
        # Choices: 'standard', 'success', 'warning', 'error', 'information'
        if display == 'standard':
            self.widget.setObjectName('StandardNotification')
        elif display == 'success':
            self.widget.setObjectName('SuccessNotification')
        elif display == 'warning':
            self.widget.setObjectName('WarningNotification')
        elif display == 'error':
            self.widget.setObjectName('ErrorNotification')
        elif display == 'information':
            self.widget.setObjectName('InformationNotification')

        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

    def setNotify(self, title, message, timeout):
        # Intitalize Message Widget
        self.msg = Message(title, message)

        # Add user interface to widget
        self.layout = QHBoxLayout(self.widget)
        self.layout.addWidget(self.msg)
        self.verticalLayout = QVBoxLayout()
        self.closeButton = QPushButton('r', self, clicked=self.accept, objectName='closeButton')
        self.verticalLayout.addWidget(self.closeButton)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.layout.addLayout(self.verticalLayout)
        self.layout.setStretch(0, 1)

        # Show the notification and play the fade animation
        self.setWindowOpacity(0.0)
        self.show()
        self.startFadeAnimation()
        
    def closeNotification(self):
        self.close()

    def onClicked(self):
        self.close()

    def startFadeIn(self):
        self.animation = QPropertyAnimation(self, b"opacity")
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setDuration(800)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()

    def startFadeOut(self):
        self.animation = QPropertyAnimation(self, b"opacity")
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setDuration(2000)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()

    def startFadeAnimation(self):
        self.startFadeIn()
        QTimer.singleShot(3000, self.startFadeOut)
        QTimer.singleShot(5000, self.closeNotification)   

Stylesheet = """
#StandardNotification {
    background: #bfbfbf;
    border-radius: 12px;
    opacity: 100;
    border: 2px solid #595959;                   
}
#SuccessNotification {
    background: #95de64;
    border-radius: 12px;
    opacity: 100;
    border: 2px solid #52c41a;                   
}
#WarningNotification {
    background: #ffc53d;
    border-radius: 12px;
    opacity: 100;
    border: 2px solid #faad14;                   
}
#ErrorNotification {
    background: #ff7875;
    border-radius: 12px;
    opacity: 100;
    border: 2px solid #f5222d;                   
}
#InformationNotification {
    background: #69b1ff;
    border-radius: 12px;
    opacity: 100;
    border: 2px solid #1677ff;                   
}
#closeButton {
    min-width: 30px;
    min-height: 30px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: #ccc;
    background: red;
}
"""

# This HIDDEN class is just used to test the Notification class
class _NotificationDemo(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        btn = QPushButton(QIcon.fromTheme("info"), "Show Notification")
        btn.setFixedWidth(110)
        btn.setFixedHeight(30)
        self.setCentralWidget(btn)
        btn.clicked.connect(self.showNotification)
        
    def showNotification(self):
        self.notification = Notification(display='error')
        self.notification.setNotify("Error", "Some is certainly going wrong in this application, aaaaaaaaaaaaaaaaaaaahhhhh!", 3000)
        # Calculate the position of window, and display the notification
        r = QRect(self.x() + round(self.width() / 2) - round(self.notification.width() / 2), 
                                        self.y() + 26, self.notification.msg.messageLabel.width() + 30, self.notification.msg.messageLabel.height())
        self.notification.setGeometry(r)

        
# Comment this out if you would like to try out the Notification class
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = _NotificationDemo()
#     w.resize(600, 330)
#     w.show()
#     sys.exit(app.exec_())