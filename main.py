from src.gui.main_window import Main_Window
from PySide2.QtWidgets import QApplication
def main():
    app = QApplication()
    window = Main_Window()
    window.show()

    return app.exec_()

if __name__ == "__main__":
    main()