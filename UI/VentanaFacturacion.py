from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QLabel, QTableWidget, QTableWidgetItem
)
from Data.Datos import pedidos


class VentanaFacturacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Facturación")
        self.setMinimumSize(700, 400)

        layout = QVBoxLayout()

        self.label_total = QLabel()
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(
            ["Cliente", "Total Facturado (€)"]
        )

        layout.addWidget(self.label_total)
        layout.addWidget(self.tabla)

        self.setLayout(layout)

        self.calcular_facturacion()

    def calcular_facturacion(self):
        total_general = 0
        facturacion_cliente = {}

        for p in pedidos:
            total_general += p.total

            if p.cliente.nombre not in facturacion_cliente:
                facturacion_cliente[p.cliente.nombre] = 0

            facturacion_cliente[p.cliente.nombre] += p.total

        self.label_total.setText(
            f"<h2>Total Facturado: {total_general} €</h2>"
        )

        self.tabla.setRowCount(len(facturacion_cliente))

        for fila, (cliente, total) in enumerate(facturacion_cliente.items()):
            self.tabla.setItem(fila, 0, QTableWidgetItem(cliente))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(total)))