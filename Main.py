import sys
from PyQt5.QtWidgets import QApplication
from Data.Datos import cargar_datos
from UI.PanelPrincipal import PanelPrincipal

if __name__ == "__main__":
    # LLamada a la función main que carga los datos de un xml
    cargar_datos()
    # Se abre la ventana del panel principal
    app = QApplication(sys.argv) 
    ventana = PanelPrincipal()
    ventana.show()
    sys.exit(app.exec_())