from agenda import *

# Menú de la aplicación de agenda de contactos
def main():
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

if __name__ == "__main__":
    main()