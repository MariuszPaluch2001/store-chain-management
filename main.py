from src.gui.main_window import Main_Window
from src.db.DB_contoller import DB_controller
from PySide2.QtWidgets import QApplication
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os

def main():
    load_dotenv(find_dotenv())
    password = os.environ.get("MONGODB_PWD")
    connect_str = f"""mongodb+srv://mariuszpaluch:{password}@myprojects.z9jwiv9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"""    
    client = MongoClient(connect_str)
    db = DB_controller(client.production)



    app = QApplication()
    window = Main_Window(db)
    window.show()

    return app.exec_()

if __name__ == "__main__":
    main()