from LZ77Functions import LZ77Functions as lz77


def main():
    ejemploUso1()
    ejemploUso2()


def ejemploUso1():
    # Ejemplo de uso
    #random_data = ''.join([str(random.randint(0, 1)) for _ in range(20)])
    random_data = "1111111100100111"
    print("Random data", random_data)
    compressed_data = lz77.lz77_compress(random_data, 4, 8)
    print(compressed_data)
    assert "111111110000111011111" == compressed_data
    111111110000111110111
    111111110000111011
    print(compressed_data)
    print(1111111100100111)
    decompressed_data = lz77.lz77_decompress(compressed_data, 4, 8)
    print(decompressed_data)
    assert random_data ==decompressed_data
    print("Datos originales:", random_data)
    print("Datos comprimidos:", compressed_data)
    print("Datos descomprimidos:", decompressed_data)
    print("Coinciden los datos originales con los descomprimidos:", random_data == decompressed_data)

def ejemploUso2():
    random_data = ''.join([str(random.randint(0, 1)) for _ in range(250)])

    compressed_data = lz77.lz77_compress(random_data, 4, 8)
    decompressed_data = lz77.lz77_decompress(compressed_data, 4, 8)

    assert random_data ==decompressed_data
    print("Datos originales:", random_data)
    print("Datos comprimidos:", compressed_data)
    print("Datos descomprimidos:", decompressed_data)
    print("Coinciden los datos originales con los descomprimidos:", random_data == decompressed_data)