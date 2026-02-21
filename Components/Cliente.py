from Components.Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, dni, email, telefono):
        super().__init__(nombre)
        self.dni = dni
        self.email = email
        self.telefono = telefono