import re

def main():

    with open ("/Users/tessacattaneo/Desktop/Dante_Rime/File_puliti/01_Inferno.txt", "r") as If:
        Inferno = If.read()
    
    lowerCase = Inferno.lower()
    noCararatteri = re.sub(r"[^\w\s]", r" ", lowerCase)
    cantoPulito = re.sub(r"(\s+)(\n)", r"\2", noCararatteri)
    noSpacesBeforeWords = re.sub(r"(\n)(\s+)", r"\1", cantoPulito)
    noDoubleSpaces = re.sub(r"\s{2,}", r" ", noSpacesBeforeWords)

    with open("canticaInferno.txt", "w") as testing:
        testing.write(noDoubleSpaces)


if __name__ == "__main__":
    main()