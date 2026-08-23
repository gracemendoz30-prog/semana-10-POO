from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


def guardar_cambios(restaurante):
    if ArchivoServicio.guardar_productos(restaurante.listar_productos()):
        print("Cambios guardados correctamente")
    else:
        print("No se pudieron guardar los cambios")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un numero valido")


def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El precio debe ser mayor a cero")
                continue
            return valor
        except ValueError:
            print("Ingresa un numero valido")


def main():
    print("Cargando productos...")
    lista = ArchivoServicio.cargar_productos()

    restaurante = Restaurante()
    restaurante.establecer_productos(lista)
    print(f"Se cargaron {len(lista)} productos")

    while True:
        print("\n===== MENU =====")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Cambiar disponibilidad")
        print("0. Salir")

        opcion = leer_entero("Elige una opcion: ")

        if opcion == 1:
            nombre = input("Nombre: ")
            precio = leer_precio("Precio: ")
            categoria = input("Categoria: ")
            try:
                restaurante.registrar_producto(nombre, precio, categoria)
                print("Producto registrado")
                guardar_cambios(restaurante)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == 2:
            print("\nLista de productos:")
            todos = restaurante.listar_productos()
            if not todos:
                print("No hay productos")
            else:
                for p in todos:
                    print(p)

        elif opcion == 3:
            nombre = input("Nombre a buscar: ")
            p = restaurante.buscar_producto(nombre)
            if p:
                print(f"Encontrado: {p}")
            else:
                print("No encontrado")

        elif opcion == 4:
            actual = input("Nombre actual: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = leer_precio("Nuevo precio: ")
            nueva_cat = input("Nueva categoria: ")
            if restaurante.actualizar_producto(actual, nuevo_nombre, nuevo_precio, nueva_cat):
                print("Producto actualizado")
                guardar_cambios(restaurante)
            else:
                print("No encontrado")

        elif opcion == 5:
            nombre = input("Nombre a eliminar: ")
            if restaurante.eliminar_producto(nombre):
                print("Producto eliminado")
                guardar_cambios(restaurante)
            else:
                print("No encontrado")

        elif opcion == 6:
            nombre = input("Nombre del producto: ")
            if restaurante.cambiar_disponibilidad(nombre):
                print("Disponibilidad cambiada")
                guardar_cambios(restaurante)
            else:
                print("No encontrado")

        elif opcion == 0:
            print("Saliendo...")
            break

        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()