import sys

from PyQt5.QtWidgets import QApplication

from window import mainWindow

app = QApplication(sys.argv)
window = mainWindow()
window.show()
app.exec()
