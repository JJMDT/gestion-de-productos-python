import json

import json

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
    nombre_usuario = input('Ingrese su nombre de usuario ')
    if nombre_usuario not in usuarios:
        print ('El nombre de usuario no existe ')
        return False
    password = input('Ingrese su contraseña ')
    if password == usuarios[nombre_usuario]:
        print ('Iniciio de sesion correcto ')
        return True
    else:
        print ('Contraseña incorrecta. ❗❗❗')
        return False
    
def cargar_productos():
    try:
        with open('productos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    
def menu_productos():
    print('***GESTION DE PRODUCTOS****')

    productos = cargar_productos()
    contador = max([int(id) for id in productos.keys()], default=0) + 1
    while True:
        print('[1] Agregar producto')
        print('[2] Modificar producto')
        print('[3] Eliminar producto')
        print('[4] Reportes')
        print('[0] Atras')
        opcion = int(input('Ingrese una opcion '))
        match opcion:
          case 1:
            contador = ingresar_producto(productos, contador)
          case 2:
            modificar_producto(productos)
          case 3:
            eliminar_producto(productos)
          case 4:
            mostrar_reportes(productos)

          case 0:
            menu()
          case other:
                 print("Error! ❌ Ingrese una opcion valida")

def guardar_productos(productos):
    with open('productos.json', 'w') as archivo:
        json.dump(productos, archivo)



def ingresar_producto(productos,contador):
    id = str(contador)
    print (f'el ID para este producto es el {id}')
    nombre = input('Ingrese el nombre del producto: ')
    marca = input('Ingrese la marca del producto: ')
    presentacion = input('Ingrese la presentación del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    stock = int(input('Ingrese el stock del producto: '))
    productos[id] = {'nombre': nombre, 'marca': marca, 'presentacion': presentacion, 'precio': precio, 'stock': stock}
    guardar_productos(productos)
    print(f'Producto fue ingresado con ID {id}. ✔')
    return contador + 1

def modificar_producto(productos):
    print('*** MODIFICAR PRODUCTO ****')

    codigo = input('Ingrese el código del producto a modificar: ')
    if codigo not in productos:
        print('El código no existe.')
        return
    print('Valores actuales del producto:')
    print(f"Nombre: {productos[codigo]['nombre']}")
    print(f"Marca: {productos[codigo]['marca']}")
    print(f"Presentación: {productos[codigo]['presentacion']}")
    print(f"Precio: {productos[codigo]['precio']}")
    print(f"Stock: {productos[codigo]['stock']}")
    print()

    while True:
        print ('¿Qué desea modificar?')
        print ('[1] Nombre')
        print ('[2] Marca')
        print ('[3] Presentacion')
        print ('[4] Precio')
        print ('[5] Stock')
        print ('[6] Todo')
        print ('[0] Finalizar')
        opcion = int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
             nombre = input('Ingrese el nuevo nombre del producto: ')
             productos[codigo]['nombre'] = nombre
            case 2:
             marca = input('Ingrese la nueva marca del producto: ')
             productos[codigo]['marca']= marca
            case 3:
             presentacion = input('Ingrese la nueva presentacion del producto: ')
             productos[codigo]['presentacion'] = presentacion
            case 4:
             precio = input('Ingrese el nuevo precio: ')
             productos[codigo]['precio']= precio
            case 5:
             stock = input('Ingrese el nuevo stock: ')
             productos[codigo]['stock']=stock
            case 6:
             nombre = input('Ingrese el nuevo nombre del producto: ')
             productos[codigo]['nombre'] = nombre
             marca = input('Ingrese la nueva marca del producto: ')
             productos[codigo]['marca']= marca
             presentacion = input('Ingrese la nueva presentacion del producto: ')
             productos[codigo]['presentacion'] = presentacion
             precio = input('Ingrese el nuevo precio: ')
             productos[codigo]['precio']= precio
             stock = input('Ingrese el nuevo stock: ')
             productos[codigo]['stock']=stock
            case 0:
             menu_productos()
            case other:
                 print("Error! ❌ Ingrese una opcion valida")
        guardar_productos(productos)
        print('Producto modificado. ✔ ')

def eliminar_producto(productos):
    print('*** ELIMINAR PRODUCTO ****')

    print('Listado de productos:')
    for codigo, producto in productos.items():
        print(f"{codigo}: {producto['nombre']}")
    print()
    codigo = input('Ingrese el código del producto a eliminar o 0 para cancelar: ')
    if codigo not in productos:
        print('El código no existe.')
        return
    del productos[codigo]
    if codigo == 0:
        menu_productos()
    guardar_productos(productos)
    print('Producto eliminado. ✔')


def mostrar_reportes(productos):

    while True:
        print('*** REPORTES DE PRODUCTOS ****')

        print('[1] Mostrar todos los productos')
        print('[2] Buscar por nombre')
        print('[3] Buscar por marca')
        print('[0] Atras')

        opcion_str = input('Ingrese una opcion: ')
        if not opcion_str.isdigit():
            print("Error! ❌ Ingrese una opcion valida.")
            continue
        opcion = int(opcion_str)
        match opcion:
            case 1:
             for codigo, producto in productos.items():
                print (f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto ['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio'] } / STOCK: {producto['stock']}")

                print()
            case 2:
             palabra_clave = input('Ingrese la palabra clave a buscar en el nombre del producto: ')
             encontrado = False
             for codigo, producto in productos.items():
                    if palabra_clave in producto['nombre']:
                        encontrado=True
                        print (f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto ['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio'] } / STOCK: {producto['stock']}")
                        print()
             if not encontrado:
                print(f'No se encontraron productos que contengan la "{palabra_clave}" en su nombre ')
                     
                        

            case 3:
        
             palabra_clave = input('Ingrese la palabra clave a buscar en el nombre del producto: ')
             encontrado = False
             for codigo, producto in productos.items():
                    if palabra_clave in producto['marca']:
                        encontrado=True
                        print (f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto ['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio'] } / STOCK: {producto['stock']}")
                        print()
             if not encontrado:
                print(f'No se encontraron productos que contengan la "{palabra_clave}" en su nombre ')

            case 0:
                menu()
            case other:
                print("Error! ❌ Ingrese una opcion valida")
            
   
  
def menu():
    productos = cargar_productos()
    contador = max([int(id) for id in productos.keys()], default=0) + 1

    while True:
        print('*** BIENVENIDO AL MENU PRINCIPAL ****')

        print('[1] Gestion de productos')
        print('[2] Mostrar reportes')
        print('[0] Salir')
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                menu_productos()
            case 2:
                mostrar_reportes(productos)
        
               
            case 0:
                pantalla_inicio()
            case other:
                 print("Error! ❌ Ingrese una opcion valida")
            
    

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
                 print("Error!  ❌ Ingrese una opcion valida")

if __name__ == '__main__':
    pantalla_inicio()
