import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import qtawesome as qta 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        home_icon = qta.icon('fa5s.home')
        home_btn = QAction(home_icon, '', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        back_icon = qta.icon('fa5s.arrow-left')
        back_btn = QAction(back_icon, '', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_icon = qta.icon('fa5s.arrow-right')
        forward_btn = QAction(forward_icon, '', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_icon = qta.icon('fa5s.sync')  # or 'fa.sync'
        reload_btn = QAction(reload_icon, '', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Ziggor')
window = MainWindow()
app.exec_()
