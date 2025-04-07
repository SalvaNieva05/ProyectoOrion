import pandas as pd
import unidecode


def normalizar(texto):
    return unidecode.unidecode(str(texto)).strip().lower()


def cargar_tabla(tablas):
    while True:
        print("\nTablas disponibles:")
        for nombre in tablas:
            print(f"- {nombre}")

        nombre_tabla = input("Ingrese el nombre exacto de la tabla (o 'm' para volver al menú): ").strip()
        if nombre_tabla.lower() == 'm':
            return None

        if nombre_tabla in tablas:
            archivo_csv = tablas[nombre_tabla]
            try:
                df = pd.read_csv(archivo_csv)
                print(f"✅ Tabla '{nombre_tabla}' cargada correctamente.")
                return df
            except Exception as e:
                print(f"❌ Error al cargar la tabla: {e}")
        else:
            print("⚠ Nombre inválido. Intente nuevamente.")


def mostrar_todo(df):
    if df is None:
        print("⚠ No hay tabla cargada. Cargue una primero.")
    else:
        print("\nContenido de la tabla:")
        print(df)


def ordenar_segun(df):
    if df is None:
        print("⚠ No hay tabla cargada. Cargue una primero.")
        return df

    while True:
        print("\nColumnas disponibles para ordenar:")
        print(", ".join(df.columns))

        columna = input("Ingrese el nombre de la columna para ordenar (o 'm' para volver al menú): ").strip()
        if columna.lower() == 'm':
            return df

        columna_normalizada = normalizar(columna)
        columnas_normalizadas = {normalizar(col): col for col in df.columns}

        if columna_normalizada in columnas_normalizadas:
            ascendente = input("¿Orden ascendente? (s/n): ").strip().lower() == 's'
            try:
                df = df.sort_values(by=columnas_normalizadas[columna_normalizada], ascending=ascendente)
                print("\n✅ Tabla ordenada correctamente:")
                print(df)
                return df
            except Exception as e:
                print(f"❌ Error al ordenar: {e}")
        else:
            print("⚠ Columna no encontrada, intente nuevamente.")


def modificar_fila(df):
    if df is None:
        print("⚠ No hay tabla cargada. Cargue una primero.")
        return df

    while True:
        print("\nColumnas disponibles para buscar:")
        print(", ".join(df.columns))

        columna = input("Ingrese el nombre de la columna para buscar la fila (o 'm' para volver al menú): ").strip()
        if columna.lower() == 'm':
            return df

        columna_normalizada = normalizar(columna)
        columnas_normalizadas = {normalizar(col): col for col in df.columns}

        if columna_normalizada in columnas_normalizadas:
            valor = input(f"Ingrese el valor a buscar en '{columnas_normalizadas[columna_normalizada]}': ").strip()
            try:
                coincidencias = df[df[columnas_normalizadas[columna_normalizada]].astype(str).apply(normalizar) == normalizar(valor)]
                if coincidencias.empty:
                    print("⚠ No se encontraron coincidencias.")
                    continue

                print("\nFilas encontradas:")
                print(coincidencias)

                try:
                    index = int(input("Ingrese el índice de la fila que desea modificar: "))
                    if index in df.index:
                        print(f"\nFila seleccionada:\n{df.loc[index]}")

                        print("\nColumnas disponibles para modificar:")
                        print(", ".join(df.columns))

                        columna_modificar = input("Ingrese la columna a modificar: ").strip()
                        columna_modificar_normalizada = normalizar(columna_modificar)

                        if columna_modificar_normalizada in columnas_normalizadas:
                            nuevo_valor = input(f"Ingrese el nuevo valor para '{columnas_normalizadas[columna_modificar_normalizada]}': ")
                            df.at[index, columnas_normalizadas[columna_modificar_normalizada]] = nuevo_valor
                            print("✅ Modificación realizada correctamente.")
                            return df
                        else:
                            print("⚠ Columna no válida.")
                    else:
                        print("⚠ Índice fuera de rango.")
                except ValueError:
                    print("⚠ Índice inválido.")
            except Exception as e:
                print(f"❌ Error al modificar: {e}")
        else:
            print("⚠ Columna no válida.")
