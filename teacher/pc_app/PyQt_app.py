import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import threading

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Sir Complex")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        self.web_view.setUrl(QUrl("https://jaskintech.com"))


    def closeEvent(self, event):
        event.accept()

if __name__ == "__main__":
    _app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(_app.exec_())