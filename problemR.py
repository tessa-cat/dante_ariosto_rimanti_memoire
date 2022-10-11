import re

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

    #Cycling through the word_rhymes
    #To check for the word-rhymes in the right order, substitute turned_list with words_list
    turned_rhymes = []
    for x in range (1, len(turned_list), 3):
        #### First set of rhymes A (B) A
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
                if letter == 0 and shorter_word[letter] == longest_word[letter]:
                    turned_rhyme += shorter_word[letter]
                if letter > 0 and shorter_word[letter] == longest_word[letter] and shorter_word[letter-1] == longest_word[letter-1]:
                    turned_rhyme += shorter_word[letter]
            turned_rhymes.append(turned_rhyme)
            #print(turned_rhyme)
        ##### Last set of rhymes X (Y) X
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
                if letter == 0 and shorter_word[letter] == longest_word[letter]:
                    turned_rhyme += shorter_word[letter]
                if letter > 0 and shorter_word[letter] == longest_word[letter] and shorter_word[letter-1] == longest_word[letter-1]:
                    turned_rhyme += shorter_word[letter]
            turned_rhymes.append(turned_rhyme)
            #print(turned_rhyme)  
        ##### All the rhymes in sets of three
        elif x != 1 and x != (len(turned_list)-3):
            #print(turned_list[x - 3], turned_list[x-1], turned_list[x + 1])
            turned_rhyme = ""
            a = len(turned_list[x - 3])
            a_word = turned_list[x - 3]
            b = len(turned_list[x-1])
            b_word = turned_list[x-1]
            c = len(turned_list[x + 1])
            c_word = turned_list[x + 1]
            if a >= b and a >= c and b >= c: 
                longest_word = a_word
                shorter_word = c_word
                middle_word = b_word
            if a >= b and a >= c and c >= b: 
                longest_word = a_word
                shorter_word = b_word
                middle_word = c_word
            if b >= a and b >= c and a >= c:
                longest_word = b_word
                shorter_word = c_word
                middle_word = a_word
            if b >= a and b >= c and c >= a:
                longest_word = b_word
                shorter_word = a_word
                middle_word = c_word
            if c >= a and c >= b and a >= b:
                longest_word = c_word
                shorter_word = b_word
                middle_word = a_word
            if c >= a and c >= b and b >= a:
                longest_word = c_word
                shorter_word = a_word
                middle_word = b_word
            for letter in range (0, len(shorter_word), 1):
                ##### The first loop through the letters simply checks that the letters of all three word_rhymes coincide (this would also cover the cases, if there are any, of "tronche" rhymes, in which the last accented vowel is the last vowel, i.e. città)
                if letter == 0 and shorter_word[letter] == longest_word[letter] and middle_word[letter] == shorter_word[letter] and middle_word[letter] == longest_word[letter]:
                    turned_rhyme += shorter_word[letter]
                ##### For the remaining loops thorugh the letters of the words the program checks that not only by pair of letters but that also the precieding one coincides, so as to avoid that other letters are picked up by mistake 
                elif letter > 0 and shorter_word[letter] == longest_word[letter] == middle_word[letter] and shorter_word[letter-1] == longest_word[letter-1] == middle_word[letter-1]:
                    turned_rhyme += shorter_word[letter]
            turned_rhymes.append(turned_rhyme)
            
    #print(turned_rhymes) 
    rhymes_list = []
    for word in turned_rhymes:
        rhymes_list.append(word[::-1])
    #print(rhymes_list)


    ##### Step 4: Check against the list of rhymes given to me that the rhymes in the canto actually exist
    with open ("soloRime.txt", 'r') as rime: 
        solo_rime = rime.read()
    final_rime_file = re.sub(r'\/', r'\n', solo_rime)
    rime_list = final_rime_file.split('\n')

    found_rhymes = []
    for rimaCanto in range (0, len(rhymes_list), 1): 
        for rima in range (0, len(rime_list), 1):
            if rhymes_list[rimaCanto] == rime_list[rima]:
                found_rhymes.append(rhymes_list[rimaCanto])
        if rhymes_list[rimaCanto] not in found_rhymes:
            print(rhymes_list[rimaCanto] + ' is not listed as a rhyme. Please check for errors')
    #print(len(found_rhymes)) 
    #print(found_rhymes) 
    # print(len(found_rhymes))

    ##### Step 5: Putting back the rhymes in the canto
    #word_list is the list containing each word_rhyme, turned_list reversed
    #print(turned_list)

    for line in range (1, len(turned_rhymes), 1):
        if line == 1: 
            for letter in range (0, len(turned_rhymes[line]), 1):
                length = len(turned_rhymes[line])
                if turned_rhymes[letter] == turned_list[line-1][letter]:
                    turned_list[line-1].insert(length, "*")
    print(turned_list)


    



if __name__ == "__main__":
    main()

## Problemi da risolvere: 
## Check that the number of rhymes found corresponds to number of lines of the canto -1 / 3? 