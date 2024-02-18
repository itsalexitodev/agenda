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
    agenda[nombre] = telefono

def ver_contactos(agenda):
    pass

def eliminar_contacto(agenda, nombre):
    pass

def buscar_contacto(agenda, nombre):
    pass

def guardar_contactos(agenda, archivo_agenda):
    pass

def cargar_contactos(archivo_agenda):
    pass

agenda = {}

while True:
    print("\n¿Qué quieres hacer?\n")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Guardar contactos en un archivo")
    print("6. Cargar contactos desde un archivo")
    print("7. Salir")

    opcion = input("\nSelecciona una opción (1-7): ")

    if opcion == "1":
        nombre = input("\nIntroduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        agregar_contacto(agenda, nombre, telefono)
    elif opcion == "2":
        if agenda:
            print("\nContactos en la agenda:")
            ver_contactos(agenda)
        else:
            print("No hay contactos en la agenda.")
    elif opcion == "3":
        nombre = input("\nIntroduce el nombre del contacto que quieres eliminar: ")
        eliminar_contacto(agenda, nombre)
    elif opcion == "4":
        nombre = input("\nIntroduce el nombre del contacto que quieres buscar: ")
        buscar_contacto(agenda, nombre)
    elif opcion == "5":
        if agenda:
            archivo_agenda = input("\nIntroduce el nombre del archivo en el que quieres guardar los contactos: ")
            guardar_contactos(agenda, archivo_agenda)
        else:
            print("No hay contactos para guardar.")
    elif opcion == "6":
        archivo_agenda = input("\nIntroduce el nombre del archivo del cual quieres cargar los contactos: ")
        agenda = cargar_contactos(archivo_agenda)
    elif opcion == "7":
        print("\nGracias por utilizar la aplicación de agenda de contactos. ¡Adiós!")
        break
    else:
        print("\nOpción no válida. Por favor, selecciona una opción válida (1-7)")
