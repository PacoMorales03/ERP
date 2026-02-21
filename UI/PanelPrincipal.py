from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout,
    QTextEdit, QLabel, QHBoxLayout, QFrame
)
from UI.VentanaClientes import VentanaClientes
from UI.VentanaProductos import VentanaProductos
from UI.VentanaPedidos import VentanaPedidos
from UI.VentanaFacturacion import VentanaFacturacion
from Data.Datos import clientes, guardar_datos, productos, pedidos

from PyQt5.QtCore import Qt


class PanelPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini ERP Empresarial")
        self.setMinimumSize(600, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f9;
                font-family: Arial;
                font-size: 14px;
            }
            QPushButton {
                background-color: #2c7be5;
                color: white;
                padding: 8px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #1a68d1;
            }
        """)

        main_layout = QVBoxLayout()

        titulo = QLabel("ERP")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        titulo.setAlignment(Qt.AlignCenter)

        botones_layout = QHBoxLayout()

        self.b_clientes = QPushButton("Clientes")
        self.b_productos = QPushButton("Productos")
        self.b_pedidos = QPushButton("Pedidos")
        self.b_facturacion = QPushButton("Facturación")

        botones_layout.addWidget(self.b_clientes)
        botones_layout.addWidget(self.b_productos)
        botones_layout.addWidget(self.b_pedidos)
        botones_layout.addWidget(self.b_facturacion)

        self.area = QTextEdit()
        self.area.setReadOnly(True)

        self.b_resumen = QPushButton("Mostrar Resumen")
        self.b_limpiar = QPushButton("Limpiar Datos")

        main_layout.addWidget(titulo)
        main_layout.addLayout(botones_layout)
        main_layout.addWidget(self.area)
        main_layout.addWidget(self.b_resumen)
        main_layout.addWidget(self.b_limpiar)

        self.setLayout(main_layout)

        self.b_clientes.clicked.connect(self.abrir_clientes)
        self.b_productos.clicked.connect(self.abrir_productos)
        self.b_pedidos.clicked.connect(self.abrir_pedidos)
        self.b_facturacion.clicked.connect(self.abrir_facturacion)
        self.b_resumen.clicked.connect(self.mostrar_resumen)
        self.b_limpiar.clicked.connect(self.limpiar_datos)

    def abrir_clientes(self):
        self.ventana = VentanaClientes()
        self.ventana.show()

    def abrir_productos(self):
        self.ventana = VentanaProductos()
        self.ventana.show()

    def abrir_pedidos(self):
        self.ventana = VentanaPedidos()
        self.ventana.show()

    def abrir_facturacion(self):
        self.ventana = VentanaFacturacion()
        self.ventana.show()

    def mostrar_resumen(self):
        texto = f"""
        RESUMEN GENERAL

        Clientes registrados: {len(clientes)}
        Productos registrados: {len(productos)}
        Pedidos realizados: {len(pedidos)}
        """
        self.area.setText(texto)

    def limpiar_datos(self):
        clientes.clear()
        productos.clear()
        pedidos.clear()
        self.area.setText("Datos eliminados correctamente.")

    def closeEvent(self, event):
        guardar_datos()
        event.accept()