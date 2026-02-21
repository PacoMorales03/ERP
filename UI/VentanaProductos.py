from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem
)
from Components.Producto import Producto
from Data.Datos import productos


class VentanaProductos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Productos")
        self.setMinimumSize(600, 400)

        self.setStyleSheet("""
            QWidget { background-color: #ffffff; font-family: Arial; }
            QPushButton {
                background-color: #ff9800;
                color: white;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #e68900; }
        """)

        layout_principal = QVBoxLayout()
        form_layout = QHBoxLayout()

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre")

        self.input_precio = QLineEdit()
        self.input_precio.setPlaceholderText("Precio")

        self.input_stock = QLineEdit()
        self.input_stock.setPlaceholderText("Stock")

        form_layout.addWidget(self.input_nombre)
        form_layout.addWidget(self.input_precio)
        form_layout.addWidget(self.input_stock)

        self.b_guardar = QPushButton("Guardar Producto")

        # TABLA
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Precio (€)", "Stock"])
        self.tabla.horizontalHeader().setStretchLastSection(True)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(self.b_guardar)
        layout_principal.addWidget(self.tabla)

        self.setLayout(layout_principal)

        self.b_guardar.clicked.connect(self.guardar_producto)
        self.actualizar_tabla()

    def guardar_producto(self):
        nombre = self.input_nombre.text()

        try:
            precio = float(self.input_precio.text())
            if precio <= 0:
                raise ValueError
        except:
            QMessageBox.warning(self, "Error", "Precio inválido")
            return

        try:
            stock = int(self.input_stock.text())
            if stock < 0:
                raise ValueError
        except:
            QMessageBox.warning(self, "Error", "Stock inválido")
            return

        productos.append(Producto(nombre, precio, stock))

        QMessageBox.information(self, "Correcto", "Producto guardado")

        self.input_nombre.clear()
        self.input_precio.clear()
        self.input_stock.clear()

        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(len(productos))

        for fila, producto in enumerate(productos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(producto.nombre))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(producto.precio)))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(producto.stock)))