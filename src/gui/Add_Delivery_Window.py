from PySide2.QtWidgets import QMainWindow
from src.gui.ui_gen_mods.ui_add_delivery_window import Ui_Add_Delivery_Window
from src.db.DB_contoller import DB_controller

class Add_Delivery_Window(QMainWindow):
    def __init__(self, db_controller : DB_controller, parent = None):
        super().__init__(parent)
        self.ui = Ui_Add_Delivery_Window()
        self.ui.setupUi(self)
        self.db_controller = db_controller


