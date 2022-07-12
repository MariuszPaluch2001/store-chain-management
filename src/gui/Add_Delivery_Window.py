from PySide2.QtWidgets import QMainWindow

class Add_Delivery_Window(QMainWindow):
    def __init__(self, db_controller ,parent = None):
        super().__init__(parent)