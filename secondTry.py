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

    #Creating a table
    tabella = []
    # for i in range (0, len(words_list), 1):
    #         tabella.append(i)
    # print(tabella)

    for word in range (0, len(turned_list), 1):
        tabella1 = []
        for number in range (-3, 4, 1):
            if number != 0:
                try:
                    turned_rime = ""
                    comparison_word = turned_list[word+number]
                    len_comparison_word = len(comparison_word)
                    analized_word = turned_list[word]
                    len_analized_word = len(analized_word)
                    if len_analized_word >= len_comparison_word: 
                        longer_word = analized_word
                        shorter_word = comparison_word
                    elif len_comparison_word >= len_analized_word:
                        longer_word = comparison_word
                        shorter_word = analized_word
                    for letter in range (0, len(shorter_word), 1):
                        if letter == 0 and shorter_word[letter] == longer_word[letter]:
                            turned_rime += shorter_word[letter]
                        elif letter > 0 and shorter_word[letter] == longer_word[letter] and shorter_word[letter-1] == longer_word[letter-1]:
                            turned_rime += shorter_word[letter]
                    tabella1.append(len(turned_rime))  
                except IndexError:
                    pass
        tabella.insert(word, tabella1)

    print(tabella)
    #print(len(tabella))

    #Interacting with the table

    """
    index_table = []
    #for line in range (0, len(tabella), 1): 
    for line in range (0, 5): 
        indexes = []

        if line < (len(tabella)-3):
            position = tabella[line]
            max_value = max(position)
            for entry in range (0, len(position), 1):
                if max_value == position[entry]:
                    print(position.index(position[entry]))
                    indexes.append(position.index(position[entry]))
        index_table.insert(line, indexes)
    """

    # idk
    all_indexes_max = []

    # Loops through each subtable in "tabella"
    for i in range (0, 5):
        indexes_max = []

        # Subtable
        subtable = tabella[i]

        # Find max in subtable
        max_in_subtable = max(subtable)
        
        # Find each value that "is" the max
        for j in range(len(subtable)):
            # If the value of the index of the subtable
            # is equal to the found max
            if subtable[j] == max_in_subtable:
                # Let's add it to "index_max"
                indexes_max.append(j)

        # Append to when all indexes were found
        all_indexes_max.append(indexes_max)
        
    # table = []
    # for line in range (0, len(tabella), 1):
    #     if line < (len(tabella)-3):
    #         position = tabella[line]
    #         a = position.index(max(position))
    #         table.append(a)
    #print(index_table)





if __name__ == "__main__":
    main()

## Problemi da risolvere: 