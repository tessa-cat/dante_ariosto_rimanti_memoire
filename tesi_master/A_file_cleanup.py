import re

def main():

    # with open ("/Users/tessacattaneo/Desktop/tesi_master/File_puliti/txt/03_Paradiso.txt", "r") as If:
    #     Inferno = If.read()
    
    # lowerCase = Inferno.lower()
    # noCararatteri = re.sub(r"[^\w\s]", r" ", lowerCase)
    # cantoPulito = re.sub(r"(\s+)(\n)", r"\2", noCararatteri)
    # noSpacesBeforeWords = re.sub(r"(\n)(\s+)", r"\1", cantoPulito)
    # noDoubleSpaces = re.sub(r"\s{2,}", r" ", noSpacesBeforeWords)

    # with open("canticaParadiso.txt", "w") as testing:
    #     testing.write(noDoubleSpaces)

    with open ("/Users/tessacattaneo/Desktop/tesi_master/File_puliti/txt/orlando_furioso.txt", "r") as OF:
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

    with open("orlando_furioso.txt", "w") as testing:
        testing.write(noDoubleNewLines)





if __name__ == "__main__":
    main()