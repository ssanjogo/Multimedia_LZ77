from matplotlib import pyplot as plt
from LZ77Functions import LZ77Functions as lz77
import random
import time


def main():
    '''
    Comentario para ver si funciona.
    '''
    file_name = "../media/raw/hamlet_short.txt"
    file_name2 = "../media/raw/quijote_short.txt"

    ejemploUso1()
    ejemploUso2()
    ejemploUso3()
    outputHamlet = analisis(file_name)
    outputQuijote = analisis(file_name2)
    plot("(Hamlet)", outputHamlet)
    plot("(Quijote)", outputQuijote)


def ejemploUso1():
    print("FIRST EXAMPLE")
    random_data = "1111111100100111"

    compressed_data = lz77.lz77_compress(random_data, 4, 8)
    decompressed_data = lz77.lz77_decompress(compressed_data, 4, 8)

    assert random_data ==decompressed_data
    print("Original data:", random_data)
    print("Compressed data:", compressed_data)
    print("Decompressed data:", decompressed_data)
    print("Match between the original data and the decompressed data:", random_data == decompressed_data)
    print()


def ejemploUso2():
    print("SECOND EXAMPLE, with random data")
    random_data = ''.join([str(random.randint(0, 1)) for _ in range(250)])

    compressed_data = lz77.lz77_compress(random_data, 4, 8)
    decompressed_data = lz77.lz77_decompress(compressed_data, 4, 8)

    assert random_data == decompressed_data
    print("Original data:", random_data)
    print("Compressed data:", compressed_data)
    print("Decompressed data:", decompressed_data)
    print("Match between the original data and the decompressed data:", random_data == decompressed_data)
    print()


def ejemploUso3():
    nombre_archivo = "../media/raw/hamlet_short.txt"
    print("THIRD EXAMPLE, with a file, ", nombre_archivo)
    inicio = time.time()
    texto = lz77.read_file(nombre_archivo)
    if texto:
        binario = lz77.texto_a_ascii(texto)
        texto_nuevo = lz77.ascii_binario_a_texto(binario)
    fin = time.time()  # Tiempo de finalización
    tiempo_total = fin - inicio
    print("Tiempo total de ejecución:", tiempo_total, "segundos")
    print()


def analisis(file_name):
    '''
    
    '''
    analisis_results = []
    text = lz77.read_file(file_name)

    for i in range(2, 13):
        mdes = 2 ** i

        for j in range (2, 13):
            ment = 2 ** j

            if ((mdes > ment) and (mdes + ment <= len(text))):
                analisis_results.append(((mdes, ment), lz77.analisis(text, mdes, ment)))
    
    return analisis_results


def plot(file_name, outputAnalisis):
    mdes_values = []
    ment_values = []
    tiempos = []
    factores_compresion = []
    # Extraer valores de Mdes y Ment y sus correspondientes tiempos y factores de compresión
    for i in range(0, len(outputAnalisis)):
        mdes_values.append(outputAnalisis[i][0][0])
        ment_values.append(outputAnalisis[i][0][1])
        tiempos.append(outputAnalisis[i][1]['tiempo'])
        factores_compresion.append(outputAnalisis[i][1]['Ratio Compression'])

    # Crear plot para tiempo
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.scatter(mdes_values, ment_values, tiempos, c='r', marker='o')
    ax1.set_xlabel('Mdes')
    ax1.set_ylabel('Ment')
    ax1.set_zlabel('Tiempo (s)')
    ax1.set_title('Tiempo para distintos valores de Mdes y Ment', file_name)

    # Crear plot para factor de compresión
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, projection='3d')
    ax2.scatter(mdes_values, ment_values, factores_compresion, c='b', marker='x')
    ax2.set_xlabel('Mdes')
    ax2.set_ylabel('Ment')
    ax2.set_zlabel('Factor de Compresión')
    ax2.set_title('Factor de Compresión para distintos valores de Mdes y Ment', file_name)

    plt.show()


if __name__ == '__main__':
    main()
