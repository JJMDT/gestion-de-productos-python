import json

def cargar_productos():
    try:
        with open('productos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_productos(productos):
    with open('productos.json', 'w') as archivo:
        json.dump(productos, archivo)

def ingresar_producto(productos, contador):
    print('*** INGRESAR PRODUCTO ***')
    nombre = input('Ingrese el nombre del producto: ')
    marca = input('Ingrese la marca del producto: ')
    presentacion = input('Ingrese la presentación del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    stock = int(input('Ingrese el stock del producto: '))

    productos[contador] = {
        'nombre': nombre,
        'marca': marca,
        'presentacion': presentacion,
        'precio': precio,
        'stock': stock
    }

    guardar_productos(productos)
    print('Producto ingresado correctamente. ✔')
    contador += 1
    return contador

def modificar_producto(productos):
    print('*** MODIFICAR PRODUCTO ***')

    codigo = int(input('Ingrese el código del producto a modificar: '))
    if codigo not in productos:
        print('El código del producto no existe. ❗❗❗')
        return

    producto = productos[codigo]
    print('Ingrese los nuevos datos del producto (deje en blanco si no desea modificar): ')
    nombre = input(f'Nombre actual: {producto["nombre"]}. Nuevo nombre: ')
    marca = input(f'Marca actual: {producto["marca"]}. Nueva marca: ')
    presentacion = input(f'Presentación actual: {producto["presentacion"]}. Nueva presentación: ')
    precio = input(f'Precio actual: {producto["precio"]}. Nuevo precio: ')
    stock = input(f'Stock actual: {producto["stock"]}. Nuevo stock: ')

    if nombre != '':
        producto['nombre'] = nombre
    if marca != '':
        producto['marca'] = marca
    if presentacion != '':
        producto['presentacion'] = presentacion
    if precio != '':
        producto['precio'] = float(precio)
    if stock != '':
        producto['stock'] = int(stock)

    guardar_productos(productos)
    print('Producto modificado correctamente. ✔')

def eliminar_producto(productos):
    print('*** ELIMINAR PRODUCTO ***')

    codigo = int(input('Ingrese el código del producto a eliminar: '))
    if codigo not in productos:
        print('El código del producto no existe. ❗❗❗')
        return

    del productos[codigo]
    guardar_productos(productos)
    print('Producto eliminado correctamente. ✔')

def mostrar_reportes(productos):
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
                    print(f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                    print()
            case 2:
                palabra_clave = input('Ingrese la palabra clave a buscar en el nombre del producto: ')
                encontrado = False
                for codigo, producto in productos.items():
                    if palabra_clave.lower() in producto['nombre'].lower():
                        print(f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                        encontrado = True
                if not encontrado:
                    print(f"No se encontraron productos con la palabra clave '{palabra_clave}' en el nombre.")
            case 3:
                palabra_clave = input('Ingrese la palabra clave a buscar en la marca del producto: ')
                encontrado = False
                for codigo, producto in productos.items():
                    if palabra_clave.lower() in producto['marca'].lower():
                        print(f"CODIGO: {codigo} / NOMBRE: {producto['nombre']} / MARCA: {producto['marca']} / PRESENTACION: {producto['presentacion']} / PRECIO: ${producto['precio']} / STOCK: {producto['stock']}")
                        encontrado = True
                if not encontrado:
                    print(f"No se encontraron productos con la palabra clave '{palabra_clave}' en la marca.")
            case 0:
                return
            case other:
                print("Error! ❌ Ingrese una opción válida.")

