from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QMovie,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 440)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.btnFrame = QFrame(MainWindow)
        self.btnFrame.setObjectName("btnFrame")
        self.btnFrame.setGeometry(QRect(370, 20, 150, 60))
        self.btnFrame.setStyleSheet(
            "#btnFrame {\n"
            "	background-color: rgb(70, 70, 70);\n"
            "	border-top-right-radius: 10px;\n"
            "}"
        )

        self.exitBtn = QPushButton(self.btnFrame)
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.setGeometry(QRect(114, 19, 18, 18))
        self.exitBtn.setStyleSheet(
            "#exitBtn {\n"
            "	background-color: rgb(255, 218, 6);\n"
            "	border-radius: 5px;\n"
            "}\n"
            "#exitBtn:hover:!pressed {\n"
            "	background-color: rgb(255, 7, 7);\n"
            "}"
        )

        self.minBtn = QPushButton(self.btnFrame)
        self.minBtn.setObjectName("minBtn")
        self.minBtn.setGeometry(QRect(78, 19, 18, 18))
        self.minBtn.setStyleSheet(
            "#minBtn {\n"
            "	background-color: rgb(255, 255, 255);\n"
            "	border-radius: 5px;\n"
            "}\n"
            "#minBtn:hover:!pressed {\n"
            "	background-color: rgba(255, 255, 255, 150);\n"
            "}"
        )

        self.titleFrame = QFrame(MainWindow)
        self.titleFrame.setObjectName("titleFrame")
        self.titleFrame.setGeometry(QRect(20, 20, 400, 60))
        self.titleFrame.setStyleSheet(
            "#titleFrame {\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border-top-left-radius: 10px;\n"
            "	border-top-right-radius: 40px;\n"
            "}"
        )

        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setGeometry(QRect(10, 10, 280, 40))
        self.titleLabel.setStyleSheet(
            "#titleLabel {\n"
            "	color: rgb(255, 255, 255);\n"
            '	font: bold 36pt "Dubai";\n'
            "}"
        )

        self.accentFrame = QFrame(MainWindow)
        self.accentFrame.setObjectName("accentFrame")
        self.accentFrame.setGeometry(QRect(20, 75, 500, 10))
        self.accentFrame.setStyleSheet(
            "#accentFrame {\n"
            "	background-color: rgb(255, 218, 6);\n"
            "	border-top-right-radius: 5px;\n"
            "	border-top-left-radius: 5px;\n"
            "}"
        )

        self.mainFrame = QFrame(MainWindow)
        self.mainFrame.setObjectName("mainFrame")
        self.mainFrame.setGeometry(QRect(20, 80, 500, 340))
        self.mainFrame.setStyleSheet(
            "#mainFrame {\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-top-left-radius: 5px;\n"
            "	border-top-right-radius: 5px;\n"
            "	border-bottom-left-radius: 10px;\n"
            "	border-bottom-right-radius: 10px;\n"
            "}"
        )

        self.search_btn = QPushButton(self.mainFrame)
        self.search_btn.setObjectName("search_btn")
        self.search_btn.setGeometry(QRect(40, 40, 50, 50))
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_btn.setStyleSheet(
            "#search_btn {\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "	border-right: 1px solid rgb(70, 70, 70);\n"
            "	border-top-left-radius: 10px;\n"
            "	border-bottom-left-radius: 10px;\n"
            "	color: white;\n"
            '	font: bold 30pt "Dubai";\n'
            "}\n"
            "#search_btn:hover:!pressed {\n"
            "	border: 2px solid rgb(255, 218, 6);\n"
            "}\n"
            "#search_btn:pressed {\n"
            '	font: bold 29pt "Dubai";\n'
            "}"
        )

        self.lineEdit = QLineEdit(self.mainFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(90, 40, 360, 50))
        self.lineEdit.setStyleSheet(
            "#lineEdit {\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border-top: 2px solid rgb(70, 70, 70);\n"
            "	border-top-right-radius: 10px;\n"
            "	border-bottom-right-radius: 10px;\n"
            "	border-right: 2px solid rgb(70, 70, 70);\n"
            "	border-left: 1px solid rgb(70, 70, 70);\n"
            "	border-bottom: 2px solid rgb(70, 70, 70);\n"
            "	color: white;\n"
            '	font: bold 18pt "Dubai";\n'
            "}"
        )

        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(True)

        self.go_btn = QPushButton(self.mainFrame)
        self.go_btn.setObjectName("go_btn")
        self.go_btn.setGeometry(QRect(100, 175, 300, 50))
        self.go_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.go_btn.setStyleSheet(
            "#go_btn {\n"
            "	background-color: rgb(30, 30, 30);\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "	color: white;\n"
            '	font: bold 32pt "Dubai";\n'
            "	border-radius: 10px;\n"
            "}\n"
            "#go_btn:hover:!pressed {\n"
            "	border: 2px solid rgb(255, 218, 6);\n"
            "}\n"
            "#go_btn:pressed {\n"
            '	font: bold 31pt "Dubai";\n'
            "}"
        )

        self.logo = QLabel(self.mainFrame)
        self.logo.setGeometry(QRect(0, 0, 500, 340))
        self.logo_movie = QMovie(r"C:\Users\Lane\Desktop\app\gui\logo.gif")
        self.logo.setMovie(self.logo_movie)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo_movie.start()
        self.logo.setStyleSheet("background-color: rgba(0, 0, 0, 180);")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Extraction", None)
        )
        # if QT_CONFIG(tooltip)
        self.exitBtn.setToolTip(QCoreApplication.translate("MainWindow", "Exit", None))
        # endif // QT_CONFIG(tooltip)
        self.exitBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.minBtn.setToolTip(
            QCoreApplication.translate("MainWindow", "Minimize", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.minBtn.setText("")
        self.titleLabel.setText(
            QCoreApplication.translate("MainWindow", "EXTRACTION", None)
        )
        self.search_btn.setText(QCoreApplication.translate("MainWindow", "S", None))
        self.go_btn.setText(QCoreApplication.translate("MainWindow", "EXTRACT", None))

    # retranslateUi
