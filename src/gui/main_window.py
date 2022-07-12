from PySide2.QtWidgets import QMainWindow, QApplication
from src.gui.ui_main_window import Ui_MainWindow
from src.gui.Add_Product_Window import Add_Product_Window

class Main_Window(QMainWindow):
    def __init__(self, db_controller, parent = None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__set_buttons()

        self.db_controller = db_controller

    def __add_product_window(self):
        window = Add_Product_Window(self.db_controller, self)
        window.show()

    def __add_delivery_window(self):
        print("Add delivery")
    
    def __info_prouct_window(self):
        print("Info product")

    def __set_buttons(self):
        self.ui.Exit_Button.clicked.connect(exit)
        self.ui.Add_Product_Button.clicked.connect(self.__add_product_window)
        self.ui.Add_Delivery_Button.clicked.connect(self.__add_delivery_window)
        self.ui.Info_Product_Button.clicked.connect(self.__info_prouct_window)