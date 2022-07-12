from PySide2.QtWidgets import QMainWindow
from src.gui.ui_gen_mods.ui_add_product_window import Ui_Add_Product
from src.db.DB_contoller import DB_controller

class Add_Product_Window(QMainWindow):
    def __init__(self, db_controller : DB_controller, parent = None):
        super().__init__(parent)
        self.ui = Ui_Add_Product()
        self.ui.setupUi(self)
        self.db_controller = db_controller
        self.__Producent_Name_Load()
        self.ui.Insert_Button.clicked.connect(self.__Insert_Data)

    def __Producent_Name_Load(self):
        producents = self.db_controller.db.get_collection("producent").find({}, {"Name":1, "_id":0})
        producents_list = [producent["Name"] for producent in producents]
        self.ui.Producent_Names_Combo.addItems(producents_list)

    def __Insert_Data(self):
        product_name = self.ui.Product_Name_Input.text()
        mass = self.ui.Product_Mass_Input.text()
        mass_unit = self.ui.Product_Mass_Unit_Input.text()
        description = self.ui.Product_Description_Input.toPlainText()
        tin = self.ui.Producent_TIN_Input.text()

        if not tin:
            producent_name = self.ui.Producent_Names_Combo.currentText()
            producent_id = self.db_controller.db.get_collection("producent").find_one(
                { "Name": { "$eq": producent_name } }, 
                { "_id" : 1}
            )
        else:
            producent_id = self.db_controller.db.get_collection("producent").find_one(
                { "TIN": { "$eq": tin } }, 
                { "_id" : 1}
            )

        product = {
            "Name": product_name,
            "Mass": int(mass),
            "Mass_Unit": mass_unit,
            "Description": description,
            "Producent_ID" :  producent_id["_id"]
        }

        self.db_controller.crud.insert("product", product)

        self.__clear_data()

    def __clear_data(self):
        self.ui.Product_Name_Input.clear()
        self.ui.Product_Mass_Input.clear()
        self.ui.Product_Mass_Unit_Input.clear()
        self.ui.Product_Description_Input.clear()
        self.ui.Producent_TIN_Input.clear()
