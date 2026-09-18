import sys
import os

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    # Định nghĩa vị trí của các file ui
    UI_LOCATION = os.path.join("ui/main_window1.ui")
    STYLE_LOCATION = os.path.join("ui/style_main1.qss")
    def __init__(self, parent:QApplication):
        super(MainWindow, self).__init__()
        self.app = parent

        # Load file giao diện .ui và .qss
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        with open(self.STYLE_LOCATION, "r") as style_file:
            style_config = style_file.read()
        self.setStyleSheet(style_config)

        # Luôn hiển thị trang home
        self.ui.stackedWidget.setCurrentIndex(0)
        # Hiển thị cửa sổ ra màn hình
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)

    sys.exit(app.exec())
