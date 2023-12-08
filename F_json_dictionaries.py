import json
import itertools
import math

def main():

    # Script F: In this script json dictionaries contaning the possible reprisals grouped in 5 different categories are created

    # Importing the json files and opening it as a python list
    # Inferno
    inferno = open('json_files/rimanti_json/inferno_rimanti.json')
    inferno_rimanti_list = json.load(inferno)

    # Purgtorio
    purgatorio = open('json_files/rimanti_json/purgatorio_rimanti.json')
    purgatorio_rimanti_list = json.load(purgatorio)

    # Paradiso
    paradiso = open('json_files/rimanti_json/paradiso_rimanti.json')
    paradiso_rimanti_list = json.load(paradiso)

    # Orlando Furioso
    OrlandoFurioso = open('json_files/rimanti_json/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # Creating a comprehensive list of all the rimantis in Dante's Divina Commedia
    dante_canti = []
    dante_rimanti = []
    for canto in inferno_rimanti_list:
        dante_canti.append(canto)
        for sub_list in canto: 
            dante_rimanti.append(sub_list)
    for canto in purgatorio_rimanti_list:
        dante_canti.append(canto)
        for sub_list in canto: 
            dante_rimanti.append(sub_list)
    for canto in paradiso_rimanti_list:
        dante_canti.append(canto)
        for sub_list in canto: 
            dante_rimanti.append(sub_list)

    with open ('json_files/rimanti_json/dante_rimanti.json', 'w') as dante:
        json.dump(dante_rimanti, dante)

    # Separating the groups of two rimanti's from the the groups of three rimanti, first for the Divina Commedia than for the Orlando Furioso
    # Divina Commedia
    dante_two_rimanti = []
    dante_three_riamnti = []
    for rimanti in dante_rimanti:
        if len(rimanti) == 2:
            dante_two_rimanti.append(sorted(rimanti))
        if len(rimanti) == 3:
            dante_three_riamnti.append(sorted(rimanti))

    # Orlando furioso
    a_two_rimanti = []
    a_three_rimanti = []
    for canto in of_rimanti_list:
        for sub_list in canto:
            if len(sub_list) == 2:
                a_two_rimanti.append(sorted(sub_list))
            if len(sub_list) == 3:
                a_three_rimanti.append(sorted(sub_list))

    set_group_two = set(tuple(i) for i in a_two_rimanti)
    print('set_group_two len', len(set_group_two))

    # Switching the list from tokens to types
    set_group_three = set(tuple(i) for i in a_three_rimanti)

    # Maaking the set of tuples in a list so as to facilitate the comparaison within lists
    unset = []
    for rimanti in set_group_three:
        unset.append(list(rimanti))

    # Category A: a group of three Furioso rimanti corresponds to a group of three Divina Commedia rimanti
    three_rimanti_sorted = []
    for of_sublist in set_group_three:
        for d_sublist in dante_rimanti:
            if sorted(of_sublist) == sorted(d_sublist):
                three_rimanti_sorted.append(sorted(of_sublist))
                break
    # Length: 406

    # Category B: a group of three Furioso rimanti corresponds to subgroups of different groups in the Divina Commedia
    # First a list of all the groups of three rimanti which were not in the previous category is created
    three_a = []
    for of_rimanti in unset:
        if of_rimanti not in three_rimanti_sorted:
            three_a.append(of_rimanti)
    # Length: 7418

    # Creating combinations (couples of rimanti) out of all the rimanti in the Divina Commedia 
    dante_paires = []
    for rimanti in dante_rimanti:
        x_combinations = list((itertools.combinations(sorted(rimanti), 2)))
        dante_paires.append(x_combinations)

    # Creating a flattened list of tuples 
    dante_flattened = []
    for sub_list in dante_paires:
        for sub_tuple in sub_list:
            dante_flattened.append(sub_tuple)

    # The group of three rimanti analized is divided into three couples of rimanti, i.e. the group ABC would become AB, AC, BC. To check that all three rimanti are also in Dante (but divided among different groups) the script makes sure that two out of three couples appear also in Dante. The group is then added to a list as are the dantean's couples (so as to facilitate the creation of the json dictionary)
    captured = []
    captured_dante = []
    for a_list in three_a:
        a_combinations = list(itertools.combinations(sorted(a_list), 2))
        if (a_combinations[0] in dante_flattened and a_combinations[1] in dante_flattened):
            captured.append(a_list)
            captured_dante.append([a_list, a_combinations[0], a_combinations[1]])
        elif (a_combinations[0] in dante_flattened and a_combinations[2] in dante_flattened):
            captured.append(a_list)
            captured_dante.append([a_list, a_combinations[0], a_combinations[2]])
        elif (a_combinations[1] in dante_flattened and a_combinations[2] in dante_flattened):
            captured.append(a_list)
            captured_dante.append([a_list, a_combinations[1], a_combinations[2]])            
    # Length of captured: 930

    # Category C: two rimanti of a group of three Furioso rimanti correspond to two rimanti of a group of two or three Divina Commedia rimanti
    # A list of all the groups of three rimanti which were not in the previous categories is created
    three_b = []
    for of_rimanti in three_a:
        if of_rimanti not in captured:
            three_b.append(of_rimanti)
    # Length: 6488

    # This time the script checks that one of the couples created by splitting a group of three is also present in the list of dantean's rimanti couples
    three_partial = []
    three_partial_dante = []
    for a_list in three_b:
        a_combinations = list(itertools.combinations(sorted(a_list), 2))
        if a_combinations[0] in dante_flattened:
            three_partial.append(a_list)
            three_partial_dante.append([a_list, a_combinations[0]])
        elif a_combinations[1] in dante_flattened:
            three_partial.append(a_list)
            three_partial_dante.append([a_list, a_combinations[1]])
        elif a_combinations[2] in dante_flattened:
            three_partial.append(a_list)
            three_partial_dante.append([a_list, a_combinations[2]])
    # Length of three_partial: 2317

    ### Groups of two rimanti ####
    # Category D: a group of two Furioso rimanti corresponds to a group of two Divina Commedia rimanti
    two_rimanti_sorted = []
    for a_rimanti in a_two_rimanti:
        for d_sublist in dante_two_rimanti:
            if a_rimanti == d_sublist:
                two_rimanti_sorted.append(a_rimanti)
                break
    set_complete_two = set(tuple(i) for i in two_rimanti_sorted)
    # Length: 42

    # Category E: a group of two Furioso rimanti corresponds to a part of a group of three Divina Commedia rimanti
    # A list of all the groups of two rimanti which were not in the previous category is created
    two_a = []
    for sub_two in set_group_two:
        if sub_two not in set_complete_two:
            two_a.append(sub_two)
    print(len(two_a))
    # Length: 3366

    # The groups of two rimanti are compared to the couples of dantean's rimanti for matches
    two_from_three = []
    two_from_three_tuple = []
    for sub_two in two_a:
        if sub_two in dante_flattened:
            two_from_three.append(list(sub_two))
            two_from_three_tuple.append(sub_two)
    # Length two_from_three: 815


    ##### Creating the dictionaries ####
    # Each dictionary is created with the following logic: a group of rimanti that has found a match is fused to create the key of the dictionary. If, for example, ABC is a group with a match in Dante, then the key would be A_B_C. First are created all the entries from the lists made previously. Then the group of rimanti is found in the comprehensive list of rimanti of the two works (where information regarding the position of the group of rimanti can be extracted). This works particularly well for Orlando Furioso (where a logic of canto, ottava is applied) but less with the Commedia. This is due to the fact that the lists are sorted so finding the rimanti which starts the sequence is not possible. The indication of verse that is obtained here always identifies the exact potion of one of the three words, but it might not be the first that appears in the text. The information regarding the position of the group of rimanti within the text is then added to the dictionary, wich is then written in a Json file.

    # Category A
    rimanti_dic_A = {}
    for sub_set in three_rimanti_sorted:
        key = '_'.join(sub_set)
        rimanti_dic_A[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in three_rimanti_sorted:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil((canto.index(of_sublist)+1)/3)
                value = [pos_canto, pos_verso]
                rimanti_dic_A[key]['OF'].append(value)
    
    # Adding the information regarding the position of the rimanti in Dante's poem
    for canto in dante_canti:
        for dante_sublist in canto:
            if sorted(dante_sublist) in three_rimanti_sorted:
                key = '_'.join(sorted(dante_sublist))
                if dante_canti.index(canto) <= 33:
                    posotion_canto = (dante_canti.index(canto)) + 1
                    value = [posotion_canto, ((canto.index(dante_sublist))*3)+1]
                    rimanti_dic_A[key]['IF'].append(value)
                if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                    posotion_canto = (dante_canti.index(canto)) - 33
                    value = [posotion_canto, ((canto.index(dante_sublist))*3)+1]
                    rimanti_dic_A[key]['PG'].append(value)
                if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                    posotion_canto = (dante_canti.index(canto)) - 66
                    value = [posotion_canto, ((canto.index(dante_sublist))*3)+1]
                    rimanti_dic_A[key]['PD'].append(value)
        
        
        myKeys = list(rimanti_dic_A.keys())
        myKeys.sort()
        sorted_dict_1 = {i: rimanti_dic_A[i] for i in myKeys}

    with open ('json_files/dictionaries_json/group_A.json', 'w') as dic:
        json.dump(sorted_dict_1, dic)
    with open ('json_files/dictionaries_json/group_A.txt', 'w') as dic:
        json.dump(sorted_dict_1, dic)

    # Category B
    rimanti_dic_B = {}
    for sub_set in captured:
        key = '_'.join(sub_set)
        rimanti_dic_B[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in captured:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil((canto.index(of_sublist)+1)/3)
                value = [pos_canto, pos_verso]
                rimanti_dic_B[key]['OF'].append(value)
    
    # Adding the information regarding the position of the rimanti in Dante's poem
    for canto in dante_canti:
        for dante_sublist in canto:
            d_combinations = list(itertools.combinations(sorted(dante_sublist), 2))
            for entry in captured_dante:
                if entry[1] in d_combinations or entry[2] in d_combinations:
                    key = '_'.join(sorted(entry[0]))
                    if dante_canti.index(canto) <= 33:
                        posotion_canto = (dante_canti.index(canto)) + 1
                        value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                        rimanti_dic_B[key]['IF'].append(value)
                    if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                        posotion_canto = (dante_canti.index(canto)) - 33
                        value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                        rimanti_dic_B[key]['PG'].append(value)
                    if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                        posotion_canto = (dante_canti.index(canto)) - 66
                        value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                        rimanti_dic_B[key]['PD'].append(value)

    myKeys = list(rimanti_dic_B.keys())
    myKeys.sort()
    B_dic = {i: rimanti_dic_B[i] for i in myKeys}
    
    with open ('json_files/dictionaries_json/group_B.json', 'w') as dic:
        json.dump(B_dic, dic)
    with open ('json_files/dictionaries_json/group_B.txt', 'w') as dic:
        json.dump(B_dic, dic)

    # Category C: Partial riprese of groups of three in Ariosto
    rimanti_dic_C = {}
    for sub_set in three_partial:
        key = '_'.join(sub_set)
        rimanti_dic_C[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in three_partial:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil((canto.index(of_sublist)+1)/3)
                value = [pos_canto, pos_verso]
                rimanti_dic_C[key]['OF'].append(value)
    
    # Adding the information regarding the position of the rimanti in Dante's poem
    for canto in dante_canti:
        for dante_sublist in canto:
            d_combinations = list(itertools.combinations(sorted(dante_sublist), 2))
            for entry in three_partial_dante:
                if entry[1] in d_combinations:
                    key = '_'.join(sorted(entry[0]))
                    if dante_canti.index(canto) <= 33:
                        posotion_canto = (dante_canti.index(canto)) + 1
                        value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                        rimanti_dic_C[key]['IF'].append(value)
                    if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                        posotion_canto = (dante_canti.index(canto)) - 33
                        value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                        rimanti_dic_C[key]['PG'].append(value)
                    if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                        posotion_canto = (dante_canti.index(canto)) - 66
                        value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                        rimanti_dic_C[key]['PD'].append(value)

    myKeys = list(rimanti_dic_C.keys())
    myKeys.sort()
    C_dic = {i: rimanti_dic_C[i] for i in myKeys}
    
    with open ('json_files/dictionaries_json/group_C.json', 'w') as dic:
        json.dump(C_dic, dic)
    with open ('json_files/dictionaries_json/group_C.txt', 'w') as dic:
        json.dump(C_dic, dic)


    # Category D: Full ripresa of a group of two
    rimanti_dic_D = {}
    for sub_set in set_complete_two:
        key = '_'.join(sub_set)
        rimanti_dic_D[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in two_rimanti_sorted:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil(canto.index(of_sublist)/3)
                value = [pos_canto, pos_verso]
                rimanti_dic_D[key]['OF'].append(value)
    
    for canto in dante_canti:
        for dante_sublist in canto:
            if sorted(dante_sublist) in two_rimanti_sorted:
                key = '_'.join(sorted(dante_sublist))
                if dante_canti.index(canto) <= 33:
                    posotion_canto = (dante_canti.index(canto)) + 1
                    position_verse = (canto.index(dante_sublist))
                    if position_verse == 0:
                        value = [posotion_canto, (position_verse + 1)]
                        rimanti_dic_D[key]['IF'].append(value)
                    elif position_verse > 0:
                        value = [posotion_canto, ((position_verse * 3) + 2)]
                        rimanti_dic_D[key]['IF'].append(value)
                if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                    posotion_canto = (dante_canti.index(canto)) - 33
                    position_verse = (canto.index(dante_sublist))
                    if position_verse == 0:
                        value = [posotion_canto, (position_verse + 1)]
                        rimanti_dic_D[key]['PG'].append(value)
                    elif position_verse > 0:
                        value = [posotion_canto, ((position_verse * 3) + 2)]
                        rimanti_dic_D[key]['PG'].append(value)
                if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                    posotion_canto = (dante_canti.index(canto)) - 66
                    position_verse = (canto.index(dante_sublist))
                    if position_verse == 0:
                        value = [posotion_canto, (position_verse + 1)]
                        rimanti_dic_D[key]['PD'].append(value)
                    elif position_verse > 0:
                        value = [posotion_canto, ((position_verse * 3) + 2)]
                        rimanti_dic_D[key]['PD'].append(value)

    myKeys = list(rimanti_dic_D.keys())
    myKeys.sort()
    D_group = {i: rimanti_dic_D[i] for i in myKeys}

    with open ('json_files/dictionaries_json/group_D.json', 'w') as dic:
        json.dump(D_group, dic)
    with open ('json_files/dictionaries_json/group_D.txt', 'w') as dic:
        json.dump(D_group, dic)


    # Category E: A group of two in Ariosto partially riprende a group of three in Dante
    rimanti_dic_E = {}
    for sub_set in two_from_three:
        key = '_'.join(sub_set)
        rimanti_dic_E[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in two_from_three:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil(canto.index(of_sublist)/3)
                value = [pos_canto, pos_verso]
                rimanti_dic_E[key]['OF'].append(value)
    
    for canto in dante_canti:
        for dante_sublist in canto:
            d_combinations = list(itertools.combinations(sorted(dante_sublist), 2))
            for sub_tuple in two_from_three_tuple:
                if sub_tuple in d_combinations:
                    key = '_'.join(sorted(sub_tuple))
                    if dante_canti.index(canto) <= 33:
                        posotion_canto = (dante_canti.index(canto)) + 1
                        position_verse = (canto.index(dante_sublist))
                        if position_verse == 0:
                            value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                            rimanti_dic_E[key]['IF'].append(value)
                        elif position_verse > 0:
                            value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                            rimanti_dic_E[key]['IF'].append(value)
                    if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                        posotion_canto = (dante_canti.index(canto)) - 33
                        position_verse = (canto.index(dante_sublist))
                        if position_verse == 0:
                            value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                            rimanti_dic_E[key]['PG'].append(value)
                        elif position_verse > 0:
                            value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                            rimanti_dic_E[key]['PG'].append(value)
                    if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                        posotion_canto = (dante_canti.index(canto)) - 66
                        position_verse = (canto.index(dante_sublist))
                        if position_verse == 0:
                            value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                            rimanti_dic_E[key]['PD'].append(value)
                        elif position_verse > 0:
                            value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
                            rimanti_dic_E[key]['PD'].append(value)

    myKeys = list(rimanti_dic_E.keys())
    myKeys.sort()
    D_group = {i: rimanti_dic_E[i] for i in myKeys}

    with open ('json_files/dictionaries_json/group_E.json', 'w') as dic:
        json.dump(D_group, dic)
    with open ('json_files/dictionaries_json/group_E.txt', 'w') as dic:
        json.dump(D_group, dic)


if __name__ == "__main__":
    main()