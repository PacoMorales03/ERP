# Importa el módulo ElementTree para trabajar con archivos XML (leer, crear y modificar)
import xml.etree.ElementTree as ET


clientes = []
productos = []
pedidos = []

def guardar_datos():
    try:
        # Se define el elemento raiz
        root = ET.Element("ERP")

        # CLIENTES
        clientes_xml = ET.SubElement(root, "Clientes")
        # Se crea un elemento Cliente con sus subelementos correspondientes para cada objeto cliente en la lista
        for c in clientes:
            cliente_xml = ET.SubElement(clientes_xml, "Cliente")
            ET.SubElement(cliente_xml, "Nombre").text = c.nombre
            ET.SubElement(cliente_xml, "DNI").text = c.dni
            ET.SubElement(cliente_xml, "Email").text = c.email
            ET.SubElement(cliente_xml, "Telefono").text = c.telefono

        # PRODUCTOS
        productos_xml = ET.SubElement(root, "Productos")
        for p in productos:
            producto_xml = ET.SubElement(productos_xml, "Producto")
            ET.SubElement(producto_xml, "Nombre").text = p.nombre
            ET.SubElement(producto_xml, "Precio").text = str(p.precio)
            ET.SubElement(producto_xml, "Stock").text = str(p.stock)

        # PEDIDOS
        pedidos_xml = ET.SubElement(root, "Pedidos")
        for ped in pedidos:
            pedido_xml = ET.SubElement(pedidos_xml, "Pedido")
            ET.SubElement(pedido_xml, "Cliente").text = ped.cliente.nombre
            ET.SubElement(pedido_xml, "Producto").text = ped.producto.nombre
            ET.SubElement(pedido_xml, "Cantidad").text = str(ped.cantidad)
            ET.SubElement(pedido_xml, "Total").text = str(ped.total)
        # Crea el árbol XML completo a partir del nodo raíz
        tree = ET.ElementTree(root)
        # Se crea el archivo datos.xml
        tree.write("datos.xml", encoding="utf-8", xml_declaration=True)

    except Exception as e:
        print("Error guardando XML:", e)


def cargar_datos():
    try:
        from Components.Cliente import Cliente
        from Components.Producto import Producto
        from Components.Pedidio import Pedido

        # Busca el archivo datos.xml
        tree = ET.parse("datos.xml")
        root = tree.getroot()

        # Se limpian las listas
        clientes.clear()
        productos.clear()
        pedidos.clear()

        # Se recorren los nodos correspondientes, se van creando los objetos y posteriormente se añaden a la lista.

        # Clientes
        for c_xml in root.find("Clientes"):
            cliente = Cliente(
                c_xml.find("Nombre").text,
                c_xml.find("DNI").text,
                c_xml.find("Email").text,
                c_xml.find("Telefono").text
            )
            clientes.append(cliente)

        # Productos
        for p_xml in root.find("Productos"):
            producto = Producto(
                p_xml.find("Nombre").text,
                float(p_xml.find("Precio").text),
                int(p_xml.find("Stock").text)
            )
            productos.append(producto)

        # Pedidos
        for ped_xml in root.find("Pedidos"):
            nombre_cliente = ped_xml.find("Cliente").text
            nombre_producto = ped_xml.find("Producto").text
            cantidad = int(ped_xml.find("Cantidad").text)
            # Busca en la lista de clientes el objeto cuyo nombre coincida
            cliente_obj = next(c for c in clientes if c.nombre == nombre_cliente)
            # Busca en la lista de productos el objeto cuyo nombre coincida
            producto_obj = next(p for p in productos if p.nombre == nombre_producto)
            pedido = Pedido(cliente_obj, producto_obj, cantidad)
            pedidos.append(pedido)
    except FileNotFoundError:
        print("No existe archivo XML aún.")
    except Exception as e:
        print("Error cargando XML:", e)