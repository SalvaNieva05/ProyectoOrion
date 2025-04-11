import pandas as pd
import unidecode
TABLAS = {
    "1- Marca": "855220395",
    "2- Modelos": "1559161636",
    "3- Tractores": "903974325",
    "4- Cisternas": "1824793552",
    "5- Flota": "1348809944",
    "6- Vencimientos": "1737376307",
    "7- Personal": "1952436154",
    "8- Vencimientos_Personal": "1551882233",
    "9- Servicios": "2124342650",
}

URL_BASE = "https://docs.google.com/spreadsheets/d/1tamP14UUTfn9ZLcR0jbBMGS63Auju1mOKvpEHVs7cxI/export?format=csv&gid="


def cargar_tabla():
    """Carga una tabla desde Google Sheets según el diccionario TABLAS"""
    while True:
        print("\nTablas disponibles:")
        for clave in TABLAS:
            print(clave)

        opcion = input("Ingrese el número de la tabla que desea cargar (o 'm' para volver al menú): ").strip()

        if opcion.lower() == 'm':
            return None

        tabla_key = next((key for key in TABLAS if key.startswith(opcion + "-")), None)

        if tabla_key:
            url = URL_BASE + TABLAS[tabla_key]
            try:
                df = pd.read_csv(url)
                print(f"\nTabla '{tabla_key}' cargada correctamente.")
                return df
            except Exception as e:
                print(f"❌ Error al cargar la tabla: {e}")
        else:
            print("⚠ Tabla no encontrada, intente nuevamente.")


def ordenar_segun(df):
    """Ordena la tabla por la columna que el usuario elija."""
    if df is None:
        print("⚠ No hay tabla cargada. Cargue una primero.")
        return

    while True:
        print("\nColumnas disponibles para ordenar:")
        print(", ".join(df.columns))

        columna = input("Ingrese el nombre de la columna para ordenar (o 'm' para volver al menú): ").strip()
        if columna.lower() == 'm':
            return

        columna_normalizada = unidecode.unidecode(columna).lower()
        columnas_normalizadas = {unidecode.unidecode(col).lower(): col for col in df.columns}

        if columna_normalizada in columnas_normalizadas:
            ascendente = input("¿Orden ascendente? (s/n): ").strip().lower() == 's'
            df = df.sort_values(by=columnas_normalizadas[columna_normalizada], ascending=ascendente)
            print("\n✅ Tabla ordenada correctamente:")
            print(df)
            return df
        else:
            print("⚠ Columna no encontrada, intente nuevamente.")


def modificar_fila(df):
    """Permite modificar una fila de la tabla."""
    if df is None:
        print("⚠ No hay tabla cargada. Cargue una primero.")
        return

    while True:
        print("\nColumnas disponibles para buscar:")
        print(", ".join(df.columns))

        columna = input("Ingrese el nombre de la columna para buscar la fila (o 'm' para volver al menú): ").strip()
        if columna.lower() == 'm':
            return

        columna_normalizada = unidecode.unidecode(columna).lower()
        columnas_normalizadas = {unidecode.unidecode(col).lower(): col for col in df.columns}

        if columna_normalizada in columnas_normalizadas:
            valor = input(f"Ingrese el valor a buscar en '{columnas_normalizadas[columna_normalizada]}': ").strip()
            filas = df[df[columnas_normalizadas[columna_normalizada]].astype(str).str.lower() == valor.lower()]

            if not filas.empty:
                print("\nFilas encontradas:")
                print(filas)

                try:
                    index = int(input("Ingrese el índice de la fila que desea modificar: "))
                    if index in df.index:
                        print(f"\nFila seleccionada:\n{df.loc[index]}")

                        print("\nColumnas disponibles para modificar:")
                        print(", ".join(df.columns))

                        columna_modificar = input("Ingrese la columna a modificar: ").strip()
                        columna_modificar_normalizada = unidecode.unidecode(columna_modificar).lower()
                        if columna_modificar_normalizada in columnas_normalizadas:
                            nuevo_valor = input(
                                f"Ingrese el nuevo valor para '{columnas_normalizadas[columna_modificar_normalizada]}': ")
                            df.at[index, columnas_normalizadas[columna_modificar_normalizada]] = nuevo_valor
                            print("✅ Modificación realizada correctamente.")
                            return df
                        else:
                            print("⚠ Columna no encontrada.")
                    else:
                        print("⚠ Índice fuera de rango.")
                except ValueError:
                    print("⚠ Entrada inválida.")
            else:
                print("⚠ No se encontraron resultados.")
        else:
            print("⚠ Columna no encontrada.")
def mostrar_todo(df):
    """Muestra la tabla cargada."""
    if df is None:
        print("⚠ No hay tabla cargada. Cargue una primero.")
    else:
        print("\n📋 Tabla completa:")
        print(df)
