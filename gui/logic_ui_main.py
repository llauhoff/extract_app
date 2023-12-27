import sys, cv2, os
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw
from gui.ui_main import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mwin = Ui_MainWindow()
        self.mwin.setupUi(self)

        self.mwin.logo.hide()
        self.mwin.go_btn.setDisabled(True)

        self.mwin.exitBtn.clicked.connect(self._close)
        self.mwin.minBtn.clicked.connect(self.minimize)
        self.mwin.titleFrame.mouseMoveEvent = self.MoveWindow
        self.mwin.search_btn.clicked.connect(self._search)
        self.mwin.go_btn.clicked.connect(self.thread_go)

    def _close(self):
        sys.exit(0)

    def minimize(self):
        self.showMinimized()

    def _search(self):
        global video_file
        video_file = qtw.QFileDialog.getOpenFileName()
        self.mwin.lineEdit.setText(video_file[0])
        self.mwin.go_btn.setEnabled(True)

    def thread_go(self):
        global dest
        dest = qtw.QFileDialog.getExistingDirectory()
        self.worker = WorkerThread()
        self.worker.start()
        self.mwin.logo.setVisible(True)
        self.worker.finished.connect(self.thread_done)

    def thread_done(self):
        self.mwin.logo.hide()
        self.mwin.lineEdit.setText("")
        self.mwin.go_btn.setDisabled(True)

    def MoveWindow(self, event):
        if event.buttons() == qtc.Qt.MouseButton.LeftButton:
            self.move(
                self.pos() + event.globalPosition().toPoint() - self.clickPosition
            )
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()


class WorkerThread(qtc.QThread):
    def run(self):
        log = []
        video = video_file[0]
        count = 0
        vidcap = cv2.VideoCapture(video)
        success = True

        while success:
            success, image = vidcap.read()
            if count % 4 == 0:
                cv2.imwrite(
                    dest
                    + "\\%s_frame%d.jpg" % (os.path.basename(video[0][:-4]), count),
                    image,
                )
                log.append(
                    dest + "\\%s_frame%d.jpg" % (os.path.basename(video[0][:-4]), count)
                )
            count += 1
        for i in log:
            print(i)

