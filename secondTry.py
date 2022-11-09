import re

def main():
    ##### Step 1: Files clean up
    with open ("/Users/tessacattaneo/Desktop/Dante_Rime/Rimari/soloRime.txt", "r") as j:
        my_file = j.read()

    #Splitting the sicilian rhymes
    final_file = re.sub(r'\/', r'\n', my_file)

    first_list = final_file.split("\n")

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
    all_indexes_max = []

    # Loops through each subtable in "tabella"
    for i in range (0, len(tabella)):
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
    
    #print(all_indexes_max)

    # If x is the verse we are taking into consideration, the position inidexes correspond to verses as follows: 0 == x-3, 1 == x-2, 2 == x-1, 3 == x+1, 4 == x+2, 5 == x+3
    #Since the index of the all_indexes_max table correspond to x verse analised we should be able to reconstruct the scheme of the poem
    #Creating a new table to correlate the verses
    verses = []
    for a in range (len(all_indexes_max)):
        subtable = all_indexes_max[a]
        corresponding_verses = []
        for i in range (len(subtable)):
            if subtable[i] == 0:
                corresponding_verses.append(a)
                corresponding_verses.append(a-3)
            elif subtable[i] == 1:
                corresponding_verses.append(a)
                corresponding_verses.append(a-2)
            elif subtable[i] == 2:
                corresponding_verses.append(a)
                corresponding_verses.append(a-1)
            elif subtable[i] == 3:
                corresponding_verses.append(a)
                corresponding_verses.append(a+1)
            elif subtable[i] == 4:
                corresponding_verses.append(a)
                corresponding_verses.append(a+2)
            elif subtable[i] == 5:
                corresponding_verses.append(a)
                corresponding_verses.append(a+3)
        #Deleting the duplicates in the list
        corresponding_verses = list(dict.fromkeys(corresponding_verses))
        #print(corresponding_verses)
        verses.append(corresponding_verses)
    #print(verses)
    
    #Looping through the table, if the numbers duplicates themselves in the tables, they are merged
    #First finding the max length of the sub_lists in the list verses

    corresponding_verses = []
    for a in range (len(verses)):
        subtable = verses[a]
        for n in range (1, 7):
            try: 
                n_comp_subtable = a + n
                comp_subtable = verses[n_comp_subtable]
                if subtable > comp_subtable:
                    long_sub = subtable
                elif comp_subtable > subtable:
                    long_sub = comp_subtable
                for i in range (len(long_sub)):
                    try:
                        if subtable[i] == comp_subtable:
                            subtable.extend(comp_subtable)
                    except IndexError:
                        pass
            except IndexError:
                pass
        corresponding_verses.append(subtable)
    print(corresponding_verses)





if __name__ == "__main__":
    main()

## Problemi da risolvere: 