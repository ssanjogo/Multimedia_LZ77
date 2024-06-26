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
![alt text](<../media/raw/Data comparision original vs. compressed - RANDOM DATA.png>)

The red flashing line represents the length of the randomly generated binary code, while the blue vertical lines represent the length of the code after processing. We can see that in any case we get a compression better than the original text this is due to the generation of random values to lead to no matches or repetitions on the chain. 

#### Compression factor depending on (Mdes, Ment)
![alt text](<../media/raw/Compression factor depending on (Mdes, Ment) - RANDOM DATA.png>)

Mdes and Ment of maximum compression ratio: (2048, 16)
Values from the compression:
 - Time:  0.9408297538757324 
 - Compression Ratio:  0.7548878991469766 
 - Compression Factor:  0.7548878991469766:1 
 - Text Length:  10000 
 - Compressed Data Length:  13247


As we can see the compression ratio is always less than 1. Therefore, we are not compressing at all, quite the contrary.

#### Time depending on (Mdes, Ment)
![alt text](<../media/raw/Time depending on (Mdes, Ment) - RANDOM DATA.png>)


As we can see we find a runtime relationship. The larger the sliding window and the input window, the longer the algorithm takes. This is an exceptional case, as these results may vary if we find a large number of matches for large input windows.

In this experiment, being completely random and finding hardly any matches, smaller input windows have fewer characters to iterate through and get to the point of having to add the Literal to the string faster. That's why these runs are faster, but worse performance-wise.

### Plots for Hamlet text
--- 
#### Data comparision original vs. compressed
![alt text](<../media/raw/Data comparision original vs. compressed - HAMLET.png>)

If we take two sentences of average length, from the text as for example the following two:

BERNARDO 'Tis now struck twelve; get thee to bed, Francisco.

FRANCISCO For this relief much thanks: 'tis bitter cold, And I am sick at heart.

We count the number of characters. Number of characters = 141. 
We multiply this number by 8 because the text is encoded in ASCII 8 bits. Number of characters * 8 = 1128.

The most obvious matches in this text are the names of the characters, which are repeated every time they have a line of text.
In case you want to encode FRANCISCO, knowing that this word appears previously. So the size of the sliding window has to be close to or larger than the length of the two sentences. 

When we have a sliding window size close to this we get better values. The length of the compressed text is smaller than the original. 


#### Compression factor depending on (Mdes, Ment)
![alt text](<../media/raw/Compression factor depending on (Mdes, Ment) - HAMLET.png>)

Mdes and Ment of maximum compression ratio: (4096, 128)
Values from the compression:
 - Time:  7.741476774215698 
 - Compression Ratio:  1.1699383062254627 
 - Compression Factor:  1.1699383062254627:1 
 - Text Length:  8344 
 - Compressed Data Length:  7132

In this case we can see that there are some compression ratios that are bigger than 1. The best compression ratio is 1.69. The compressed data length is smaller than than text lenght, decreasing the text size by more than 1000 characters. 

#### Time depending on (Mdes, Ment)
![alt text](<../media/raw/Time depending on (Mdes, Ment) - HAMLET.png>)

We have an exponential trend in time as the sliding and input windows increase, and we have this trend periodically. Except for the input window and slider value of 4096 as the text size is approximately the size of the original text.

### Plots for Quijote text
--- 
#### Data comparision original vs. compressed
![alt text](<../media/raw/Data comparision original vs. compressed - QUIJOTE.png>)

In this case we can observe that with different combinations of the value of the sliding window and the input window, we get some compressions that are below the length of the original data length.

#### Compression factor depending on (Mdes, Ment)
![alt text](<../media/raw/Compression factor depending on (Mdes, Ment) - QUIJOTE.png>)

Mdes and Ment of maximum compression ratio: (4096, 64)
Values from the compression:
 - Time:  4.221064805984497 
 - Compression Ratio:  1.0809956538917425 
 - Compression Factor:  1.0809956538917425:1 
 - Text Length:  8208 
 - Compressed Data Length:  7593

In this case we can see that there are some compression ratios that are bigger than 1. The best compression ratio is 1.08. The compressed data length is smaller than than text lenght, decreasing the text size by about 800 characters. 


#### Time depending on (Mdes, Ment)
![alt text](<../media/raw/Time depending on (Mdes, Ment) - QUIJOTE.png>)

As in the previous example with the Hamlet text, we have an exponential trend in time as the sliding and input window increase periodically. Except for the input window and slider value of 4096 as the text size is approximately the size of the original text.


## Developed by 
- Oscar Blazquez Jimenez
- Sara San José Gómez
