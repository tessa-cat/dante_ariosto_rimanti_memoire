import re
import json
import itertools

def main():

    # In this script a complete citation would correspond to either a group of three being cited in Ariosto or a whole group of two. To account for the difference in the two groups three separate lists will be created and checked against each other. The first containing couples extrated from groups of three rimanti (if a citation happens in this group it will count as 1/3 of a point); the second containing couples that appear as a whole group of rimanti by themselves AND as a part of a group of three (will also be counted as a third of a point); the third list will contain groups of twos which were originally so (this type of citation will be counted as one point, because complete)

    # Importing the json files and opening it as a python list
    # Inferno
    inferno = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/inferno_rimanti.json')
    inferno_rimanti_list = json.load(inferno)

    # Purgtorio
    purgatorio = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/purgatorio_rimanti.json')
    purgatorio_rimanti_list = json.load(purgatorio)

    # Paradiso
    paradiso = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/paradiso_rimanti.json')
    paradiso_rimanti_list = json.load(paradiso)

    # Orlando Furioso
    OrlandoFurioso = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # Creating a comprehensive list of all rimanti across the Commedia
    dante_rimanti = []
    # INFERNO
    for canto in inferno_rimanti_list :
        for gruppo_rimanti in canto:
            dante_rimanti.append(list(gruppo_rimanti))
    # PURGATORIO
    for canto in purgatorio_rimanti_list :
        for gruppo_rimanti in canto:
            dante_rimanti.append(list(gruppo_rimanti))
    # PARADISO
    for canto in paradiso_rimanti_list :
        for gruppo_rimanti in canto:
            dante_rimanti.append(list(gruppo_rimanti))
    print(len(dante_rimanti))

    # Creating two separate lists, one for groups of three rimanti and one for groups of two
    dante_two_rimanti = []
    dante_three_rimanti = []
    for rimanti in dante_rimanti: 
        if len(rimanti) == 2:
            dante_two_rimanti.append(sorted(rimanti))
        elif len(rimanti) == 3:
            dante_three_rimanti.append(sorted(rimanti))

    # Splitting the list composed by sub_lists of three rimanti in couples of rimanti that rhyme between them
    dante_three_to_two = []
    for rimanti in dante_three_rimanti:
        combinations = itertools.combinations(rimanti, 2)
        for combination in combinations:
            dante_three_to_two.append(sorted(list(combination)))

    # Comparing the two list we now have for overlay
    dante_rimanti_overlay = []   
    for rimanti_due in dante_two_rimanti:
        for rimanti_three in dante_three_to_two:
            if rimanti_due == rimanti_three:
                dante_rimanti_overlay.append(rimanti_due)
                dante_two_rimanti.remove(rimanti_due)
                break
    #print(len(dante_two_rimanti), len(dante_rimanti_overlay))

    # ORLANDO FURIOSO
    of_opera_completa = []
    for canto in of_rimanti_list :
        for gruppo_rimanti in canto:
            of_opera_completa.append(list(gruppo_rimanti))
    #print(len(of_opera_completa))

    
    # Creating two separate lists, one for groups of three rimanti and one for groups of two
    ariosto_two_rimanti = []
    ariosto_three_rimanti = []
    for rimanti in of_opera_completa: 
        if len(rimanti) == 2:
            ariosto_two_rimanti.append(sorted(rimanti))
        elif len(rimanti) == 3:
            ariosto_three_rimanti.append(sorted(rimanti))

    # Splitting the list composed by sub_lists of three rimanti in couples of rimanti that rhyme between them
    ariosto_three_to_two = []
    for rimanti in ariosto_three_rimanti:
        combinations = itertools.combinations(rimanti, 2)
        for combination in combinations:
            ariosto_three_to_two.append(sorted(list(combination)))

    # Comparing the two list we now have for overlay
    ariosto_rimanti_overlay = []   
    for rimanti_due in ariosto_two_rimanti:
        for rimanti_three in ariosto_three_to_two:
            if rimanti_due == rimanti_three:
                ariosto_rimanti_overlay.append(rimanti_due)
                ariosto_two_rimanti.remove(rimanti_due)
                break
    #print(len(ariosto_two_rimanti), len(ariosto_rimanti_overlay))

    # Now we will separetly calculate the citations by type of list, first the ones that once upon a time were composed by group of three rimanti, each citation will count one point
    tokens = 0
    for a_rimanti in ariosto_three_to_two:
        for d_rimanti in dante_three_to_two:
            if a_rimanti == d_rimanti:
                tokens += 1/3
                break

    for a_rimanti in ariosto_two_rimanti:
        for d_rimanti in dante_two_rimanti:
            if a_rimanti == d_rimanti: 
                tokens += 1
                break
    
    print(tokens)
    percentage = (tokens/(len(ariosto_three_to_two) + len(ariosto_three_to_two))) * 100
    print(percentage)

    

if __name__ == "__main__":
    main()