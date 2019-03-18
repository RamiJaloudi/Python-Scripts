
import sys
from PySide.QtGui import QApplication
from PySide.QtCore import QUrl
from PySide.QtWebkit import QWebView

app = QApplication(sys.argv)
b = QWebView()
b.load(QUrl('http://www.youtube.com'))
b.show()
app.exec_()


