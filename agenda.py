# -*- coding: iso-8859-1 -*-

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
    pass

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

if __name__ == "__main__":
    def leer_archivo(main):
        try:
            with open(main.py, 'r') as archivo:
                contenido = archivo.read()
                print("Contenido del archivo:")
                print(contenido)
        except FileNotFoundError:
            print(f"El archivo '{main.py}' no se encontró.")