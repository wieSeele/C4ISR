import sys
import os
import folium
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

## 采用高德地图
Map = folium.Map(location=[34.2634, 109.0432],
                zoom_start=16,
                control_scale=True,
                tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
                attr='default')

# 鼠标点击显示经纬度
Map.add_child(folium.LatLngPopup())
Map.add_child(folium.ClickForMarker(popup='Waypoint'))

# 标记一个实心圆
folium.CircleMarker(
  location=[34.2634, 109.0432],
  radius=1,
  popup='popup',
  color='#DC143C',
  fill=True,
  fill_color='#6495E').add_to(Map)


Map.save('map.html')


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle('地图显示')
    self.resize(1000, 640)
    self.browser = QWebEngineView(self)
    self.browser.setGeometry(20,20,960,600)

    path = "file:\\" + os.getcwd() + "\\map.html"
    path = path.replace('\\', '/')
    print(path)
    self.browser.load(QUrl(path))

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = MainWindow()
  win.show()
  app.exit(app.exec_())