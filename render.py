from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore,QtGui

class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)

        # убираем контекстное меню на правой кнопке мыши
        self.browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        # загружаем страницу google.com
        self.browser.load(QtCore.QUrl("http://localhost:1441"))
        # устанавливаем заголовок окна
        self.setWindowTitle("PjLaunch!")

        # устанавливаем размер окна
        self.setFixedSize(1000,600)

app = QtWidgets.QApplication([])
app.setWindowIcon(QtGui.QIcon('res/icon.png'))
window = Browser()
window.setWindowIcon(QtGui.QIcon('res/icon.png'))
window.show()
app.exec_()