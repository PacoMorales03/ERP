from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox,
    QComboBox, QSpinBox,
    QTableWidget, QTableWidgetItem
)
from Components.Pedidio import Pedido
from Data.Datos import clientes, productos, pedidos


class VentanaPedidos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Pedidos")
        self.setMinimumSize(700, 400)

        self.setStyleSheet("""
            QWidget { background-color: #ffffff; font-family: Arial; }
            QPushButton {
                background-color: #17a2b8;
                color: white;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #138496; }
        """)

        layout_principal = QVBoxLayout()
        form_layout = QHBoxLayout()

        self.combo_cliente = QComboBox()
        self.combo_producto = QComboBox()

        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setMinimum(1)
        self.spin_cantidad.setMaximum(1000)

        form_layout.addWidget(self.combo_cliente)
        form_layout.addWidget(self.combo_producto)
        form_layout.addWidget(self.spin_cantidad)

        self.b_crear = QPushButton("Crear Pedido")

        # TABLA
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(
            ["Cliente", "Producto", "Cantidad", "Total (€)"]
        )

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(self.b_crear)
        layout_principal.addWidget(self.tabla)

        self.setLayout(layout_principal)

        self.b_crear.clicked.connect(self.crear_pedido)

        self.cargar_datos()
        self.actualizar_tabla()

    def cargar_datos(self):
        self.combo_cliente.clear()
        self.combo_producto.clear()

        for c in clientes:
            self.combo_cliente.addItem(c.nombre)

        for p in productos:
            self.combo_producto.addItem(p.nombre)

    def crear_pedido(self):
        if not clientes or not productos:
            QMessageBox.warning(self, "Error", "Debe haber clientes y productos")
            return

        cliente = clientes[self.combo_cliente.currentIndex()]
        producto = productos[self.combo_producto.currentIndex()]
        cantidad = self.spin_cantidad.value()

        if producto.stock < cantidad:
            QMessageBox.warning(self, "Error", "Stock insuficiente")
            return

        producto.stock -= cantidad

        nuevo_pedido = Pedido(cliente, producto, cantidad)
        pedidos.append(nuevo_pedido)

        QMessageBox.information(
            self, "Correcto",
            f"Pedido creado. Total: {nuevo_pedido.total} €"
        )

        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(len(pedidos))

        for fila, p in enumerate(pedidos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(p.cliente.nombre))
            self.tabla.setItem(fila, 1, QTableWidgetItem(p.producto.nombre))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(p.cantidad)))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(p.total)))