# Multimedia_LZ77
## Description
The idea of this code is to do a LZ77 codification. 

In the following text we are going to explain how the algorithm will work. Binary string with:
- Header with the first "Mdes" bits of the input data
- From this header, the control bit must be inserted.
    - "0" for literals.
    - "1" for tuples (L,D)
- Store matches of L = 1 as literals.
- Store matches (with L > 1) as tuples (L, D) encoded in fixed-length binary format (log2(Ment) + log2(Mdes) bits in total)
- The search for matches ends when the remaining bits to be processed are fewer than Ment. In such case, store these remaining bits at the end of the compressed string.

## Things to develop and study
In the first part of the work (a), we are asked to do:
    - the codification of a binary data compressor/decompressor using the LZ-77 algorithm.
    - Research if it is possible to have a chain of data longer than the compressed data.

In the second part of the work (b), we are asked to do:
    - Develop the compressor and decompressor for strings, long texts instead of only binary numbers.
    - Compare the results. 

## Input and output data
- Input and output data format will be a binary string (ones and zeros) of arbitrary length.
- We will have the possibility to configure variable Input Window Length (Ment) and Sliding Window Length (Mdes).
For a valid configuration control, Ment and Mdes must be:
- powers of 2
- Ment <= Mdes
- Mdes + Ment <= length of data to be compressed

## Execution of the code
First you have to install the requirements.txt located in the main directory using this code: 

> 
    pip install -r requirements.txt

To run the code you have to go to the folder that contains the main.py, in this case the address of this folder is: MULTIMEDIA_LZ77/src/ and in this directory we will find the main.py
The next step is to execute the main.py file using the command:

> 
    python main.py

*Maybe you have to use python3 instead of python. 

## Execution of the documentation
To run the documentation using mk you must do the following, from the root folder:

***Important**: you must install the requirements first*.

> 
    mkdocs build
    

> 
    mkdocs serve

When you run the serve, you will get the web page address on the command line, so you have to open it on your browser. 

## Analysis of the plots
For this exercise we did different plots. 


### Plots for RANDOM DATA
--- 
#### Data comparision original vs. compressed
![alt text](<media/raw/Data comparision original vs. compressed - RANDOM DATA.png>)

We can see that in any case we get a compression better than the original text this is due to the generation of random values to lead to no matches or repetitions on the chain. 

#### Compression factor depending on (Mdes, Ment)
![alt text](<media/raw/Compression factor depending on (Mdes, Ment) - RANDOM DATA.png>)

Mdes and Ment of maximum compression ratio: (2048, 16)
Values from the compression:
 - Time:  0.9408297538757324 
 - Compression Ratio:  0.7548878991469766 
 - Compression Factor:  0.7548878991469766:1 
 - Text Length:  10000 
 - Compressed Data Length:  13247

#### Time depending on (Mdes, Ment)
![alt text](<media/raw/Time depending on (Mdes, Ment) - RANDOM DATA.png>)




### Plots for Hamlet text
--- 
#### Data comparision original vs. compressed
![alt text](<media/raw/Data comparision original vs. compressed - HAMLET.png>)

Si cojemos dos frases de longitud promedio, del texto como por ejemplo las dos siguientes:

BERNARDO 'Tis now struck twelve; get thee to bed, Francisco.
FRANCISCO For this relief much thanks: 'tis bitter cold, And I am sick at heart.

Contamos el numero de caracteres. Numero de caracteres = 141. 
Multiplicamos este numero por 8 debido a que el texto esta codificado en ASCII 8 bits. Numero de caracteres * 8 = 1128.

Las coincidencias mas obvias en este texto son los nombres de los personajes, que se repiten cada vez que estos tienen una linia de texto.
En caso de querer codificar FRANCISCO, se que esta palabra ha salido en dos frases de distancia. De manera que el tamaño de la ventana deslizante tiene que ser de un tamaño cercano o mayor al tamaño de las dos frases. 

Cuando tenemos un tamaño de ventana deslizante proximo a este optenemos mejores valores. 


#### Compression factor depending on (Mdes, Ment)
![alt text](<media/raw/Compression factor depending on (Mdes, Ment) - HAMLET.png>)

Mdes and Ment of maximum compression ratio: (4096, 128)
Values from the compression:
 - Time:  7.741476774215698 
 - Compression Ratio:  1.1699383062254627 
 - Compression Factor:  1.1699383062254627:1 
 - Text Length:  8344 
 - Compressed Data Length:  7132



#### Time depending on (Mdes, Ment)
![alt text](<media/raw/Time depending on (Mdes, Ment) - HAMLET.png>)




### Plots for Quijote text
--- 
#### Data comparision original vs. compressed
![alt text](<media/raw/Data comparision original vs. compressed - QUIJOTE.png>)

#### Compression factor depending on (Mdes, Ment)
![alt text](<media/raw/Compression factor depending on (Mdes, Ment) - QUIJOTE.png>)

Mdes and Ment of maximum compression ratio: (4096, 64)
Values from the compression:
 - Time:  4.221064805984497 
 - Compression Ratio:  1.0809956538917425 
 - Compression Factor:  1.0809956538917425:1 
 - Text Length:  8208 
 - Compressed Data Length:  7593


#### Time depending on (Mdes, Ment)
![alt text](<media/raw/Time depending on (Mdes, Ment) - QUIJOTE.png>)



## Developed by 
- Oscar Blazquez Jimenez
- Sara San José Gómez