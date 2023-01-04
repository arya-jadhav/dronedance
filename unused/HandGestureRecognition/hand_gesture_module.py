# class GestureStreaming(QLabel):
#     reSize = pyqtSignal(QSize)
#     def __init__(self, ParentWidget):
#         super(GestureStreaming, self).__init__()
#         self.initUI()

#     # def ImageUpdateSlot(self, Frame):
#     #     self.label_vidCapture.setPixmap(QPixmap.fromImage(Frame))

#     @pyqtSlot(QImage)
#     def setImage(self, Frame):
#         self.label_vidCapture.setPixmap(QPixmap.fromImage(Frame))

#     def initUI(self, ParentWidget):
#         self.setWindowTitle("Image")
#         # Create A Label
#         self.label_vidCapture = QLabel(ParentWidget)
#         self.label_vidCapture.setStyleSheet("border-radius: 10px;")
#         self.label_vidCapture.setText("")
#         self.label_vidCapture.setAlignment(Qt.AlignCenter)
#         self.label_vidCapture.setObjectName("label_vidCapture")

#         vidCap = HandGestureModule(self)
#         vidCap.ImageUpdate.connect(self.setImage)
#         self.reSize.connect(vidCap.scaled)
#         vidCap.start()

#     def resizeEvent(self, event):
#         print(self.size())
#         self.reSize.emit(self.size())