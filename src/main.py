from matplotlib import pyplot as plt
from LZ77Functions import LZ77Functions as lz77
import random
import time


def main():
    '''
    Main method, from where we are going to call the examples and other functions to show the correct behaviour of the compressor LZ77.
    '''

    firstExample()
    secondExample()

    randomData = ''.join([str(random.randint(0, 1)) for _ in range(1000)])
    outputRandomData = analisis(randomData, 1, 12)
    plotLength(outputRandomData)
    plotCompressionRatio("Random Data", outputRandomData)
    plotTimeAndCompression("Random Data", outputRandomData)

    hamletFile = "../media/raw/hamlet_short.txt"
    hamletData = lz77.read_file(hamletFile)  
    outputHamlet = analisis(hamletData, 2, 13)
    plotCompressionRatio("(Hamlet)", outputHamlet)
    plotTimeAndCompression("(Hamlet)", outputHamlet)

    quijoteFile = "../media/raw/quijote_short.txt"
    quijoteData = lz77.read_file(quijoteFile)  
    outputQuijote = analisis(quijoteData, 2, 13)
    plotCompressionRatio("(Quijote)", outputQuijote)
    plotTimeAndCompression("(Quijote)", outputQuijote)


def firstExample():
    '''
    Method to show the first example, with a established input (1111111100100111), and then we call the method to compress and decompress. 
    We have the slinding and input window set as:
        - Ment = 4
        - Mdes = 8
    '''

    print("FIRST EXAMPLE")
    random_data = "1111111100100111"                                                                        # Establish the value of the random data. 

    compressed_data = lz77.lz77_compress(random_data, 4, 8)                                                 # Compress the established data
    decompressed_data = lz77.lz77_decompress(compressed_data, 4, 8)                                         # Decompress the data previously compressed.

    assert random_data == decompressed_data                                                                 # Check if the initial random data is equal to the decompressed data.
    print("Original data:", random_data)                                                                    # Show the original data.
    print("Compressed data:", compressed_data)                                                              # Show the data compressed
    print("Decompressed data:", decompressed_data)                                                          # Show the decompressed data.
    print("The original data and the decompressed data are equal:", random_data == decompressed_data, "\n") # Show if the compressed data and the original data are equal.


def secondExample():
    '''
    Method to show the second example, with a random input data, and then we call the method to compress and decompress. 
    We have the slinding and input window set as:
        - Ment = 4
        - Mdes = 8
    '''

    print("SECOND EXAMPLE, with random data")
    random_data = ''.join([str(random.randint(0, 1)) for _ in range(250)])                                  # Establish the value of the random data, randomly. 

    compressed_data = lz77.lz77_compress(random_data, 4, 8)                                                 # Compress the established data
    decompressed_data = lz77.lz77_decompress(compressed_data, 4, 8)                                         # Decompress the data previously compressed.

    assert random_data == decompressed_data                                                                 # Check if the initial random data is equal to the decompressed data.
    print("Original data:", random_data)                                                                    # Show the original data.
    print("Compressed data:", compressed_data)                                                              # Show the data compressed
    print("Decompressed data:", decompressed_data)                                                          # Show the decompressed data.
    print("The original data and the decompressed data are equal:", random_data == decompressed_data, "\n") # Show if the compressed data and the original data are equal.


def analisis(data, power1, power2):
    '''
    Method to get the values of Mdes and Ment in a range of (4, 4096) and the value of the time and ratio 
    compression for those specific sliding and input window.

    Args:
        data (string): data to be compressed. 
        power1 (int): Value of the start of the range.
        power2 (int): Value of the end of the range. 
    
    Returns:
        dictionary: Gives back a list of tuples of tuple (Mdes, Ment) and a dictionary of the analisis with the 
              time necesary to do the compression, the ratio compression and the factor. 
    '''

    analisis_results = {}                                                                                   # Creation of the dictionary where we are going to save the values.

    for i in range(power1, power2):                                                                         # Iterate in order to get the powers of two for Mdes
        mdes = 2 ** i                                                                                       # Calculate the mdes, that is 2 up to a value i. 

        for j in range (power1, power2):                                                                    # Iterate in order to get the powers of two for Ment.
            ment = 2 ** j                                                                                   # Calculate the ment, that is 2 up to a value j. 

            if ((mdes >= ment) and (mdes + ment <= len(data))):                                             # Check if the sliding window is bigger than the input window and the sum of the sliding and input window is smaller or equal to the length of the data.
                analisis_results[(mdes, ment)] = lz77.analisis(data, mdes, ment)                            # We add to the dictionary the results obtained 
    
    return analisis_results                                                                                 # Return the list of results. 


def convertDictIntoLists(analisisDict):
    '''
    Method to convert the dictionary to diferent lists. 

    Args:
        analisisDict (dictionary): the values obtained in the analisis. 
    '''
    keys, mdes_values, ment_values, times, compressionFactors, originalLength, compressedLength = [], [], [], [], [], [], []

    for key, value in analisisDict.items():                                                                 # Iterate through the values that we obtained. 
        keys.append(key)
        mdes_values.append(key[0])                                                                          # Add the value of the sliding window.
        ment_values.append(key[1])                                                                          # Add the values of the input window.
        times.append(value['Time'])                                                                         # Add the time.
        compressionFactors.append(value['Compression Ratio'])                                               # Add the ratio compress. 
        originalLength.append(value['Text length'])
        compressedLength.append(value['Compressed data length'])

    return keys, mdes_values, ment_values, times, compressionFactors, originalLength, compressedLength
    

def plotLength(analisisDict):
    '''
    Method to plot length of the original and the compressed data. 

    Args:
        file_name (string) : Path where the file is located. 
        analisisDict (dictionary): the values obtained in the analisis. 
    '''

    keys, _, _, _, _, originalLength, compressedLength = convertDictIntoLists(analisisDict)                 # Get the lists.

    ancho_barra = 0.35                                                                                      # Width of the bars.
    posiciones = range(len(keys))                                                                           # Position of the axis x for the bars.

    fig, ax = plt.subplots()                                                                                # Create the figure and the axis.
    rects1 = ax.bar(posiciones, originalLength, ancho_barra, label='Longitud de Datos Originales')          # Create the bar for the original data.

    rects2 = ax.bar([pos + ancho_barra for pos in posiciones], compressedLength, ancho_barra, label='Longitud de Datos Comprimidos')    # Create the bar for the compressed data.

    ax.set_ylabel('Longitud')                                                                               # Set the label of the axis y. 
    ax.set_title('Data Comparison Original vs. Compress')                                                   # Set the title of the graph.
    ax.set_xticks([pos + ancho_barra / 2 for pos in posiciones])                                            # Set the position of the labels of the values.
    ax.set_xticklabels(keys, rotation = 75)                                                                 # Establish the labels for the values of the axis x, with a rotation of 75 degrees. 
    ax.legend()                                                                                             # Set the legend

    plt.show()                                                                                              # Show the plot. 
        
    
def plotCompressionRatio(file_name, analisisDict):
    '''
    Method to plot the compression ratio and print on the screen the sliding and input window with 
    maximum compression ratio, and also the values of it. 

    Args:
        file_name (string) : Path where the file is located. 
        analisisDict (dictionary): the values obtained in the analisis. 
    '''

    keys, _, _, _, compressionFactors, _, _ = convertDictIntoLists(analisisDict)

    maximum_value_key, maximum_value = max(analisisDict.items(), key=lambda item: item[1]['Compression Ratio'])
    print("Mdes and Ment of maximum compression ratio:", maximum_value_key)
    print("Values from the compression:\n - Time: ", maximum_value['Time'], "\n - Compression Ratio: ", maximum_value['Compression Ratio'],
          "\n - Compression Factor: ", maximum_value['Factor'], "\n - Text Length: ", maximum_value['Text length'],
          "\n - Compressed Data Length: ", maximum_value['Compressed data length'])

    fig, ax = plt.subplots()                                                                                # Creation of the bar graph. 
    x_pos = range(len(compressionFactors))                                                                  # Creation of a position range for the bars.

    ax.bar(x_pos, compressionFactors)                                                                       # Draw the bars. 

    ax.set_xlabel('Mdes and Ment')                                                                          # Set the label of the x axis. 
    ax.set_ylabel('Compression factor')                                                                     # Set the label of the y axis
    ax.set_title('Compression factor for ' + file_name)                                                     # Set the title of the figure. 

    ax.set_xticks(x_pos)                                                                                    # Set the position of the labels of the values.
    ax.set_xticklabels(keys, rotation=75)                                                                   # Establish the labels for the values of the axis x,  with a rotation of 75 degrees.

    plt.show()                                                                                              # Show the plot. 


def plotTimeAndCompression(file_name, analisisDict):
    '''
    Method to plot the time and compression ratio against the sliding and input window. 

    Args:
        file_name (string) : Path where the file is located. 
        analisisDict (dictionary): the values obtained in the analisis. 
    '''
    
    _, mdes_values, ment_values, times, compressionFactors, _, _ = convertDictIntoLists(analisisDict)       # Get the lists.
    
    fig1 = plt.figure()                                                                                     # Creation of the plot for the time.
    ax1 = fig1.add_subplot(111, projection='3d')                                                            # Add a 3d subplot. 
    ax1.scatter(mdes_values, ment_values, times, c='r', marker='o')                                         # Create the scatter plot.
    ax1.set_xlabel('Mdes')                                                                                  # Set x label.
    ax1.set_ylabel('Ment')                                                                                  # Set the y label.
    ax1.set_zlabel('Time (s)')                                                                              # Set the z label. 
    ax1.set_title('Time for different values of Mdes and Ment on the file: ' + file_name)                   # Set the title of the plot.

    fig2 = plt.figure()                                                                                     # Creation of the plot for the compression factor.
    ax2 = fig2.add_subplot(111, projection='3d')                                                            # Add a 3d subplot. 
    ax2.scatter(mdes_values, ment_values, compressionFactors, c='b', marker='x')                            # Create the scatter plot.
    ax2.set_xlabel('Mdes')                                                                                  # Set x label.
    ax2.set_ylabel('Ment')                                                                                  # Set the y label.
    ax2.set_zlabel('Compression factor')                                                                    # Set the z label. 
    ax2.set_title('Compression factor for different values of Mdes and Ment on the file: ' + file_name)     # Set the title of the plot.

    plt.show()                                                                                              # Show the plots


if __name__ == '__main__':
    main()
