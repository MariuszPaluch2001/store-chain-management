from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from src.gui.ui_gen_mods.ui_info_window import Ui_Info_Window
from src.db.DB_contoller import DB_controller

class Info_Window(QMainWindow):
    def __init__(self, db_controller : DB_controller, parent = None):
        super().__init__(parent)
        self.ui = Ui_Info_Window()
        self.ui.setupUi(self)
        self.db_controller = db_controller
        self.__load_data()
        self.ui.Refresh_Button.clicked.connect(self.__load_data)

    def __load_data(self):
        self.ui.Query_Table.setRowCount(0)
        res = self.db_controller.db.get_collection("product_delivery").aggregate([{
                "$lookup": {
                "from": "product",
                "localField": "Product_id",
                "foreignField": "_id",
                "as": "product"
                }
            },
            {
                "$lookup": {
                "from": "store",
                "localField": "Store_id",
                "foreignField": "_id",
                "as": "store"
                }
            },

        ]
        )
        for r in res:
            pr_dev_amount = str(r["Amount"])
            pr_del_time = str(r["Delivery_Date"])
            pr_exp_time = str(r["Expiration_Date"])
            pr_name = r["product"][0]["Name"]
            pr_store_name= r["store"][0]["Name"]
            rowPosition = self.ui.Query_Table.rowCount()
            self.ui.Query_Table.insertRow(rowPosition)
            self.ui.Query_Table.setItem(rowPosition , 0, QTableWidgetItem(pr_name))
            self.ui.Query_Table.setItem(rowPosition , 1, QTableWidgetItem(pr_dev_amount))
            self.ui.Query_Table.setItem(rowPosition , 2, QTableWidgetItem(pr_del_time))
            self.ui.Query_Table.setItem(rowPosition , 3, QTableWidgetItem(pr_exp_time))
            self.ui.Query_Table.setItem(rowPosition , 4, QTableWidgetItem(pr_store_name))