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

def eliminar_contacto(agenda, nombre, telefono):
      # Verifica si el contacto a eliminar existe en la agenda
    if nombre == agenda:
        # Elimina el contacto de la agenda
        del agenda[nombre]
        print(f'\nse ha eliminado el contacto {nombre}, {telefono}\n')
    else:
        print(f'\nel contacto {nombre} no existe\n')

def buscar_contacto(agenda, nombre, telefono):
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
    