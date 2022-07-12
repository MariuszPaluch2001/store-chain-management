from PySide2.QtWidgets import QMainWindow
from ui_main_window import Ui_MainWindow

class Main_Window(QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui = self.ui.setupUi(self)