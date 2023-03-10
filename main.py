import os, sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from py_components.resorces import Resources



APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")
POPUP_QML = os.path.join(APP_ROOT, "popup.qml")
QQuickStyle.setStyle("Material")

class TMDB:
    def __init__(self):
        # instance of QGuiApplication
        self.app = QGuiApplication(sys.argv)

        # instance QQmlApplicationEngine egy példány kell hogy el tudjon indulni az ablak
        self.engine = QQmlApplicationEngine()

        # get rootContext

        self.context = self.engine.rootContext()

        # insert my python object into QML context

        self.resources = Resources()
        self.context.setContextProperty("Resources", self.resources)


        #load main.qml
        self.engine.load(MAIN_QML)

        if not self.engine.rootObjects:
            sys.exit(-1)
        #hold window open till user click close button
        sys.exit(self.app.exec())


if __name__ == "__main__":
    TMDB()


