import sys
from PySide6 import QtGui
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile,QIODevice,QTimer
from PySide6.QtWidgets import QApplication,QLabel,QPushButton,QLineEdit,QTextEdit,QMessageBox
import os
application_path = os.path.dirname (sys.executable)
class Main():

      def __init__(self):
################################################################################################
            self.app = QApplication(sys.argv)
            ui_file_name = r"lib\UI.ui"
            ui_file = QFile(ui_file_name)
            ui_file.open(QIODevice.ReadOnly)
            loader = QUiLoader()
            window = loader.load(ui_file)
            window.show()      
            self.msg = QMessageBox()
            sys.exit(self.app.exec())
#######################################_set_ui_############################################
            # camara = window.findChild(QLabel,"camera")
            # CAMERA_CONNECT = window.findChild(QPushButton,"CAMERA_CONNECT")
            # print(camara)
            # IP_CONNECT = window.findChild(QPushButton,"IP_CONNECT")
            # label_camera = window.findChild(QLineEdit,"CAMERA")
            # IP = window.findChild(QLineEdit,"IP")
            # PORT = window.findChild(QLineEdit,"PORT")
            # show_text = window.findChild(QTextEdit,"SHOW_TEXT")
            # btn_Forward = window.findChild(QPushButton,"Forward")
            # btn_Stop = window.findChild(QPushButton,"Stop")
            # btn_Reverse = window.findChild(QPushButton,"Reverse")
            # Auto = window.findChild(QPushButton,"Auto")

            # run_loop = QTimer()
################################################################################################


      def messagebox(self,text):
            self.msg.setWindowTitle("App")
            self.msg.setText(text)
            self.msg.exec_()


if __name__ == "__main__":
      Main()
