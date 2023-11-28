import os
import re

def main():

    # Script A: the files are cleaned up and prepared for splitting up by canto
    
    # Directory where the .txt files are contained
    folder = 'File_puliti/txt'
    # Cycling through the files
    for filename in os.listdir(folder):
        # Identifying the 'Commedia' files (the modifications to the texts will be different depending on the selected poem)
        if filename[0] == '0':
            filepath = os.path.join(folder, filename)
            
            with open ("File_puliti/txt/03_Paradiso.txt", "r") as If:
                Inferno = If.read()
    
            lowerCase = Inferno.lower()
            noCararatteri = re.sub(r"[^\w\s]", r" ", lowerCase)
            cantoPulito = re.sub(r"(\s+)(\n)", r"\2", noCararatteri)
            noSpacesBeforeWords = re.sub(r"(\n)(\s+)", r"\1", cantoPulito)
            noDoubleSpaces = re.sub(r"\s{2,}", r" ", noSpacesBeforeWords)

            if filename[1] == '1':
                with open("cleaned_up_files/canticaInferno.txt", "w") as testing:
                    testing.write(noDoubleSpaces)
            if filename[1] == '2':
                with open("cleaned_up_files/canticaPurgatorio.txt", "w") as testing:
                    testing.write(noDoubleSpaces)                    
            if filename[1] == '3':
                with open("cleaned_up_files/canticaParadiso.txt", "w") as testing:
                    testing.write(noDoubleSpaces)

    # Orlando Furioso
    with open ("File_puliti/txt/Orlando_furioso.txt", "r") as OF:
        Orlando = OF.read()

    # Because the canti in the Orlando are identified by being a string
    # of upper case letters, the first step of lower() is here avoided
    # to then better split the text
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