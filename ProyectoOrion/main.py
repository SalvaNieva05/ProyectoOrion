from functions import *


def menu():
    """Muestra el menú de opciones."""
    print("\n" + "-" * 30)
    print("📌 Menú de opciones:")
    print("1. Cargar Tabla")
    print("2. Ordenar según una columna")
    print("3. Modificar Fila")
    print("4. Mostrar Todo")
    print("0. Salir")

    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 0 <= opcion <= 4:
                return opcion
            print("⚠ Opción inválida, ingrese un número entre 0 y 4.")
        except ValueError:
            print("⚠ Entrada inválida, ingrese un número.")


def main():
    df = None
    while True:
        opcion = menu()

        if opcion == 1:
            df = cargar_tabla()
        elif opcion == 2:
            df = ordenar_segun(df)
        elif opcion == 3:
            df = modificar_fila(df)
        elif opcion == 4:
            mostrar_todo(df)
        elif opcion == 0:
            print("👋 Hasta luego, vuelva pronto.")
            break


if __name__ == "__main__":
    main()
