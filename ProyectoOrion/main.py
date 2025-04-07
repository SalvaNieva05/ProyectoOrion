from functions import *


def menu():
    print("\n" + "-" * 30)
    print("Menú de opciones:")
    print("1. Cargar Tabla")
    print("2. Ordenar según")
    print("3. Modificar Fila")
    print("4. Mostrar todo")
    print("0. Salir")

    while True:
        try:
            return int(input("Ingrese opción: "))
        except ValueError:
            print("⚠ Ingrese un número válido.")


def main():
    TABLAS = {
        "1- Marca": "marca.csv",
        "2- Modelos": "modelos.csv",
        "3- tractores": "tractores.csv",
        "4- cisternas": "cisternas.csv",
        "5- flota": "flota.csv",
        "6-vencimientos": "vencimientos.csv",
        "7- personal": "personal.csv",
        "8- vencimientos_personal": "vencimientos_personal.csv",
        "9- servicios": "servicios.csv",
    }

    df = None
    while True:
        op = menu()
        if op == 1:
            df = cargar_tabla(TABLAS)
        elif op == 2:
            df = ordenar_segun(df)
        elif op == 3:
            df = modificar_fila(df)
        elif op == 4:
            mostrar_todo(df)
        elif op == 0:
            print("Hasta luego. 👋")
            break
        else:
            print("⚠ Opción inválida.")


if __name__ == "__main__":
    main()