from PySide2.QtWidgets import QMainWindow
from src.gui.ui_gen_mods.ui_info_window import Ui_Info_Window
class Info_Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)