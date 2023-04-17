import json
import itertools
import math
import re

def main():

    # Importing the json files and opening it as a python list
    # Commedia
    Commedia = open('/Users/tessacattaneo/Desktop/Dante_Rime/dante_rimanti.json')
    dante_rimanti_list = json.load(Commedia)

    # Orlando Furioso
    OrlandoFurioso = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    ## TYPES ##
    # Putting in a list all groups of three rimanti in OF
    OF_three_rimanti_sorted = []
    for canto in of_rimanti_list:
        for sub_list in canto: 
            if len(sub_list) == 3:
                OF_three_rimanti_sorted.append(sorted(sub_list))
    print('tokens OF ' + str(len(OF_three_rimanti_sorted)))

    # Putting in a list all groups of three rimanti of Dante's
    D_three_rimanti_sorted = []
    for sub_list in dante_rimanti_list:
        if len(sub_list) == 3:
            D_three_rimanti_sorted.append(sorted(sub_list))
    print('tokens Cm ' + str(len(D_three_rimanti_sorted)))

    # Making sets of the two lists
    OF_set = set(tuple(i) for i in OF_three_rimanti_sorted)
    C_set = set(tuple(i) for i in D_three_rimanti_sorted)
    print('OF set ' + str(len(OF_set)))
    print('Cm set ' + str(len(C_set)))

    # For comparison entre paires
    D_pairs_list = []
    for sub_set in C_set:
        combinations = list(itertools.combinations(sub_set, 2))
        for combination in combinations:
            D_pairs_list.append(combination)
    D_set_pairs = set(tuple(i) for i in D_pairs_list)


    v_group_1 = 0
    v_group_2 = 0
    v_group_3 = 0
    v_group_4 = 0

    # First group: a group of three in Ariosto is present as a complete set of three in Dante (not ordered)
    group_two = []
    for sub_set in OF_set:
        if sub_set in C_set:
            v_group_1 += 1
        else:
            group_two.append(sub_set)
    print('First group: '+str(v_group_1))
    v_1_per = str(v_group_1/len(OF_set)*100)
    print('Percentage: '+v_1_per)

    # Second group: a group of three in Ariosto is composed by two or three groups of three in Dante
    group_three = []
    for sub_list in group_two:
        combinations = list(itertools.combinations(sub_list, 2))
        if combinations[0] in D_set_pairs and combinations[1] in D_set_pairs and combinations[2] in D_set_pairs:
            v_group_2 += 1
        else: 
            group_three.append(sub_list)
    print('Second group: '+str(v_group_2))
    v_2_per = str(v_group_2/len(OF_set)*100)
    print('Percentage: '+v_2_per)

    # Third group: a group of three in Ariosto (which could be split up into three sub-groups of two) is partially taken from Dante (partial citation)
    group_four = []
    for sub_list in group_three:
            combinations = list(itertools.combinations(sub_list, 2))
            if combinations[0] in D_set_pairs or combinations[1] in D_set_pairs or combinations[2] in D_set_pairs:
                v_group_3 += 1
            else:
                group_four.append(sub_list)
    print('Third group: '+str(v_group_3))
    v_3_per = str(v_group_3/len(OF_set)*100)
    print('Percentage: '+v_3_per)

    for sub_list in group_four:
        v_group_4 += 1
    print('Fourth group: '+str(v_group_4))
    v_4_per = str(v_group_4/len(OF_set)*100)
    print('Percentage: '+v_4_per)

    print(v_group_1 + v_group_2 + v_group_3 + v_group_4)

    OF_two_rimanti_sorted = []
    for canto in of_rimanti_list:
        for sub_list in canto: 
            if len(sub_list) == 2:
                OF_two_rimanti_sorted.append(sorted(sub_list))

    D_two_rimanti_sorted = []
    for sub_list in dante_rimanti_list:
        if len(sub_list) == 2:
            D_two_rimanti_sorted.append(sorted(sub_list))
    
    OF_two_set = set(tuple(i) for i in OF_two_rimanti_sorted)
    C_two_set = set(tuple(i) for i in D_two_rimanti_sorted)
    print(len(OF_two_set))
    print(len(C_two_set))

    v_group_two_1 = 0
    v_group_two_2 = 0
    v_group_two_3 = 0
    v_group_two_4 = 0

    group_two_2 = []
    for sub_set in OF_two_set:
        if sub_set in C_two_set:
            v_group_two_1 += 1
        else:
            group_two_2.append(sub_set)
    print(v_group_two_1)

    group_two_3 = []
    for sub_list in group_two_2:
        if sub_list in D_set_pairs:
            v_group_two_2 += 1
        else:
            group_two_3.append(sub_list)
    print(v_group_two_2)

    for sub_list in group_two_3:
        v_group_two_3 += 1

    print(v_group_two_1 + v_group_two_2 + v_group_two_3)

    







if __name__ == "__main__":
    main()