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

## Developed by 
- Oscar Blazquez Jimenez
- Sara San José Gómez