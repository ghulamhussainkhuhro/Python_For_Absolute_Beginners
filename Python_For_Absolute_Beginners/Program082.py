"""
this mode allow us to read and overwrite at a single time
In this mode ointer will be at start of the file

Readiing : 
    CASE I: r --> to read the file
            opens text file for reading.
            The stream is positioned at the beginning of the file

Writing : 
    CASE II: w --> Truncate the file to zero length or create the text file (in case if not exists) for writing
                   The stream is positioned at the beginning of the file

    CASE III: a --> open for reading and writing. The file is created if it doeanot exists.
                    The stream is positioned at the end of the file. Subsequent writes to the file will always end up at the current end of file.


Reading and Writing :

    with truncating:

        CASE IV: w+ --> Open file for reading and writing. The file is created if doesnot exists, otherwise it is truncated 
                   The stream is positioned at the beginning of the file.
                   
                   

    without truncating:

        CASE V: r+ -->  opens text file for reading and writing..
            The stream is positioned at the beginning of the file



        CASE VI: a+ --> open for reading and writing. THe file is created if it doeanot exists.
                        The stream is positioned at the end of the file. Subsequent writes to the file will always end up at the current end of file.

"""

