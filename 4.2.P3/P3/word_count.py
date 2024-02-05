"""
Conteo de Palabras
Por Mateo Cruz L

Este programa identifica todas las palabras distintas y su frecuencia
"""
import sys
import time

def contar_palabras(ruta_archivo):
    """
    Contar la frecuencia de palabras distintas en un archivo.

    Args:
        ruta_archivo (str): Ruta al archivo de entrada.

    Returns:
        dict: Un diccionario que contiene palabras distintas
        como claves y sus frecuencias como valores.
    """
    frecuencia_palabras = {}

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    palabra = palabra.lower()
                    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    except FileNotFoundError as error_archivo:
        print(f"Error: Archivo no encontrado: {error_archivo}")
        sys.exit(1)
    except UnicodeDecodeError as error_decodificacion:
        print(f"Error:Revisar la codificación UTF-8: {error_decodificacion}")
        sys.exit(1)

    return frecuencia_palabras

def manejar_error_inesperado(error):
    """
    Manejar errores inesperados imprimiendo un mensaje de error y saliendo.

    Args:
        error (Exception): El error inesperado.
    """
    print(f"Error Inesperado: {type(error).__name__}: {error}")
    sys.exit(1)

def imprimir_resultados(frecuencia_palabras):
    """
    Imprimir frecuencias de palabras en la consola con encabezados.

    Args:
        frecuencia_palabras (dict): Diccionario que contiene palabras distintas y sus frecuencias.
    """
    print("Etiquetas de Fila\tConteo")
    for palabra, conteo in frecuencia_palabras.items():
        print(f"{palabra}\t{conteo}")

def guardar_resultados(frecuencia_palabras, tiempo_transcurrido):
    """
    Guardar frecuencias de palabras y tiempo transcurrido en un archivo con encabezados.

    Args:
        frecuencia_palabras (dict): Diccionario que contiene palabras distintas y sus frecuencias.
        tiempo_transcurrido (float): Tiempo transcurrido para la ejecución.
    """
    with open("WordCountResults.txt", 'w', encoding='utf-8') as archivo_resultados:
        archivo_resultados.write("Etiquetas de Fila\tConteo\n")
        total = 0
        for palabra, conteo in frecuencia_palabras.items():
            archivo_resultados.write(f"{palabra}\t{conteo}\n")
            total += conteo

        archivo_resultados.write(f"\nTotal General: {total}\n")
        archivo_resultados.write(f"Tiempo Transcurrido: {tiempo_transcurrido:.2f} segundos")

def main():
    """
    Función principal para ejecutar el programa de conteo de palabras.
    """
    tiempo_inicio = time.time()

    try:
        if len(sys.argv) != 2:
            raise ValueError("Uso: python conteoPalabras.py archivoConDatos.txt")

        archivo_entrada = sys.argv[1]
        frecuencia_palabras = contar_palabras(archivo_entrada)
        imprimir_resultados(frecuencia_palabras)
        tiempo_transcurrido = time.time() - tiempo_inicio
        print(f"\nTiempo Transcurrido: {tiempo_transcurrido:.2f} segundos")
        guardar_resultados(frecuencia_palabras, tiempo_transcurrido)
    except FileNotFoundError as error:
        print(f"Error: Archivo no encontrado: {error}")
    except UnicodeDecodeError as error:
        print(f"Error: No se puede decodificar el archivo con codificación UTF-8: {error}")
    except ValueError as error:
        print(f"Error: Valor incorrecto: {error}")

if __name__ == "__main__":
    main()
