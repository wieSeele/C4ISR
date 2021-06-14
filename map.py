## 尝试folium库作为Map的基础
import folium
import pandas as pd
import webbrowser

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QSplitter, QGridLayout, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt5.QtCore import Qt, QUrl, QFileInfo
from PyQt5.QtWebEngineWidgets import QWebEngineView



class Main_Window(QMainWindow):
  def __init__(self):
    self.desktop = QApplication.desktop()
    self.screenRect = self.desktop.screenGeometry()
    self.height = self.screenRect.height()
    self.width = self.screenRect.width()

    self.ditu1 = 'world'
    self.ditu2 = ''

    self.knowledge = {'world': '全世界共有七大洲和四大洋',
                      'china': '中国共有56各民族',
                      '北京': '北京是中国的首都',
                      '美国': ''}
    super().__init__()
    self.initUI()

  def initUI(self):
    # 将整个窗口分割成3个部分
    choice_frame = QFrame(self)
    choice_frame.setFrameShape(QFrame.StyledPanel)
    knowledge_frame = QFrame(self)
    knowledge_frame.setFrameShape(QFrame.StyledPanel)
    show_frame = QFrame(self)
    show_frame.setFrameShape(QFrame.StyledPanel)

    splitter1 = QSplitter(Qt.Vertical)
    splitter1.addWidget(choice_frame)
    splitter1.addWidget(knowledge_frame)

    splitter2 = QSplitter(Qt.Horizontal)
    splitter2.addWidget(splitter1)
    splitter2.addWidget(show_frame)

    self.setCentralWidget(splitter2)

    choice_grid = QGridLayout()
    choice_grid.setSpacing(10)

    ## 选择方式1
    choice1_label = QLabel('地图显示选择')
    choice1 = QComboBox(self)
    choice1.addItem('world')
    choice1.addItem('china')
    choice1.addItem('美国')
    choice1.addItem('日本')
    choice1.addItem('加拿大')
    choice1.addItem('北京')
    choice1.addItem('上海')
    choice1.addItem('山西')
    choice1.activated[str].connect(self.ditu1_Changed)
    button1 = QPushButton('显示', self)
    button1.clicked.connect(self.button1_action)
    choice_grid.addWidget(choice1_label, 0, 0)
    choice_grid.addWidget(choice1, 0, 1)
    choice_grid.addWidget(button1, 0, 2)
    choice_frame.setLayout(choice_grid)

    knowledge_grid =QGridLayout()
    self.knowledge_label = QLabel('')
    knowledge_grid.addWidget(self.knowledge_label)

    self.map_grid = QGridLayout()
    self.browser = QWebEngineView()
    self.map_grid.addWidget(self.browser)
    # self.browser.load(QUrl(QFileInfo("./map.html").absoluteFilePath()))
    self.browser.load(QUrl('www.baidu.com'))
    show_frame.setLayout(self.map_grid)

    self.setGeometry(self.width/4, self.height/4, self.width/2, self.height/2)
    self.setWindowTitle('地理地图')

  def ditu1_Changed(self, text):
    self.ditu1 = text

  def button1_action(self):
    print(self.ditu1)
    self.get_ditu(self.ditu1)

  def get_ditu(self, text):
    # world_map = folium.Map(location=[39.93, 116.40], zoom_start=10)
    # world_map.save("map.html")
    # webbrowser.open('map.html')

    # self.browser.load(QUrl(QFileInfo('./map.html').absoluteFilePath()))
    self.browser.load(QUrl('www.baidu.com'))
    if text in self.knowledge:
      self.knowledge_label.setText(self.knowledge[text])
    else:
      self.knowledge_label.setText('')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Main_Window()
  window.show()
  sys.exit(app.exec_())
