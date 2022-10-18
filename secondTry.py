import re

def main():
    ##### Step 1: Files clean up
    with open ("/Users/tessacattaneo/Desktop/Dante_Rime/Rimari/soloRime.txt", "r") as j:
        my_file = j.read()

    #Alcune rime presentano doppia occorrenza, sono state divise per comodità nonostante vengano considerate come la stessa rima
    final_file = re.sub(r'\/', r'\n', my_file)
    #print(final_file)

    first_list = final_file.split("\n")
    #print(first_list)

    #Opening the canto III
    with open ("canto_3.txt", 'r') as canto3: 
        canto = canto3.read()

    #Cleaning up the canto from not useful characters
    noCararatteri = re.sub(r"[^\w\s]", r" ", canto)

    cantoPulito = re.sub(r"(\s+)(\n)", r"\2", noCararatteri)
    noSpacesBeforeWords = re.sub(r"(\n)(\s)", r"\1", cantoPulito)
    noDoubleSpaces = re.sub(r"\s{2,}", r" ", noSpacesBeforeWords)

    with open("canto3.txt", "w") as testing:
        testing.write(noDoubleSpaces)

    ##### Step 2: Extracting the word-rhymes from the file and putting them in a list
    with open("canto3.txt", "r") as testing: 
        parole_rima = testing.read()

    paroleRima = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", parole_rima)

    with open ("canto_parole_rima.txt", "w") as testing: 
        testing.write(paroleRima)

    #Putting the words-rhyme in a list
    with open ("canto_parole_rima.txt", "r") as word_rhymes:
        word_rhyme = word_rhymes.read()
    words_list = word_rhyme.split("\n")
    if "" in words_list:
        words_list.remove("")
    else:
        print("The value is not present")
    #print(words_list)

    ##### Step 3: Finding the actual rhymes by comparing the word-rhymes that coincide
    #Cycling throgh the list and turning the rhyme-words around
    turned_list = []
    for word in words_list:
        turned_list.append(word[::-1])
    #print(turned_list)

    #Creating a two dimensional table
    tabella = []
    for i in range (0, len(words_list), 1):
        for a in range(0, len(words_list), 1):
            tabella.insert(i, [a])
    print(len(tabella))



    



if __name__ == "__main__":
    main()

## Problemi da risolvere: 
## Check that the number of rhymes found corresponds to number of lines of the canto -1 / 3? 