"""
Calcular Estadísticas
por Mateo Cruz L

Este código extrae los números de un archivo de texto
y devuelve un informe estadístico que muestra
la media, moda, mediana, desviación estándar y varianza
de la lista de números proporcionada
"""

# P1 - Código utilizado para realizar algunas estadísticas
import time
import sys

def calcular_media(datos):
    """
    Calcular la media de una lista de números.
    """
    return sum(datos) / len(datos) if len(datos) > 0 else 0

def calcular_mediana(datos):
    """
    Calcular la mediana de una lista de números.
    """
    datos_ordenados = sorted(datos)
    total_datos = len(datos_ordenados)
    if total_datos % 2 == 0:
        medio1 = datos_ordenados[total_datos // 2 - 1]
        medio2 = datos_ordenados[total_datos // 2]
        return (medio1 + medio2) / 2
    return datos_ordenados[total_datos // 2]

def calcular_moda(datos):
    """
    Calcular la moda de una lista de números.
    """
    frecuencia = {}
    for num in datos:
        frecuencia[num] = frecuencia.get(num, 0) + 1
    max_freq = max(frecuencia.values())
    modas = [k for k, v in frecuencia.items() if v == max_freq]
    return modas[0] if modas else None  # Devolver la primera moda si existe

def calcular_desviacion_estandar(datos, media):
    """
    Calcular la desviación estándar de una lista de números.
    """
    varianza = sum((x - media) ** 2 for x in datos) / len(datos) if len(datos) > 0 else 0
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar

def calcular_varianza(datos, media):
    """
    Calcular la varianza de una lista de números.
    """
    return sum((x - media) ** 2 for x in datos) / len(datos) if len(datos) > 0 else 0

def manejar_datos_invalidos(dato_str):
    """
    Manejar datos inválidos intentando convertirlos a punto flotante.
    Si la conversión falla, eliminar caracteres no numéricos y contar los datos.
    """
    try:
        # Attempt to convert with both separators
        return float(dato_str.replace(';', '.').replace(',', '.'))
    except ValueError:
        valor_numerico = ''.join(char if char.isdigit()
                                 or char in ('.', ',')
                                 else '' for char in dato_str)
        if valor_numerico:
            print(f"Dato no numérico convertido: {dato_str} a {valor_numerico}")
            return float(valor_numerico.replace(',', '.'))
        print(f"Ignorando dato inválido: {dato_str}")
        return None

def leer_datos_desde_archivo(nombre_archivo):
    """
    Leer datos desde un archivo y manejar entradas inválidas.
    """
    datos = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            for item in linea.split():
                dato_valido = manejar_datos_invalidos(item)
                if dato_valido is not None:
                    datos.append(dato_valido)
    return datos

def procesar_archivo(nombre_archivo):
    """
    Procesar un solo archivo y devolver estadísticas.
    """
    tiempo_inicio = time.time()

    datos = leer_datos_desde_archivo(nombre_archivo)

    cantidad = len(datos)
    media_valor = calcular_media(datos)
    mediana_valor = calcular_mediana(datos)
    moda_valor = calcular_moda(datos)
    desviacion_estandar_valor = calcular_desviacion_estandar(datos, media_valor)
    varianza_valor = calcular_varianza(datos, media_valor)

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return (
        cantidad, media_valor, mediana_valor, moda_valor,
        desviacion_estandar_valor, varianza_valor, tiempo_transcurrido, timestamp
    )

def main():
    """
    Función principal para calcular y mostrar estadísticas para múltiples archivos.
    """
    if len(sys.argv) < 2:  # Change the condition here
        print("Uso: python computeStatistics.py <nombre_archivo>")
        sys.exit(1)

    # Preparar datos para StatisticsResults.txt
    headers = [
        "TC", "CANTIDAD", "MEDIA", "MEDIANA", "MODA",
        "SD", "VAR", "Tiempo Transcurrido", "Marca de Tiempo"
    ]
    resultados_archivos = []

    # Procesar archivos TC1 a TC7
    for i in range(1, 8):
        nombre_archivo = f"TC{i}.txt"
        resultado = [f"TC{i}"] + list(map(str, procesar_archivo(nombre_archivo)))
        resultados_archivos.append(resultado)

    # Mostrar la tabla
    longitudes_maximas = [
        max(len(str(row[i])) for row in resultados_archivos) for i in range(len(headers))
    ]

    # Imprimir encabezados
    print('\t'.join(f"{header:<{max_length}}" for header,
                    max_length in zip(headers, longitudes_maximas)))

    # Imprimir datos
    for row in resultados_archivos:
        print('\t'.join(f"{value:<{max_length}}" for value,
                        max_length in zip(row, longitudes_maximas)))

    # Guardar la tabla en un archivo
    with open("StatisticsResults.txt", 'w', encoding='utf-8') as archivo_resultado:
        # Escribir encabezados
        archivo_resultado.write('\t'.join(headers) + '\n')
        # Escribir datos
        for row in resultados_archivos:
            archivo_resultado.write('\t'.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()
