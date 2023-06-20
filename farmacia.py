import json
from productos import (
    cargar_productos,
    guardar_productos,
    ingresar_producto,
    modificar_producto,
    eliminar_producto,
    mostrar_reportes
)

def guardar_usuarios(usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo)

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def crear_usuario():
    usuarios = cargar_usuarios()
    nombre_usuario = input('Ingrese su nombre de usuario: ')
    if nombre_usuario in usuarios:
        print('El nombre de usuario ya existe. ❗❗❗')
        return
    contrasena = input('Ingrese su contraseña: ')
    usuarios[nombre_usuario] = contrasena
    guardar_usuarios(usuarios)
    print('Usuario creado. ✔ ')

def iniciar_sesion():
    usuarios = cargar_usuarios()
    nombre_usuario = input('Ingrese su nombre de usuario: ')
    if nombre_usuario not in usuarios:
        print('El nombre de usuario no existe.')
        return False
    contrasena = input('Ingrese su contraseña: ')
    if contrasena == usuarios[nombre_usuario]:
        print('Inicio de sesión correcto.')
        return True
    else:
        print('Contraseña incorrecta. ❗❗❗')
        return False
    
def pantalla_inicio():
    while True:
        print('*** LOGIN ****')

        print('[1] Crear usuario')
        print('[2] Iniciar sesión')

        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                crear_usuario()
            case 2:
                if iniciar_sesion():
                    menu()
            case other:
                print("Error!  ❌ Ingrese una opción válida.")

def mostrar_reportes(productos):
    while True:
        print('*** REPORTES DE PRODUCTOS ****')

        print('[1] Mostrar todos los productos')
        print('[2] Buscar por nombre')
        print('[3] Buscar por marca')
        print('[0] Atrás')

        opcion_str = input('Ingrese una opción: ')
        if not opcion_str.isdigit():
            print("Error! ❌ Ingrese una opción válida.")
            continue
        opcion = int(opcion_str)
        match opcion:
            case 1:
                for codigo, producto in productos.items():
                    print(f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                    print()
            case 2:
                palabra_clave = input('Ingrese la palabra clave a buscar en el nombre del producto: ')
                encontrado = False
                for codigo, producto in productos.items():
                    if palabra_clave in producto['nombre']:
                        encontrado = True
                        print(f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                        print()
                if not encontrado:
                    print(f'No se encontraron productos que contengan "{palabra_clave}" en su nombre.')
            case 3:
                palabra_clave = input('Ingrese la palabra clave a buscar en la marca del producto: ')
                encontrado = False
                for codigo, producto in productos.items():
                    if palabra_clave in producto['marca']:
                        encontrado = True
                        print(f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                        print()
                if not encontrado:
                    print(f'No se encontraron productos que contengan "{palabra_clave}" en su marca.')
            case 0:
                menu()
            case other:
                print("Error! ❌ Ingrese una opción válida.")

def menu_productos(menu):
    print('*** GESTIÓN DE PRODUCTOS ****')

    productos = cargar_productos()
    contador = max([int(id) for id in productos.keys()], default=0) + 1
    while True:
        print('[1] Agregar producto')
        print('[2] Modificar producto')
        print('[3] Eliminar producto')
        print('[4] Reportes')
        print('[0] Atrás')
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                contador = ingresar_producto(productos, contador)
            case 2:
                modificar_producto(productos, menu)
            case 3:
                eliminar_producto(productos)
            case 4:
                mostrar_reportes(productos)
            case 0:
                menu()
            case other:
                print("Error! ❌ Ingrese una opción válida.")

def menu():
    productos = cargar_productos()  # Cargar los productos aquí para que estén disponibles en todo el alcance de menu()

    while True:
        print('**** MENÚ PRINCIPAL ****')

        print('[1] Gestión de productos')
        print('[2] Reportes')
        print('[0] Salir')

        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                menu_productos(menu)
            case 2:
                mostrar_reportes(productos)  # Pasar la variable 'productos' como argumento a mostrar_reportes()
            case 0:
                pantalla_inicio()
            case other:
                print("Error!  ❌ Ingrese una opción válida.")

