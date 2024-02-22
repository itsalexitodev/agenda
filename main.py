"""
/* 
 * Se pide que desarrollen EN PAREJAS una aplicación de agenda de contactos en Python con las siguientes funcionalidades:
 * 1. Añadir contacto: Permite a los usuarios agregar un nuevo contacto con nombre y número de teléfono.
 * 2. Ver contactos: Muestra todos los contactos guardados.
 * 3. Eliminar contacto: Permite a los usuarios eliminar un contacto por su nombre.
 * 4. Búsqueda de contactos: Permite a los usuarios buscar un contacto por su nombre.
 * 5. Guardar y cargar contactos en un archivo: La aplicación debe permitir a los usuarios guardar los contactos en un archivo y cargarlos posteriormente.
 * 6. Agregar_contacto(nombre, teléfono): Agrega un contacto al diccionario.
 * 7. Ver_contactos(): Muestra todos los contactos guardados.
 * 8. Eliminar_contacto(nombre): Elimina un contacto por su nombre.
 * 9. Buscar_contacto(nombre): Busca un contacto por su nombre.
 * 10. Guardar_contactos(nombre_archivo): Guarda los contactos en un archivo.
*/
"""
def agregar_contacto(agenda, nombre, telefono):
    # Verifica si el nombre ya existe en la agenda
    if nombre in agenda:
        print(f'\nEl contacto {nombre}, {telefono} ya existe en la agenda\n')
    else:
    # Agrega el contacto al diccionario de la agenda
        agenda[nombre] = telefono
        print(f'\nContacto {nombre} agregado correctamente con el número {telefono}\n')

def ver_contactos(agenda):
    # Verifica si hay contactos en la agenda   
    if agenda:
        for nombre, telefono in agenda.items():
            # Itera sobre los contactos y los muestra
            print(f'\nNombre: {nombre}, \nTeléfono: {telefono}\n')
    else:
        print("\nNo hay ningún contacto\n")

def eliminar_contacto(agenda, nombre):
      # Verifica si el contacto a eliminar existe en la agenda
    if nombre == agenda:
        # Elimina el contacto de la agenda
        del agenda[nombre]
        print(f'\nse ha eliminado el contacto {nombre}, {telefono}\n')
    else:
        print(f'\nel contacto {nombre} no existe\n')

def buscar_contacto(agenda, nombre):
    # Verifica si el contacto está en la agenda y lo muestra
    if nombre in agenda:
        print(f'\nel contcato es:\n\nNombre: {nombre}, \nTeléfono: {telefono}\n')
    else:
        print(f'\nel nombre {nombre} no se ha encontrado\n')

def guardar_contactos(agenda, archivo_agenda):
    # Guarda los contactos en un archivo
    with open(archivo_agenda, 'w') as file:
        for nombre,telefono in agenda.items():
            file.write(f'{nombre},{telefono}')


def cargar_contactos(agenda, archivo_agenda):
    # Carga los contactos desde un archivo
    try:
        with open(archivo_agenda, 'r') as file:
            for line in file:
                nombre, telefono = line.split(',')
                agenda[nombre] = telefono
        return agenda
    except FileNotFoundError:
        print("El archivo no existe")
    
agenda = {}

# Menú de la aplicación de agenda de contactos
while True:
    print(" ############################# ")
    print(" # AGENDA - CONTACTOS - 2024 # ")
    print(" ############################# ")
    print("\n¿Qué quieres hacer?\n")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Guardar contactos en un archivo")
    print("6. Cargar contactos desde un archivo")
    print("7. Salir")

    opcion = input("\nSelecciona una opción (1-7): \n")

    if opcion == "1":
        nombre = input("\nIntroduce el nombre del contacto: \n")
        telefono = None

        while True:
            try:
                telefono = int(input("\nIntroduce el teléfono del contacto: \n"))
                break           
            except ValueError:
                print("\nPor favor, introduce un número válido.")
                continue
        agregar_contacto(agenda, nombre, telefono)

    elif opcion == "2":
        ver_contactos(agenda)

    elif opcion == "3":
        nombre = input("\nIntroduce el nombre del contacto que quieres eliminar: \n")
        eliminar_contacto(agenda, nombre)

    elif opcion == "4":
        nombre = input("\nIntroduce el nombre del contacto que quieres buscar: \n")
        buscar_contacto(agenda, nombre)

    elif opcion == "5":
        archivo_agenda = input("\nIntroduce el nombre del archivo en el que quieres guardar los contactos: \n")
        guardar_contactos(agenda, archivo_agenda)

    elif opcion == "6":
        archivo_agenda = input("\nIntroduce el nombre del archivo del cual quieres cargar los contactos: \n")
        agenda = cargar_contactos(agenda, archivo_agenda)

    elif opcion == "7":
        print("\nGracias por utilizar la aplicación de agenda de contactos. ¡Adiós!\n")
        break

    else:
        print("\nOpción no válida. Por favor, selecciona una opción válida (1-7)")