import re

FILEPATH = "/Users/tessacattaneo/Desktop/Mémoire/soloRime.txt"

def main():
    ##### Step 1: Files clean up
    my_file = open("soloRime.txt", "r")
    content = my_file.read()

    #Alcune rime presentano doppia occorrenza, sono state divise per comodità nonostante vengano considerate come la stessa rima
    final_file = re.sub(r'\/', r'\n', content)
    #print(final_file)

    first_list = final_file.split("\n")
    my_file.close
    #print(first_list)

    #Opening the canto III
    with open ("canto_3.txt", 'r') as canto3: 
        canto = canto3.read()

    #Cleaning up the canto from not useful characters
    #clean up with regex
    canto = canto.replace(",", "")
    canto = canto.replace(";", "")
    canto = canto.replace("\"", "")
    canto = canto.replace("?", "")
    canto = canto.replace(".", "")
    canto = canto.replace(":", "")
    canto = canto.replace(".", "")
    canto = canto.replace("!", "")
    canto = canto.replace("'", " ")

    cantoPulito = re.sub(r"(')(\s)(\n)", r"\3", canto)
    cantoPulito1 = re.sub(r"(\s+)(\n)", r"\2", cantoPulito)
    noDoubleSpaces = re.sub(r"\s{2,}", r" ", cantoPulito1)

    with open("canto3.txt", "w") as testing:
        testing.write(noDoubleSpaces)

    ##### Step 2: Extracting the word-rhymes from the file and putting them in a list
    #Only keeping the words-rhyme for purposes of clarity
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

    #Cycling through the word_rhymes
    #To check for the word-rhymes in the right order, substitute turned_list with words_list
    turned_rhymes = []
    for x in range (1, len(turned_list), 3):
        if x == 1:
            turned_rhyme = ""
            #print(turned_list[x-1], turned_list[x+1])
            if len(turned_list[x-1]) >= len(turned_list[x+1]):
                longest_word = turned_list[x-1]
                shorter_word = turned_list[x+1]
            elif len(turned_list[x+1]) >= len(turned_list[x-1]):
                longest_word = turned_list[x+1]
                shorter_word = turned_list[x-1]
            for letter in range (0, len(shorter_word), 1):
                if shorter_word[letter] == longest_word[letter]:
                    turned_rhyme += shorter_word[letter]
            turned_rhymes.append(turned_rhyme)
            #print(turned_rhyme)
        if x == (len(turned_list)-3): 
            turned_rhyme = ""
            #print(turned_list[x], turned_list[x+2])
            if len(turned_list[x]) >= len(turned_list[x+2]):
                longest_word = turned_list[x]
                shorter_word = turned_list[x+2]
            elif len(turned_list[x+2]) >= len(turned_list[x]):
                longest_word = turned_list[x+2]
                shorter_word = turned_list[x]  
            for letter in range (0, len(shorter_word), 1):
                if shorter_word[letter] == longest_word[letter]:
                    turned_rhyme += shorter_word[letter]
            turned_rhymes.append(turned_rhyme)
            #print(turned_rhyme)  
        elif x != 1 and x != (len(turned_list)-3):
            #print(turned_list[x - 3], turned_list[x-1], turned_list[x + 1])
            turned_rhyme = ""
            if len(turned_list[x - 3]) >= len(turned_list[x-1]) and len(turned_list[x - 3]) >= len(turned_list[x + 1]):
                longest_word = turned_list[x - 3]
            if len(turned_list[x-1]) >= len(turned_list[x - 3]) and len(turned_list[x-1]) >= len(turned_list[x + 1]):
               longest_word = turned_list[x-1]
            if len(turned_list[x + 1]) >= len(turned_list[x-1]) and len(turned_list[x + 1]) >= len(turned_list[x - 3]):
                longest_word = turned_list[x + 1]
            if len(turned_list[x-1]) <= len(turned_list[x + 1]) and len(turned_list[x-1]) <= len(turned_list[x - 3]):
                shorter_word = turned_list[x-1]
            if len(turned_list[x + 1]) <= len(turned_list[x-1]) and len(turned_list[x + 1]) <= len(turned_list[x - 3]):
                shorter_word = turned_list[x + 1]
            if len(turned_list[x - 3]) <= len(turned_list[x + 1]) and len(turned_list[x - 3]) <= len(turned_list[x-1]):
                shorter_word = turned_list[x - 3]
            for letter in range (0, len(shorter_word), 1):
                if letter == 0 and shorter_word[letter] == longest_word[letter]:
                    turned_rhyme += shorter_word[letter]
                if letter > 0 and shorter_word[letter] == longest_word[letter] and shorter_word[letter-1] == longest_word[letter-1]:
                    turned_rhyme += shorter_word[letter]
            turned_rhymes.append(turned_rhyme)
            
    #print(turned_rhymes) 
    rhymes_list = []
    for word in turned_rhymes:
        rhymes_list.append(word[::-1])
    print(rhymes_list)

#     ##### Step 4: Check against the list of rhymes given to me that the rhymes in the canto actually exist
#     with open ("soloRime.txt", 'r') as rime: 
#         solo_rime = rime.read()
#     final_rime_file = re.sub(r'\/', r'\n', solo_rime)
#     rime_list = final_rime_file.split('\n')

#     found_rhymes = []
#     for rimaCanto in range (0, len(rhymes_list), 1): 
#         for rima in range (0, len(rime_list), 1):
#             if rhymes_list[rimaCanto] == rime_list[rima]:
#                 found_rhymes.append(rhymes_list[rimaCanto])
#     print(len(found_rhymes))


# if __name__ == "__main__":
#     main()

## Problemi da risolvere: 
## 1. Il codice in questo momento identifica tutte le lettere uguali, non solo le rime a partire dalla fine e si ferma una volta che ne trova una sbagliata --> vedre se while potrebbe funzionare meglio? 