from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from Components.Cliente import Cliente
from Data.Datos import clientes


class VentanaClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Clientes")
        self.setMinimumSize(600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: Arial;
            }
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QLineEdit {
                padding: 5px;
            }
        """)

        layout_principal = QVBoxLayout()

        form_layout = QHBoxLayout()

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre")

        self.input_dni = QLineEdit()
        self.input_dni.setPlaceholderText("DNI")

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Email")

        self.input_telefono = QLineEdit()
        self.input_telefono.setPlaceholderText("Teléfono")

        form_layout.addWidget(self.input_nombre)
        form_layout.addWidget(self.input_dni)
        form_layout.addWidget(self.input_email)
        form_layout.addWidget(self.input_telefono)

        self.b_guardar = QPushButton("Guardar Cliente")

        # TABLA
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(
            ["Nombre", "DNI", "Email", "Teléfono"]
        )
        self.tabla.horizontalHeader().setStretchLastSection(True)

        layout_principal.addLayout(form_layout)
        layout_principal.addWidget(self.b_guardar)
        layout_principal.addWidget(self.tabla)

        self.setLayout(layout_principal)

        self.b_guardar.clicked.connect(self.guardar_cliente)

        self.actualizar_tabla()

    def guardar_cliente(self):
        nombre = self.input_nombre.text()
        dni = self.input_dni.text()
        email = self.input_email.text()
        telefono = self.input_telefono.text()

        if dni == "":
            QMessageBox.warning(self, "Error", "El DNI no puede estar vacío")
            return

        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Error", "Email inválido")
            return

        for c in clientes:
            if c.dni == dni:
                QMessageBox.warning(self, "Error", "Cliente ya existe")
                return

        nuevo_cliente = Cliente(nombre, dni, email, telefono)
        clientes.append(nuevo_cliente)

        QMessageBox.information(self, "Correcto", "Cliente guardado")

        self.input_nombre.clear()
        self.input_dni.clear()
        self.input_email.clear()
        self.input_telefono.clear()

        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(len(clientes))

        for fila, cliente in enumerate(clientes):
            self.tabla.setItem(fila, 0, QTableWidgetItem(cliente.nombre))
            self.tabla.setItem(fila, 1, QTableWidgetItem(cliente.dni))
            self.tabla.setItem(fila, 2, QTableWidgetItem(cliente.email))
            self.tabla.setItem(fila, 3, QTableWidgetItem(cliente.telefono))