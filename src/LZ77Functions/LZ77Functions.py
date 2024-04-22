import math
import time


def validate_configuration(Ment, Mdes, data_length):
    """
    Validate the configuration parameters.

    Args:
        Ment (int): Number of bits for entropy coding.
        Mdes (int): Number of bits for describing the data.
        data_length (int): Length of the data to be encoded.

    Raises:
        ValueError: If the configuration is invalid.
    """
    
    if not (Ment & (Ment - 1) == 0 and Mdes & (Mdes - 1) == 0):                                         # Check if the input window and the sliding window are powers of 2. 
        raise ValueError("Ment and Mdes must be powers of 2")                                           # If so, raise an error. 
    if Ment > Mdes:                                                                                     # Check if the input window is bigger than the sliding window.
        raise ValueError("Ment must be less than or equal to Mdes")                                     # If so, raise an error. 
    if Mdes + Ment > data_length:                                                                       # Check if the sliding window  plus the input window is bigger than the length of the data.
        raise ValueError("Mdes + Ment must be less than or equal to data length")                       # If so, raise an error. 
    

def lz77_compress(data, Ment, Mdes):
    '''
    This method is used to compress some data with the lz77 algorithm.

    Args:
      data(string): The information that we want to compress.
      Ment(int): The input window.
      Mdes(int): The sliding window.

    Returns:
      compressed_data: Output of the data compressed.
      
    '''

    validate_configuration(Ment, Mdes, len(data))                                                       # Check if the configuration is valid. 
    compressed_data = str(data[0:Mdes])                                                                 # Inicialize the compressed data as the string of the sliding window.
    i = Mdes                                                                                            # Inicialize i as the sliding window. 
    while i < len(data):                                                                                # Iterate while the sliding window is smaller than the length of the data. 
        if (i > len(data)-Ment):                                                                        # Check if the length of the data minus the sliding window is smaller than i.                 
            compressed_data += str(data[i:len(data)])                                                   # We add the remaining data to the compressed data. 
            return compressed_data                                                                      # Give back the compressed data

        match_found = False                                                                             # Inicialize the variable to find a match as False. 

        for j in range(min(Ment, len(data) - i),1,-1):                                                  # For j in range 1 to the size of the input or the maximum of the string... To know how many values we are comparing.
            if j == 1:                                                                                  # Check if j is equal to 1. 
                return "Literal"                                                                        # If so, whe have a Literal. 

            for k in range(max(0, i - Mdes),max(0, i - Mdes)+Mdes):                                     # Iteration to find matches in the sliding window
                if j > i-k:                                                                             # Check if j is bigger than i - k.
                    break                                                                               # If so, finish the current iteration. 

                if data[i:i+j] == data[k:k+j]:                                                          # Check if there is a match of the data in our sliding window.
                    match_found = True                                                                  # We activate the boolean because we found a match. 
                    match_length = j                                                                    # We establish the length of the match. 
                    match_distance = i - k                                                              # We establish the match distance. 
                    compressed_data += '1'                                                              # Addition of a 1 to the compressed data  

                    if match_length == Ment:                                                            # In case that the match length is equal to the input window.
                        compressed_data += format(0, '0' + str(int(math.log2(Ment))) + 'b')             # We write the compressed data into the output
                        
                    else:                                                                               # If the match length is not equal to the input window size.
                        compressed_data += format(match_length, '0' + str(int(math.log2(Ment))) + 'b')  # We write the compressed data, with the match length. 

                    if match_distance == Mdes:                                                          # If the match distances is equal to the sliding window. 
                        compressed_data +=format(0, '0' + str(int(math.log2(Mdes))) + 'b')              # Write compressed data with no match distance.

                    else:                                                                               # If the match distance is not equal to the sliding window size.
                        compressed_data +=format(match_distance, '0' + str(int(math.log2(Mdes))) + 'b') # Write compressed data with match distance.

                    i += match_length                                                                   # We establish the begining of the sliding window.
                    break

            if match_found:                                                                             # In case that we found a match. 
                break                                                                                   # We finish the current iteration. 

        if not match_found:                                                                             # In case that we didn't find a match.
            compressed_data += '0' + data[i]                                                            # Addition of a literal to the compressed data. 
            i += 1                                                                                      # Add 1 to the begining of the sliding window. 
        match_found = False                                                                             # Reset the value of the match found.

    return compressed_data[:Mdes] + compressed_data[Mdes:]                                              # Give back the compressed data. 


def lz77_decompress(compressed_data, Ment, Mdes): 
    '''
    Decompress data using the LZ77 algorithm.

    Args:
        compressed_data (str): Compressed data to be decompressed.
        Ment (int): Number of bits for entropy coding.
        Mdes (int): Number of bits for describing the data.

    Returns:
        str: Decompressed data.

    '''
    decompressed_data = compressed_data[:Mdes]
    i = Mdes

    while i < len(compressed_data)-Ment:
        control_bit = compressed_data[i]

        if control_bit == '0':  # Literal
            decompressed_data += compressed_data[i+1]
            i += 2

        else:  # Tupla (L,D)
            length_bits = compressed_data[i+1:i+1+int(math.log2(Ment))]
            distance_bits = compressed_data[i+1+int(math.log2(Ment)):i+1+int(math.log2(Ment))+int(math.log2(Mdes))]
            length = int(length_bits, 2)
            distance = int(distance_bits, 2)

            if length == 0:
                length = Ment
            if distance == 0:
                distance = Mdes

            tmp=decompressed_data

            for j in range(length):
                decompressed_data += str(tmp[-distance+j])

            i += 1 + int(math.log2(Ment)) + int(math.log2(Mdes))

    decompressed_data+=str(compressed_data[i:])

    return decompressed_data


def analisis(text, Mdes, Ment):
    '''
    Method to give the information for the analysis of the data 

    Args:
        text (str): Data to be analized.
        Ment (int): Number of bits for entropy coding.
        Mdes (int): Number of bits for describing the data.

    Returns:


    '''
    #con distintos valores de Mdes y Ment entre 4 y 4096 y analizad el factor de compresión y el tiempo invertido
    compression_ratio = 0
    if Mdes < Ment:
        return "error"

    inicio = time.time()

    if text:
        binario = texto_a_ascii(text)
        compressed_data = lz77_compress(binario, Ment, Mdes)
        compression_ratio = len(text) / len(compressed_data)

    fin = time.time()  # Tiempo de finalización
    tiempo_total = fin - inicio
    return {'tiempo':tiempo_total, "Ratio Compression":compression_ratio, "Factor": str(compression_ratio)+":1"}


def texto_a_ascii(text):
    '''
    Convert text to ASCII representation.

    Args:
        text (str): Text to be converted to ASCII.

    Returns:
        text (str): List of ASCII values representing the input text.

    '''

    ascii_binario = ""                                                  # Initialize the string where we are going to write the ASCII.

    for caracter in text:                                               # We iterate trough the text character by character. 
        ascii_decimal = ord(caracter)                                   # Obtain the decimal ASCII value.
        ascii_binario += format(ascii_decimal, '08b')                   # Convert to a 8 bit binary and add it to the binary ASCII text. 

    return ascii_binario                                                # Give back the string text. 


def ascii_binario_a_texto(ascii_binario):
    '''
    Convert binary ASCII representation to text.

    Args:
        ascii_binario (str): Binary ASCII representation to be converted to text.

    Returns:
        str: Text decoded from the binary ASCII representation.

    '''
    text = ""                                                           # Initialize the string where we are going to write the ASCII.

    for i in range(0, len(ascii_binario), 8):                           # We iterate throug the binary ASCII, 8 bits each one.
        byte = ascii_binario[i:i+8]                                     # We take 8 bits together. 
        decimal = int(byte, 2)                                          # Convert from binary to decimal.
        caracter = chr(decimal)                                         # Convert from decimal to a ASCII character. 
        text += caracter                                                # Add the character to the output string. 

    return text                                                         # Give back the string text. 


def read_file(file_name):
    '''
    Read the contents of a file.

    Args:
        file_name (str): Name of the file to read.

    Returns:
        str: Contents of the file.

    '''
    try:
        with open(file_name, 'r', encoding='latin1') as archivo:                           # We open the file. 
            contenido = archivo.read()                                  # We read the file
        return contenido                                                # Give back the content of the file.
    
    except FileNotFoundError:                                           # In case that we don't find the file.
        print(f"No se encontró el archivo '{file_name}'")               # We print the exception. 
        return None                                                     # And return none. 
