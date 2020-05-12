import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.msh = int(input('Уровень маштабирования(от 0 до 17):'))
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.hbox = QHBoxLayout(self)
        self.coords = [37.530887, 55.703118]
        self.setLayout(self.hbox)
        self.lbl = QLabel(self)
        self.show_image()

    def closeEvent(self, event):
        os.remove(self.map_file)

    def show_image(self):
        self.map_file = "map.png"
        response = requests.get(
            f"http://static-maps.yandex.ru/1.x/?ll={self.coords[0]},{self.coords[1]}&z={self.msh}&l=map")
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        if self.lbl is not None:
            self.hbox.removeWidget(self.lbl)
        pixmap = QPixmap(self.map_file)
        self.lbl.setPixmap(pixmap)
        self.hbox.addWidget(self.lbl)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.msh > 1:
                self.msh -= 1
        if event.key() == Qt.Key_PageDown:
            if self.msh < 14:
                self.msh += 1
        if event.key() == Qt.Key_Up:
            self.coords[1] += (15 - self.msh) / (5 * self.msh)
        if event.key() == Qt.Key_Down:
            self.coords[1] -= (15 - self.msh) / (5 * self.msh)
        if event.key() == Qt.Key_Left:
            self.coords[0] -= (15 - self.msh) / (5 * self.msh)
        if event.key() == Qt.Key_Right:
            self.coords[0] += (15 - self.msh) / (5 * self.msh)
        self.show_image()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
