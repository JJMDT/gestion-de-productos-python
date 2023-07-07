import json

def guardar_proveedores(proveedores): #guarda los proveedores en el archivo proveedores.json
    with open('proveedores.json','w') as archivo:
        json.dump(proveedores,archivo) 
def cargar_proveedores():# carga los datos de los proveedores y son cargados en proveedores.json
    try:
        with open('proveedores.json','r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

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
def menu_productos(): #Menu gestion de productos (crear, modifica, eliminar producto)
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
            return
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
        print(f"{codigo}: {producto['nombre']}  MARCA: {producto['marca']}  PRESENTACION: {producto['presentacion']} STOCK:{producto['stock']}")
    
    codigo = input('Ingrese el código del producto a modificar: ')
    if codigo not in productos:
        print('El código no existe.')
        return
    print()
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
        print('Eliminacion cancelada')
             
def mostrar_reportes_productos(productos): #mostrar reportes de productos ( todos, por nombre o marca)
    productos = cargar_productos()

    print('*** REPORTES DE PRODUCTOS ***')

    while True:
        print('[1] Mostrar todos los productos')
        print('[2] Buscar producto por palabra clave en el nombre')
        print('[3] Buscar producto por palabra clave en la marca')
        print('[0] Atras')

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
def mostrar_reportes(productos): # menu de reportes ( productos, usuarios, proveedores)
    productos = cargar_productos()

    print('*** REPORTES ***')

    while True:
        print('[1] Reportes de productos')
        print('[2] Reportes de usuarios')
        print('[3] Reportes de proveedores')
        print('[0] Atras')

        opcion = int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
                mostrar_reportes_productos(productos)
                  
            case 2:
                mostrar_usuarios()
            case 3:
                mostrar_proveedores()
                
            case 0:
                menu()
            case other:
                print("Error! ❌ Ingrese una opción válida.")


#seccion de usuarios    
def menu_usuarios(): #menu de gestion de usuarios ( crear, modificar o eliminar usuario )
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
               return
         
def mostrar_usuarios(): #mostrar usuarios
    usuarios = cargar_usuarios()

    print('*** REPORTES DE USUARIOS ***')

    while True:
        print('[1] Mostrar todos los usuarios')
        print('[2] Buscar usuario por palabra clave en el NOMBRE ')
        print('[3] Buscar usuario por palabra clave en el APELLIDO ')
        print('[0] Atras')

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
    confirmacion = input(f"\nID: {id_usuario}\nUsuario: {usuario['nombre_usuario']}\nNombre: {usuario['nombre']}\nApellido: {usuario['apellido']}\n\n¿Está seguro que desea eliminar este usuario?  S/N: ")
    
    if confirmacion.upper() == 'S':
        del usuarios[id_usuario]
        guardar_usuarios(usuarios)
        print('Usuario eliminado. ✔')
    else:
        print('Eliminación cancelada.')

#seccion proveedores
def menu_proveedores(): # Menu proveedores
    print('*** GESTION DE PROVEEDORES ***') #menu gestion de proveedores ( nuevo, modificar, eliminar)
    proveedores = cargar_proveedores()
    contador = len(proveedores) + 1
    while True:
        print('[1] Agregar proveedor')
        print('[2] Modificar proveedor')
        print('[3] Eliminar proveedor')
        print('[0] Atras')
        opcion=int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
                nuevo_proveedor(proveedores, contador)
            case 2:
                modificar_proveedor()
                
            case 3:
                eliminar_proveedor(proveedores)
                
            case 0:
                return
            case other:
                print("Error! ❌ Ingrese una opcion valida")
                menu_proveedores()
def nuevo_proveedor(proveedores,contador):#crea un nuevo proveedor 
    proveedores = cargar_proveedores()
    
    nombre_proveedor=input('Ingrese el nombre del proveedor: ')
    nombre_contacto=input('Ingrese el nombre del contacto: ')
    direccion=input('Ingrese la direccion del proveedor: ')
    telefono=int(input('Ingrese el numero de telefono: '))
    correo=input('Ingrese el correo electronico: ')
    observaciones=input('Observaciones: ')
    id_proveedor = str(contador)
    proveedores[id_proveedor] = {
        'nombre_proveedor': nombre_proveedor,
        'nombre_contacto': nombre_contacto,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'observaciones': observaciones
    }
    guardar_proveedores(proveedores)
    print('Proveedor guardado con exito. ✔ ')
    contador + 1
    menu_proveedores()
def modificar_proveedor(): #Modificar un proveedor de la lista proveedores.json
    proveedores = cargar_proveedores()
    print('*** MODIFICAR USUARIO ***')
    print('Listado de provvedores')
    for id_proveedor, proveedor in proveedores.items():
        print()
        print(f'ID: {id_proveedor}')
        print(f'NOMBRE: {proveedores[id_proveedor]["nombre_proveedor"]}')
        print(f'CONTACTO: {proveedores[id_proveedor]["nombre_contacto"]}')
        print(f'DIRECCION: {proveedores[id_proveedor]["direccion"]}')
        print(f'TELEFONO: {proveedores[id_proveedor]["telefono"]}')
        print(f'CORREO: {proveedores[id_proveedor]["correo"]}')
        print(f'OBSERVACIONES: {proveedores[id_proveedor]["observaciones"]}')
        print('------------')

    id_proveedor = input('Ingrese el ID del proveedor a modificar: ')
    if id_proveedor not in proveedores:
        print('El proveedor no existe. ')
        return
    print('Valores actuales del proveedor. ')
    print(f'NOMBRE: {proveedores[id_proveedor]["nombre_proveedor"]}')
    print(f'CONTACTO: {proveedores[id_proveedor]["nombre_contacto"]}')
    print(f'DIRECCION: {proveedores[id_proveedor]["direccion"]}')
    print(f'TELEFONO: {proveedores[id_proveedor]["telefono"]}')
    print(f'CORREO: {proveedores[id_proveedor]["correo"]}')
    print(f'OBSERVACIONES: {proveedores[id_proveedor]["correo"]}')
    print('------------')

    while True:
        print('¿Que desea modificar?: ')
        print('[1] Nombre de proveedor')
        print('[2] Nombre de contacto')
        print('[3] Direccion')
        print('[4] Telefono')
        print('[5] Correo electronico')
        print('[6] Observaciones')
        print('[7] Todo')
        print('[0] Finalizar')

        opcion=int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
                nombre=input('Ingrese el nuevo nombre: ')
                proveedores[id_proveedor]['nombre']=nombre
            case 2:
                nombre_contacto=input('Ingrese el nuevo nombre de contacto: ')
                proveedores[id_proveedor]['nombre_contacto']=nombre_contacto
            case 3:
                direccion=input('Ingrese la nueva direccion: ')
                proveedores[id_proveedor]['direccion']=direccion
            case 4:
                telefono=input('Ingrese el nuevo telefono: ')
                proveedores[id_proveedor]['telefono']=telefono
            case 5:
                correo=input('Ingrese el nuevo correo electronico: ')
                proveedores[id_proveedor]['correo']=correo
            case 6:
                observaciones=input('Ingrese la nueva observacion: ')
                proveedores[id_proveedor]['observaciones']=observaciones
            case 7:
                nombre=input('Ingrese el nuevo nombre: ')
                proveedores[id_proveedor]['nombre']=nombre
                nombre_contacto=input('Ingrese el nuevo nombre de contacto: ')
                proveedores[id_proveedor]['nombre_contacto']=nombre_contacto
                direccion=input('Ingrese la nueva direccion: ')
                proveedores[id_proveedor]['direccion']=direccion
                telefono=input('Ingrese el nuevo telefono: ')
                proveedores[id_proveedor]['telefono']=telefono
                correo=input('Ingrese el nuevo correo electronico: ')
                proveedores[id_proveedor]['correo']=correo
                observaciones=input('Ingrese la nueva observacion: ')
                proveedores[id_proveedor]['observaciones']=observaciones
            case 0:
                break
            case other:
                print("Error! ❌ Ingrese una opcion valida")
def eliminar_proveedor(proveedores): #Eliminar un proveedor de la lista provveedores.json
    print('*** ELIMINAR PROVEEDOR ***')
    print('Listado de proveedores')
    for id_proveedor, proveedor in proveedores.items():
        print(f'{id_proveedor} : {proveedores[id_proveedor]["nombre_proveedor"]}')
    print()
    id_proveedor = input('Ingrese el código del proveedor a eliminar o 0 para cancelar: ')
    if id_proveedor not in proveedores:
        print('El proveedor no existe.')
        return
    proveedor = proveedores[id_proveedor]
    confirmacion = input(f'¿Está seguro de que desea eliminar: ID:{id_proveedor}  {proveedores[id_proveedor]["nombre_proveedor"]}? (S/N): ')
    if confirmacion.upper() == 'S':
        del proveedores[id_proveedor]
        guardar_proveedores(proveedores)
        print('Proveedor eliminado con éxito. ✔')
    else:
        print('Eliminación cancelada.')
def mostrar_proveedores(): #Menu de reportes de proveedores
    print('*** REPORTES DE PROVEEDORES ***')
    proveedores = cargar_proveedores()
    while True:
        print('[1] Mostrar todos los proveedores')
        print('[2] Buscar proovedor por nombre')
        print('[3] Buscar proovedor por insumo')
        print('[0] Atras')

        opcion=int(input('Ingrese una opcion: '))
        match opcion:

            case 1:
                print('--- Todos los proveedores ---')
                for id_proveedor, proveedor in proveedores.items():
                    print(f"ID: {id_proveedor}")
                    print(f"NOMBRE: {proveedor['nombre_proveedor']}")
                    print(f"CONTACTO: {proveedor['nombre_contacto']}")
                    print(f"DIRECCION: {proveedor['direccion']}")
                    print(f"TELEFONO: {proveedor['telefono']}")
                    print(f"CORREO ELECTRONICO: {proveedor['correo']}")
                    print(f"OBSERVACIONES: {proveedor['observaciones']}")
                    print('------------')
            case 2:
                proveedor = cargar_proveedores()
                if not proveedores:
                        print("No hay registros de proveedores.")
                        return
                    
                palabra_clave = input("Ingrese la palabra clave a buscar en el nombre: ")
                encontrado = False
                    
                for id_proveedor, proveedor in proveedores.items():
                        if palabra_clave.lower() in proveedores[id_proveedor]['nombre_proveedor'].lower():
                            print()
                            print(f"ID: {id_proveedor}")
                            print(f"NOMBRE: {proveedor['nombre_proveedor']}")
                            print(f"CONTACTO: {proveedor['nombre_contacto']}")
                            print(f"DIRECCION: {proveedor['direccion']}")
                            print(f"TELEFONO: {proveedor['telefono']}")
                            print(f"CORREO ELECTRONICO: {proveedor['correo']}")
                            print(f"OBSERVACIONES: {proveedor['observaciones']}")
                            print('------------')
                            encontrado = True
                    
                if not encontrado:
                        print(f"No se encontraron proveedores con la palabra clave '{palabra_clave}' en el nombre.")
            case 3:
                proveedor = cargar_proveedores()
                if not proveedores:
                        print("No hay registros de insumos.")
                        return
                    
                palabra_clave = input("Ingrese la palabra clave a buscar por insumos: ")
                encontrado = False
                    
                for id_proveedor, proveedor in proveedores.items():
                        if palabra_clave.lower() in proveedores[id_proveedor]['observaciones'].lower():
                            print()
                            print(f"ID: {id_proveedor}")
                            print(f"NOMBRE: {proveedor['nombre_proveedor']}")
                            print(f"CONTACTO: {proveedor['nombre_contacto']}")
                            print(f"DIRECCION: {proveedor['direccion']}")
                            print(f"TELEFONO: {proveedor['telefono']}")
                            print(f"CORREO ELECTRONICO: {proveedor['correo']}")
                            print(f"OBSERVACIONES: {proveedor['observaciones']}")
                            print('------------')
                            encontrado = True
                    
                if not encontrado:
                        print(f"No se encontraron insumos con la palabra clave '{palabra_clave}' en el nombre.")
            case 0:
                return
            case other:
                print("Error! ❌ Ingrese una opción válida.")

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

def menu_gestion(): #menu de getion (productos, usuarios, proveedores)
    print('*** MENU DE GESTION ***')
    while True:
        print('[1] Gestion de productos')
        print('[2] Gestion de usuarios')
        print('[3] Gestion de proveedores')
        print('[0] Atras')
        opcion=int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
                menu_productos()
            case 2:
                menu_usuarios()
            case 3:
                menu_proveedores()
            case 0:
                menu()
            case other:
                print("Error! ❌ Ingrese una opcion valida")
def menu(): #menu principal
    productos = cargar_productos()
    contador = max([int(id) for id in productos.keys()], default=0) + 1

    while True:
        print('*** BIENVENIDO AL MENU PRINCIPAL ****')

        print('[1] Gestion ')
        print('[2] Reportes')
        print('[3] Ventas')
        print('[0] Salir')
        
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                menu_gestion()
            
            case 2:
                mostrar_reportes(productos)
            case 3:
                menu_ventas()
               
            case 0:
                pantalla_inicio()
            case other:
                 print("Error! ❌ Ingrese una opcion valida")
        
             
            
def pantalla_inicio(): #pantalla de inicio, donde se inicia sesion
    print('*** LOGIN ***')
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
    


            
