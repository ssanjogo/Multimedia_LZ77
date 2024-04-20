import math


def validate_configuration(Ment, Mdes, data_length):
    if not (Ment & (Ment - 1) == 0 and Mdes & (Mdes - 1) == 0):
        raise ValueError("Ment and Mdes must be powers of 2")
    if Ment > Mdes:
        raise ValueError("Ment must be less than or equal to Mdes")
    if Mdes + Ment > data_length:
        raise ValueError("Mdes + Ment must be less than or equal to data length")
    

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

    validate_configuration(Ment, Mdes, len(data))
    compressed_data = str(data[0:Mdes])
    print("COMPRESSED_DATA_START")
    print(compressed_data)
    i = Mdes #letra por la que vamos
    while i < len(data):
        if (i > len(data)-Ment):
            print("Remaining data - "+str(data[i:len(data)]))
            compressed_data+=str(data[i:len(data)])
            return compressed_data

        match_found = False
        #Para j en rango 1 hasta el tamaño de la entrada o el maximo de la cadena... Para saber cuantos valores comparamos
        print(i)
        print(str(data[max(0, i - Mdes):max(0, i - Mdes)+Mdes])+" - "+str(data[i:i+min(Ment, len(data) - i)]))
        print()

        for j in range(min(Ment, len(data) - i),1,-1):
            print("Entrada: ")
            print(data[i:i+j])
            if j == 1:
                return "Literal"

            #Iteracion para comparar por la ventan deslizante
            for k in range(max(0, i - Mdes),max(0, i - Mdes)+Mdes):
                if j > i-k:
                    print("j :"+str(j)+" , i-k "+str(i-k))
                    break
                print("Letra :",str(i))
                print("tamaño comparar :",str(j))
                print("posicion deslizante :",str(k))
                print("Comparacion Deslizante")
                print(str(data[k:k+j]) +" --- "+str(data[i:i+j]))
                print()
                if data[i:i+j] == data[k:k+j]:
                    match_found = True
                    match_length = j
                    match_distance = i - k
                    compressed_data += '1'
                    print("Zero compressed")
                    print(format(0, '0' + str(int(math.log2(Ment))) + 'b'))
                    if match_length==Ment:
                        compressed_data +=format(0, '0' + str(int(math.log2(Ment))) + 'b')
                    else:
                        compressed_data +=format(match_length, '0' + str(int(math.log2(Ment))) + 'b')
                    if match_distance==Mdes:
                        compressed_data +=format(0, '0' + str(int(math.log2(Mdes))) + 'b')
                    else:
                        compressed_data +=format(match_distance, '0' + str(int(math.log2(Mdes))) + 'b')


                    print("compressed")
                    print(data[i:i+j])
                    print(data[k:k+j])
                    print("("+str(match_length)+","+str(match_distance)+")")
                    print(compressed_data)
                    i += match_length

                    break
            if match_found:
                break

        if not match_found:
            print("Literal")
            compressed_data += '0' + data[i]
            i += 1
        match_found=False

    return compressed_data[:Mdes] + compressed_data[Mdes:]

def lz77_decompress(compressed_data, Ment, Mdes): #WIP
    decompressed_data = compressed_data[:Mdes]
    i = Mdes
    print("########################################################################################")
    while i < len(compressed_data)-Ment:
        control_bit = compressed_data[i]
        if control_bit == '0':  # Literal
            print("control Bit 0: "+str(compressed_data[i:i+2]))
            decompressed_data += compressed_data[i+1]
            i += 2
        else:  # Tupla (L,D)
            print("control Bit 1: "+str(compressed_data[i:i+1]))
            length_bits = compressed_data[i+1:i+1+int(math.log2(Ment))]
            print("Len bits: "+str(int(math.log2(Ment))))
            distance_bits = compressed_data[i+1+int(math.log2(Ment)):i+1+int(math.log2(Ment))+int(math.log2(Mdes))]
            print("Dist bits: "+str(int(math.log2(Mdes))))
            length = int(length_bits, 2)
            distance = int(distance_bits, 2)
            print("len value "+ str(length))
            print("distance value "+ str(distance))
            if length == 0:
                length = Ment
            if distance == 0:
                distance = Mdes
            print("decompressed-pre")
            print(decompressed_data)
            tmp=decompressed_data
            print("tmp")
            print(tmp)
            for j in range(length):
                print(i,distance,j)
                print("value : "+str(tmp[-distance+j])+ str(-distance+j))
                decompressed_data += str(tmp[-distance+j])
            i += 1 + int(math.log2(Ment)) + int(math.log2(Mdes))
            print("decompressed-post")
            print(decompressed_data)
    print("FIN DEL WHILE")
    print(i)
    print(decompressed_data)
    print(compressed_data[i:])
    decompressed_data+=str(compressed_data[i:])
    return decompressed_data
