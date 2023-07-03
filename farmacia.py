import json


def guardar_usuarios(usuarios): #guarda los usuarios en el archivo usuarios.json
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo)

def cargar_usuarios(): #carga los datos de los usuarios y son cargados en usuarios.json
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
def crear_usuario(): #crear un usuario nuevo
    usuarios = cargar_usuarios()
    contador = len(usuarios) + 1  # Obtenemos el valor del contador sumándole 1 a la cantidad de usuarios existentes
    dni = input('Ingrese su DNI: ')
    if dni in [usuario['dni'] for usuario in usuarios.values()]: # Verifica si el DNI ingresado ya existe en el diccionario de usuarios.
        print('Error! ❌ Ya se encuentra registrado.')
        pantalla_inicio()
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    while True:
        nombre_usuario = input('Ingrese un nombre de usuario: ')
        
        if nombre_usuario in [usuario['nombre_usuario'] for usuario in usuarios.values()]: # Verifica si el nombre de usuario ingresado ya existe en el diccionario de usuarios.

            print('El nombre de usuario ya existe, intente con otro nombre de usuario.')
        else:
            break
    password = input('Ingrese su contraseña: ')
    ID = str(contador)  # ID de cada usuario en la lista usuarios
    usuarios[ID] = {'nombre': nombre, 'apellido': apellido, 'dni': dni, 'nombre_usuario': nombre_usuario, 'password': password}
    guardar_usuarios(usuarios)
    print('Usuario creado. ✔ ')
    pantalla_inicio()

def iniciar_sesion(): #iniciar sesion con los datos del usuario
    usuarios = cargar_usuarios()
    nombre_usuario = input('Ingrese su nombre de usuario: ')
    encontrado = False
    for usuario in usuarios.values():
        if usuario['nombre_usuario'] == nombre_usuario:
            encontrado = True
            break
    
    if encontrado:
        password = input('Ingrese su contraseña: ')
        if password == usuario['password']:
            print('Inicio de sesión correcto')
            carrito = []
            menu()
        else:
            print('Error! ❌ Contraseña incorrecta')
            pantalla_inicio()
    else:
        print('Error! ❌ El nombre de usuario no existe')
        pantalla_inicio()


#seccion de productos
def cargar_productos(): #carga los datos de los productos y son cargados en productos.json
    try:
        with open('productos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_productos(productos): #guarda los productos en el archivo productos.json
    with open('productos.json', 'w') as archivo:
        json.dump(productos, archivo)
def menu_productos():
    print('*** GESTION DE PRODUCTOS ***')

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
carrito = {}

def ingresar_producto(productos,contador): #crea un nuevo un producto en la lista productos.js
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

def modificar_producto(productos): #modifica un producto de la lista productos.js
    print('*** MODIFICAR PRODUCTO ****')
    print('Listado de productos:')
    for codigo, producto in productos.items():
        print(f"{codigo}: {producto['nombre']}  STOCK:{producto['stock']}")
    
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
                productos[codigo]['marca'] = marca
            case 3:
                presentacion = input('Ingrese la nueva presentacion del producto: ')
                productos[codigo]['presentacion'] = presentacion
            case 4:
                precio = float(input('Ingrese el nuevo precio: '))
                productos[codigo]['precio'] = precio
            case 5:
                stock = int(input('Ingrese el nuevo stock: '))
                productos[codigo]['stock'] = stock
            case 6:
                nombre = input('Ingrese el nuevo nombre del producto: ')
                productos[codigo]['nombre'] = nombre
                marca = input('Ingrese la nueva marca del producto: ')
                productos[codigo]['marca'] = marca
                presentacion = input('Ingrese la nueva presentacion del producto: ')
                productos[codigo]['presentacion'] = presentacion
                precio = float(input('Ingrese el nuevo precio: '))
                productos[codigo]['precio'] = precio
                stock = int(input('Ingrese el nuevo stock: '))
                productos[codigo]['stock'] = stock
            case 0:
                break
            case other:
                print("Error! ❌ Ingrese una opcion valida")

    guardar_productos(productos)
    print('Producto modificado. ✔ ')

def eliminar_producto(productos): #elimina un producto de la lista productos.js
    print('*** ELIMINAR PRODUCTO ****')

    print('Listado de productos:')
    for codigo, producto in productos.items():
        print(f"{codigo}: {producto['nombre']}")
    print()
    codigo = input('Ingrese el código del producto a eliminar o 0 para cancelar: ')
    if codigo not in productos:
        print('El código no existe.')
        return 
    producto = productos[codigo]
    confirmacion = input(f" Esta seguro que desea eliminar: COD:{codigo} NOMBRE: {producto['nombre']}?   S/N : ")
    if confirmacion.upper()=='S':
     del productos[codigo]
     
     guardar_productos(productos)
     print('Producto eliminado. ✔')
    else:
        print('eliminacion cancelada')
             
def mostrar_reportes_productos(productos): #mostrar reportes de productos ( todos, por nombre o marca)
    productos = cargar_productos()

    print('*** REPORTES ***')

    while True:
        print('[1] Mostrar todos los productos')
        print('[2] Buscar producto por palabra clave en el nombre')
        print('[3] Buscar producto por palabra clave en la marca')
        print('[0] Atrás')

        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                print('--- Todos los productos ---')
                for codigo, producto in productos.items():
                    print(f"COD:{codigo} | NOMBRE: {producto['nombre']} | MARCA: {producto['marca']} | PRESENTACION: {producto['presentacion']} | PRECIO: ${producto['precio']} | STOCK: {producto['stock']}")
                  
            case 2:
                palabra_clave = input('Ingrese la palabra clave a buscar en el nombre del producto: ')
                encontrado = False
                for codigo, producto in productos.items():
                    if palabra_clave.lower() in producto['nombre'].lower():
                        print(f"COD: {codigo} | NOMBRE: {producto['nombre']} | MARCA: {producto['marca']} | PRESENTACION: {producto['presentacion']} | PRECIO: ${producto['precio']} | STOCK: {producto['stock']}")
                        encontrado = True
                if not encontrado:
                    print(f"No se encontraron productos con la palabra clave '{palabra_clave}' en el nombre.")
            case 3:
                palabra_clave = input('Ingrese la palabra clave a buscar en la marca del producto: ')
                encontrado = False
                for codigo, producto in productos.items():
                    if palabra_clave.lower() in producto['marca'].lower():
                        print(f"COD: {codigo} | NOMBRE: {producto['nombre']} | MARCA: {producto['marca']} | PRESENTACION: {producto['presentacion']} | PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                        encontrado = True
                if not encontrado:
                    print(f"No se encontraron productos con la palabra clave '{palabra_clave}' en la marca.")
            case 0:
                return
            case other:
                print("Error! ❌ Ingrese una opción válida.")
def mostrar_reportes(productos): # menu de reportes ( productos y usuarios)
    productos = cargar_productos()

    print('*** REPORTES ***')

    while True:
        print('[1] Reportes de productos')
        print('[2] Reportes de usuarios')
      
        print('[0] Atrás')

        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                mostrar_reportes_productos(productos)
                  
            case 2:
                mostrar_usuarios()
                
            case 0:
                menu()
            case other:
                print("Error! ❌ Ingrese una opción válida.")


#seccion de usuarios    
def menu_usuarios(): #menu de gestion de usuarios ( crear , modificar o eliminar usuario )
    print('*** GESTION DE USUARIOS ***')
    usuarios=cargar_usuarios()
    while True:
        print('[1] Agregar usuario')
        print('[2] Modificar usuario')
        print('[3] Eliminar usuario')
        print('[0] Atras')
        opcion=int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
                crear_usuario()
            case 2:
                modificar_usuario()
            case 3:
                eliminar_usuario()
            case 0:
                menu()
         
def mostrar_usuarios(): #mostrar usuarios
    usuarios = cargar_usuarios()

    print('*** REPORTES USUARIOS ***')

    while True:
        print('[1] Mostrar todos los usuarios')
        print('[2] Buscar usuario por palabra clave en el NOMBRE ')
        print('[3] Buscar usuario por palabra clave en el APELLIDO ')
        print('[0] Atrás')

        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:

                usuarios = cargar_usuarios()
                if usuarios:
                    print("*** USUARIOS REGISTRADOS ***")
                    print()
                    for dni, usuario in usuarios.items():
                     print("Nombre:", usuario['nombre'])
                     print("Apellido:", usuario['apellido'])
                     print("DNI:", usuario['dni'])
                     print('Usuario:', usuario['nombre_usuario'])
                     print("-----------------------")
                else:
                    print("No hay registros de usuarios.")
                    mostrar_reportes()
            case 2 :
                 
                    usuarios = cargar_usuarios()
                    if not usuarios:
                        print("No hay registros de usuarios.")
                        return
                    
                    palabra_clave = input("Ingrese la palabra clave a buscar en el nombre: ")
                    encontrado = False
                    
                    for dni, usuario in usuarios.items():
                        if palabra_clave.lower() in usuario['nombre'].lower():
                            print()
                            print("Nombre:", usuario['nombre'])
                            print("Apellido:", usuario['apellido'])
                            print("DNI:", usuario['dni'])
                            print('Usuario:', usuario['nombre_usuario'])
                            print("-----------------------")
                            encontrado = True
                    
                    if not encontrado:
                        print(f"No se encontraron usuarios con la palabra clave '{palabra_clave}' en el nombre.")
            case 3:
                if not usuarios:
                    print("No hay registros de usuarios.")
                    return

                palabra_clave = input("Ingrese la palabra clave a buscar en el APELLIDO: ")
                encontrado = False

                for dni, usuario in usuarios.items():
                    if palabra_clave.lower() in usuario['apellido'].lower():
                        print("Nombre:", usuario['nombre'])
                        print("Apellido:", usuario['apellido'])
                        print("DNI:", usuario['dni'])

                        print('Usuario:', usuario['nombre_usuario'])
                        print("-----------------------")
                        encontrado = True

                if not encontrado:
                    print(f"No se encontraron usuarios con la palabra clave '{palabra_clave}' en el apellido.")
            case 0:
                mostrar_reportes(usuarios)
            case other:
                print("Error! ❌ Ingrese una opción válida.")
def modificar_usuario(): #modifica un usuario y los datos se guardan en usuarios.json
    usuarios = cargar_usuarios()

    print('*** MODIFICAR USUARIO ***')
    print('Listado de usuarios')
    for id_usuario, usuario in usuarios.items():
        print(f"ID: {id_usuario}")
        print(f"Usuario: {usuario['nombre_usuario']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Apellido: {usuario['apellido']}")
        print(f"DNI: {usuario['dni']}")
        print('-----------')

    id_usuario = input('Ingrese el ID del usuario a modificar: ')
    if id_usuario not in usuarios:
        print('El usuario no existe.')
        return

    print('Valores actuales del usuario:')
    
    print(f"Nombre: {usuarios[id_usuario]['nombre']}")
    print(f"Apellido: {usuarios[id_usuario]['apellido']}")
    print(f"DNI: {usuarios[id_usuario]['dni']}")
    print(f"Usuario: {usuarios[id_usuario]['nombre_usuario']}")
    print(f"Contraseña: {usuarios[id_usuario]['password']}")
    print('-----------')

    while True:
        print('¿Qué desea modificar?')
        print('[1] Nombre')
        print('[2] Apellido')
        print('[3] DNI')
        print('[4] Usuario')
        print('[5] Contraseña')
        print('[0] Finalizar')
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                nombre = input('Ingrese el nuevo nombre: ')
                usuarios[id_usuario]['nombre'] = nombre
            case 2:
                apellido = input('Ingrese el nuevo apellido: ')
                usuarios[id_usuario]['apellido'] = apellido
            case 3:
                dni_nuevo = input('Ingrese el nuevo DNI: ')
                usuarios[id_usuario]['dni'] = dni_nuevo
            case 4:
                nombre_usuario = input('Ingrese el nuevo nombre de usuario: ')
                usuarios[id_usuario]['nombre_usuario'] = nombre_usuario
            case 5:
                password = input('Ingrese la nueva contraseña: ')
                usuarios[id_usuario]['password'] = password
            case 0:
                break
            case other:
                print("Error! ❌ Ingrese una opción válida.")

    guardar_usuarios(usuarios)
    print('Usuario modificado. ✔')

def eliminar_usuario(): #elimina un usuario del archivo usuarios.json
    usuarios = cargar_usuarios()
    print('*** ELIMINAR USUARIO ***')
    print('Listado de usuarios')
    
    for id_usuario, usuario in usuarios.items():
        print(f"ID: {id_usuario}")
        print(f"Usuario: {usuario['nombre_usuario']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Apellido: {usuario['apellido']}")
        print(f"DNI: {usuario['dni']}")
        print('-----------')
    
    id_usuario = input('Ingrese el ID de usuario del usuario a eliminar: ')

    if id_usuario not in usuarios:
        print('Error! ❌ El usuario no existe.')
        return

    usuario = usuarios[id_usuario]
    confirmacion = input(f"¿Está seguro que desea eliminar?\nID: {id_usuario}\nUsuario: {usuario['nombre_usuario']}\nNombre: {usuario['nombre']}\nApellido: {usuario['apellido']}\nS/N: ")
    
    if confirmacion.upper() == 'S':
        del usuarios[id_usuario]
        guardar_usuarios(usuarios)
        print('Usuario eliminado. ✔')
    else:
        print('Eliminación cancelada.')




#seccion carrito de ventas
def agregar_producto_al_carrito(carrito, productos, codigo_producto, cantidad):
    if codigo_producto not in productos:
        print('El código del producto no existe.')
        return

    producto = productos[codigo_producto]
    if producto['stock'] < cantidad:
        print('No hay suficiente stock disponible.')
        return

    if codigo_producto in carrito:
        carrito[codigo_producto]['cantidad'] += cantidad
    else:
        carrito[codigo_producto] = {
            'nombre': producto['nombre'],
            'precio': producto['precio'],
            'cantidad': cantidad
        }

    productos[codigo_producto]['stock'] -= cantidad
    guardar_productos(productos)
    print('Producto agregado al carrito. ✔')
def mostrar_carrito(carrito):
    def mostrar_carrito(carrito):
     print('*** CARRITO DE COMPRAS ***')
    if not carrito:
        print('El carrito está vacío.')
        return

    total = 0
    for codigo, producto in carrito.items():
        subtotal = producto['precio'] * producto['cantidad']
        total += subtotal
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Subtotal: {subtotal}")
        print()

    print(f"Total gastado: {total}")
def menu_ventas():
    productos = cargar_productos()
    carrito = {}
    contador = len(productos) + 1

    while True:
        print('*** Ventas ***')
        
        print('[1] Agregar producto al carrito')
        print('[2] Mostrar carrito')
        print('[3] Finalizar venta')
        print('[0] Salir')
        opcion = input('Ingrese una opción: ')

        if opcion == '0':
            break
        elif opcion == '1':
            print('Listado de productos:')
            for codigo, producto in productos.items():
                print(f"{codigo}: {producto['nombre']} STOCK: {producto['stock']}")
            codigo_producto = input('Ingrese el código del producto: ')
            cantidad = int(input('Ingrese la cantidad: '))
            agregar_producto_al_carrito(carrito, productos, codigo_producto, cantidad)
        elif opcion == '2':
            mostrar_carrito(carrito)
        elif opcion == '3':
            finalizar_venta(productos,carrito)
        else:
            print('Opción inválida.')
def obtener_precio_producto(producto):
    pass
def registrar_venta():
    total_gastado = 0
    print("Productos en el carrito:")
    for producto, cantidad in carrito:
        precio = obtener_precio_producto(producto)  # Reemplaza 'obtener_precio_producto' con la función adecuada que obtenga el precio del producto
        subtotal = precio * cantidad
        print(f"{producto}: {cantidad} x {precio} = {subtotal}")
        total_gastado += subtotal
    print("Total gastado:", total_gastado)
    carrito.clear()  
def finalizar_venta(productos, carrito):
    print('*** FINALIZAR VENTA ***')
    mostrar_carrito(carrito)
    confirmacion = input('¿Desea finalizar la venta? (S/N): ')
    if confirmacion.upper() == 'S':
     total = 0
     for codigo, producto in carrito.items():
         subtotal = producto['precio'] * producto['cantidad']
         total += subtotal
         productos[codigo]['stock'] - producto['cantidad']
     carrito.clear()
     guardar_productos(productos)
     print(f'Venta exitosa. Total a pagar: {total}')
    else:
     print('Venta cancelada.')

    # No se realiza el descuento del stock si la venta es cancelada

     carrito.clear()
     guardar_productos(productos)


def menu(): #menu principal
    productos = cargar_productos()
    contador = max([int(id) for id in productos.keys()], default=0) + 1

    while True:
        print('*** BIENVENIDO AL MENU PRINCIPAL ****')

        print('[1] Gestion de productos')
        print('[2] Gestion de usuarios')
        print('[3] Mostrar reportes')
        print('[4] Ventas')
        print('[0] Salir')
        
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                menu_productos()
            case 2:
                menu_usuarios()
            case 3:
                mostrar_reportes(productos)
            case 4:
                menu_ventas()
               
            case 0:
                pantalla_inicio()
            case other:
                 print("Error! ❌ Ingrese una opcion valida")
        
             
            
def pantalla_inicio(): #pantalla de inicio, donde se inicia sesion
    print('****LOGIN****')
    print('[1] Crear usuario')
    print('[2] Iniciar sesion')
    
    opcion = int(input('Ingrese una opción: '))
    match opcion:
        case 1:
           crear_usuario()
        case 2:
            iniciar_sesion()
        case other:
             print("Error! ❌ Ingrese una opcion valida")
             pantalla_inicio()
    


            
