import os
import re

def main():

    # Script A: the files are cleaned up and prepared for splitting up by canto
    ## The docx files of the Commedia were provided by Giacomo Stanga, while the digital edition of Furioso was downloaded from liberliber.it and converted to txt
    
    # Directory where the .txt files are contained
    folder = 'File_puliti/txt'
    # Cycling through the files
    for filename in os.listdir(folder):
        # Identifying the 'Commedia' files
        if filename[0] == '0':
            filepath = os.path.join(folder, filename)
            
            with open (filepath, "r") as text:
                Commedia_text = text.read()
    
            lowerCase = Commedia_text.lower()
            noCararatteri = re.sub(r"[^\w\s]", r" ", lowerCase)
            cantoPulito = re.sub(r"(\s+)(\n)", r"\2", noCararatteri)
            noSpacesBeforeWords = re.sub(r"(\n)(\s+)", r"\1", cantoPulito)
            noDoubleSpaces = re.sub(r"\s{2,}", r" ", noSpacesBeforeWords)

            if filename[1] == '1':
                with open("cleaned_up_files/Inferno.txt", "w") as testing:
                    testing.write(noDoubleSpaces)
            if filename[1] == '2':
                with open("cleaned_up_files/Purgatorio.txt", "w") as testing:
                    testing.write(noDoubleSpaces)                    
            if filename[1] == '3':
                with open("cleaned_up_files/Paradiso.txt", "w") as testing:
                    testing.write(noDoubleSpaces)

    # Orlando Furioso
    with open ("File_puliti/txt/Orlando_furioso.txt", "r") as OF:
        Orlando = OF.read()

    # Because the beginning of a canto in Orlando Furioso is identified by a string of upper case letters, the first step of lower() is here avoided to then better split the text
    noCararatteri = re.sub(r"[^\w\s]", r" ", Orlando)
    noNumeri = re.sub(r"([0-9]+)(\n)", r"\2", noCararatteri)
    cantoPulito = re.sub(r"(\s+)(\n)", r"\2", noNumeri)
    noSpacesBeforeWords = re.sub(r"(\n)(\s+)", r"\1", cantoPulito)
    noDoubleSpaces = re.sub(r"\s{2,}", r" ", noSpacesBeforeWords)
    noDoubleNewLines = re.sub(r"(\n){2,}", r"\1", noDoubleSpaces)

    with open("cleaned_up_files/orlando_furioso.txt", "w") as testing:
        testing.write(noDoubleNewLines)


if __name__ == "__main__":
    main()