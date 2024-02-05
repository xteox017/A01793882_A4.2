"""
Por Mateo Cruz L
Script - Conversión
"""
import sys
import time

def decimal_a_binario_recursivo(number):
    """
    Convierte decimal a representación binaria utilizando recursión.

    :param n: Número decimal a convertir.
    :return: Representación binaria como cadena.
    """
    if number == 0:
        return '0'
    return (
        '-' + decimal_a_binario_recursivo(-number) if number < 0
        else decimal_a_binario_recursivo(number // 2) + str(number % 2)
    )

def convertir_numeros(archivo_resultados, numero_archivo, ruta_archivo):
    """
    Convierte números en un archivo a bases binarias y hexadecimales.

    :param archivo_resultados: Archivo de resultados.
    :param numero_archivo: Número de archivo.
    :param ruta_archivo: Ruta al archivo que contiene una lista de números.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            numeros = [linea.strip() for linea in archivo]
    except FileNotFoundError:
        print(f"Error: Archivo '{ruta_archivo}' no encontrado.")
        return None

    resultados_binarios = []
    resultados_hexadecimales = []

    for _, numero in enumerate(numeros, start=1):
        try:
            num = int(numero)
            resultado_binario = decimal_a_binario_recursivo(num)
            resultado_hexadecimal = format(num if num >= 0 else (1 << 32) + num, 'X')
        except ValueError:
            print(f"Error: Se encontraron datos no válidos - '{numero}' en el archivo.")
            resultado_binario, resultado_hexadecimal = "#VALUE!", "#VALUE!"

        resultados_binarios.append(resultado_binario)
        resultados_hexadecimales.append(resultado_hexadecimal)

    archivo_resultados.write(f"\nNUMBER\tTC{numero_archivo}\tBIN\tHEX\n")

    for _, (binario, valor_hexadecimal, valor) in enumerate(
        zip(resultados_binarios, resultados_hexadecimales, numeros), start=1):
        if "Error: Se encontraron datos no válidos" in binario:
            tc_texto = valor
        else:
            tc_texto = f"{valor}"

        archivo_resultados.write(f"{_}\t{tc_texto}\t{binario}\t{valor_hexadecimal}\n")
        print(f"{_}\t{tc_texto}\t{binario}\t{valor_hexadecimal}")
    return None

def procesar_archivos(archivos, archivo_resultados):
    """
    Procesa una lista de archivos y escribe los resultados en un archivo de salida.

    :param archivos: Lista de archivos a procesar.
    :param archivo_resultados: Archivo de salida para escribir los resultados.
    """
    for numero_archivo, archivo in enumerate(archivos, start=1):
        print(f"\nProcesando archivo: {archivo}")
        convertir_numeros(archivo_resultados, numero_archivo, archivo)

def main():
    """
    Función principal para ejecutar el proceso de conversión y mostrar el tiempo transcurrido.
    """
    if len(sys.argv) < 2:
        print("Uso: python convertirNumeros.py archivo_1.txt archivo_2.txt archivo_3.txt ...")
        sys.exit(1)

    archivos_a_procesar = sys.argv[1:]

    tiempo_inicio = time.time()

    with open("ConversionResults.txt", 'w', encoding='utf-8') as archivo_resultados:
        procesar_archivos(archivos_a_procesar, archivo_resultados)

    tiempo_fin = time.time()

    print("Los resultados de la conversión se han escrito en ConversionResults.txt")

    tiempo_transcurrido = tiempo_fin - tiempo_inicio
    print(f"Tiempo transcurrido: {tiempo_transcurrido:.4f} segundos")

if __name__ == "__main__":
    main()
