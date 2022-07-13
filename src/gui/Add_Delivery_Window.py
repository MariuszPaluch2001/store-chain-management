from PySide2.QtWidgets import QMainWindow
from src.gui.ui_gen_mods.ui_add_delivery_window import Ui_Add_Delivery_Window
from src.db.DB_contoller import DB_controller

class Add_Delivery_Window(QMainWindow):
    def __init__(self, db_controller : DB_controller, parent = None):
        super().__init__(parent)
        self.ui = Ui_Add_Delivery_Window()
        self.ui.setupUi(self)
        self.db_controller = db_controller
        self.__Product_Name_Load()
        self.__Store_Name_Load()
        self.ui.Submit_Button.clicked.connect(self.__Insert_Data)
        
    def __Product_Name_Load(self):
        producents = self.db_controller.db.get_collection("product").find({}, {"Name":1, "_id":0})
        producents_list = [producent["Name"] for producent in producents]
        self.ui.Product_Name_Combo.addItems(producents_list)

    def __Store_Name_Load(self):
        producents = self.db_controller.db.get_collection("store").find({}, {"Name":1, "_id":0})
        producents_list = [producent["Name"] for producent in producents]
        self.ui.Store_Name_Combo.addItems(producents_list)


    def __Insert_Data(self):

        self.__clear_data()

    
    def __clear_data(self):
        self.ui.Amount_Input.clear()
        self.ui.Delivery_Date_Input.clear()
        self.ui.Expiration_Date_Input.clear()