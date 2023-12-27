import sys
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw
from logic.logic_ui_main import MainWindow


class MainApp(qtw.QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.mwin = MainWindow()
        self.mwin.show()


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec())
