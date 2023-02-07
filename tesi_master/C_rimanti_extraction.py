import re
import os
import json


def main():
    # ### INFERNO ###
    # # Directory
    # folder = 'Inferno'

    # #Comprehensive list of all the rimanti sublists by canto
    # inferno_rimanti_list = []

    # for filename in sorted(os.listdir(folder)):
    #     filepath = os.path.join(folder, filename)

    #     # Opening the canto in read mode
    #     with open (filepath, 'r') as testing:
    #         canto = testing.read()
        
    #     # Accounting for different writing
    #     characters = canto.replace('ï', 'i').replace('è', 'e').replace('ò', 'o').replace('í', 'i').replace('é', 'e').replace('ü', 'u').replace('à', 'a').replace('ô', 'o').replace('cavalieri', 'cavallieri')

    #     # Keeping only the rimante !this might not work for some rimanti!
    #     rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

    #     # Putting the rimanti in a list
    #     rimanti_list = rimanti.split("\n")
    #     # Making sure there are no empty entraces in the list
    #     if "" in rimanti_list:
    #         rimanti_list.remove("")

    #     # Cycling through the list of rimanti to aggregate the ones that rhyme
    #     rimanti_in_rima = []
    #     for rimante in range (1, len(rimanti_list), 3):
    #         # First set of rhymes A (B) A
    #         if rimante == 1:
    #             rimanti = rimanti_list[rimante-1], rimanti_list[rimante+1]
    #             rimanti_in_rima.append(rimanti)
    #         # Last set of rhymes X (Y) X
    #         if rimante == (len(rimanti_list)-3):
    #             rimanti = rimanti_list[rimante], rimanti_list[rimante+2]
    #             rimanti_in_rima.append(rimanti)
    #         # All of the rhymes in sets of three
    #         elif rimante != 1 and rimante != (len(rimanti_list)-3):
    #             rimanti = rimanti_list[rimante-3], rimanti_list[rimante-1], rimanti_list[rimante+1]
    #             rimanti_in_rima.append(rimanti)
    #     inferno_rimanti_list.append(rimanti_in_rima)

    # # Putting the rimanti in a txt document for check purposes
    # with open ('rimanti_inferno.txt', 'w') as check:
    #     for element in inferno_rimanti_list:
    #         single_element = str(element)
    #         check.write(single_element+'\n')


    ### PURGATORIO ###
    # Directory
    folder = 'Purgatorio'

    #Comprehensive list of all the rimanti sublists by canto
    purgatorio_rimanti_list = []

    for filename in sorted(os.listdir(folder)):
        filepath = os.path.join(folder, filename)

        # Opening the canti in read mode
        with open (filepath, 'r') as testing:
            canto = testing.read()

        # Accounting for different writing
        characters = canto.replace('ï', 'i').replace('è', 'e').replace('ò', 'o').replace('í', 'i').replace('é', 'e').replace('ü', 'u').replace('à', 'a').replace('ô', 'o')

        # Keeping only the rimante !this might not work for some rimanti!
        rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

        # Putting the rimanti in a list
        rimanti_list = rimanti.split("\n")
        # Making sure there are no empty entraces in the list
        if "" in rimanti_list:
            rimanti_list.remove("")

        # Cycling through the list of rimanti to aggregate the ones that rhyme
        rimanti_in_rima = []
        for rimante in range (1, len(rimanti_list), 3):
            # First set of rhymes A (B) A
            if rimante == 1:
                rimanti = rimanti_list[rimante-1], rimanti_list[rimante+1]
                rimanti_in_rima.append(rimanti)
            # Last set of rhymes X (Y) X
            if rimante == (len(rimanti_list)-3):
                rimanti = rimanti_list[rimante], rimanti_list[rimante+2]
                rimanti_in_rima.append(rimanti)
            # All of the rhymes in sets of three
            elif rimante != 1 and rimante != (len(rimanti_list)-3):
                rimanti = rimanti_list[rimante-3], rimanti_list[rimante-1], rimanti_list[rimante+1]
                rimanti_in_rima.append(rimanti)
        purgatorio_rimanti_list.append(rimanti_in_rima)

    # Putting the rimanti in a txt document for check purposes
    with open ('rimanti_purgatorio.txt', 'w') as check:
        for element in purgatorio_rimanti_list:
            single_element = str(element)
            check.write(single_element+'\n')     


    # ### PARADISO ###
    # # Directory
    # folder = 'Paradiso'

    # #Comprehensive list of all the rimanti sublists by canto
    # paradiso_rimanti_list = []

    # for filename in sorted(os.listdir(folder)):
    #     filepath = os.path.join(folder, filename)

    #     # Opening the canti in read mode
    #     with open (filepath, 'r') as testing:
    #         canto = testing.read()

    #     # Accounting for different writing
    #     characters = canto.replace('ï', 'i').replace('è', 'e').replace('ò', 'o').replace('í', 'i').replace('é', 'e').replace('ü', 'u').replace('à', 'a').replace('ô', 'o')

    #     # Keeping only the rimante !this might not work for some rimanti!
    #     rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

    #     # Putting the rimanti in a list
    #     rimanti_list = rimanti.split("\n")
    #     # Making sure there are no empty entraces in the list
    #     if "" in rimanti_list:
    #         rimanti_list.remove("")

    #     # Cycling through the list of rimanti to aggregate the ones that rhyme
    #     rimanti_in_rima = []
    #     for rimante in range (1, len(rimanti_list), 3):
    #         # First set of rhymes A (B) A
    #         if rimante == 1:
    #             rimanti = rimanti_list[rimante-1], rimanti_list[rimante+1]
    #             rimanti_in_rima.append(rimanti)
    #         # Last set of rhymes X (Y) X
    #         if rimante == (len(rimanti_list)-3):
    #             rimanti = rimanti_list[rimante], rimanti_list[rimante+2]
    #             rimanti_in_rima.append(rimanti)
    #         # All of the rhymes in sets of three
    #         elif rimante != 1 and rimante != (len(rimanti_list)-3):
    #             rimanti = rimanti_list[rimante-3], rimanti_list[rimante-1], rimanti_list[rimante+1]
    #             rimanti_in_rima.append(rimanti)
    #     paradiso_rimanti_list.append(rimanti_in_rima)

    # # Putting the rimanti in a txt document for check purposes
    # with open ('rimanti_paradiso.txt', 'w') as check:
    #     for element in paradiso_rimanti_list:
    #         single_element = str(element)
    #         check.write(single_element+'\n') 

    # ### ORLANDO FURIOSO ###
    # # Directory
    # folder = 'OF'

    # #Comprehensive list of all the rimanti sublists by canto
    # Of_rimanti_list = []

    # for filename in sorted(os.listdir(folder)):
    #     filepath = os.path.join(folder, filename)

    #     # Opening the canti in read mode
    #     with open (filepath, 'r') as testing:
    #         canto = testing.read()

    #     # Lowercase now because before the uppercase was used to split up the canti
    #     lowercase = canto.lower()

    #     # Accounting for different writing --> the problem with this is that the autors not only write some words differently, but within the works themselves a word can be spelled differently. How do I account for the magin of error? 
    #     characters = lowercase.replace('ï', 'i').replace('è', 'e').replace('ò', 'o').replace('í', 'i').replace('é', 'e').replace('ü', 'u').replace('à', 'a').replace('ô', 'o').replace('eterno', 'etterno').replace('camino', 'cammino').replace('castiga', 'gastiga')

    #     # Keeping only the rimante !this might not work for some rimanti!
    #     rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

    #     # Putting the rimanti in a list
    #     rimanti_list = rimanti.split("\n")
    #     # Making sure there are no empty entraces in the list
    #     if "" in rimanti_list:
    #         rimanti_list.remove("")

    #     # Cycling through the list of rimanti to aggregate the ones that rhyme
    #     rimanti_in_rima = []
    #     for rimante in range (0, len(rimanti_list), 8):
    #         # First set of rhymes A (B) A (B) A
    #         rimanti_A = rimanti_list[rimante], rimanti_list[rimante+2], rimanti_list[rimante+4]
    #         rimanti_in_rima.append(rimanti_A)
    #         # Second set B (A) B (A) B
    #         rimanti_B = rimanti_list[rimante+1], rimanti_list[rimante+3], rimanti_list[rimante+5]
    #         rimanti_in_rima.append(rimanti_B)
    #         # Last set C C
    #         rimanti_C = rimanti_list[rimante+6], rimanti_list[rimante+7]
    #         rimanti_in_rima.append(rimanti_C)
    #     Of_rimanti_list.append(rimanti_in_rima)

    # # Putting the rimanti in a txt document for check purposes
    # with open ('rimanti_of.txt', 'w') as check:
    #     for element in Of_rimanti_list:
    #         single_element = str(element)
    #         check.write(single_element+'\n')

    # with open ('inferno_rimanti.json', 'w') as inf:
    #     json.dump(inferno_rimanti_list, inf)

    with open ('purgatorio_rimanti.json', 'w') as purg:
        json.dump(purgatorio_rimanti_list, purg)

    # with open ('paradiso_rimanti.json', 'w') as para:
    #     json.dump(paradiso_rimanti_list, para)

    # with open ('orlando_rimanti.json', 'w') as orl:
    #     json.dump(Of_rimanti_list, orl)

if __name__ == "__main__":
    main()

