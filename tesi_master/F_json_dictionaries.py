import json
import itertools
import math

def main():

    #In this script a dictionary containing all the riprese of a group of three from Dante by Ariosto is created. The dictionary contains the ordered group of three as the name of a sub_dictionary like this: A_B_C and the position of the three word combination in OF and in the three Cantica

    # Importing the json files and opening it as a python list
    # Inferno
    inferno = open('tesi_master/json_files/rimanti_json/inferno_rimanti.json')
    inferno_rimanti_list = json.load(inferno)

    # Purgtorio
    purgatorio = open('tesi_master/json_files/rimanti_json/purgatorio_rimanti.json')
    purgatorio_rimanti_list = json.load(purgatorio)

    # Paradiso
    paradiso = open('tesi_master/json_files/rimanti_json/paradiso_rimanti.json')
    paradiso_rimanti_list = json.load(paradiso)

    # Orlando Furioso
    OrlandoFurioso = open('tesi_master/json_files/rimanti_json/orlando_rimanti.json')
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

    # with open ('tesi_master/json_files/rimanti_json/dante_rimanti.json', 'w') as dante:
    #     json.dump(dante_rimanti, dante)

    # Separating the groups of two rimanti's from the rest, first for the Divina Commedia than for the Orlando Furioso
    dante_two_rimanti = []
    for rimanti in dante_rimanti:
        if len(rimanti) == 2:
            dante_two_rimanti.append(sorted(rimanti))
    #print(len(dante_two_rimanti))
    # 200

    dante_two_rimanti_double = []
    for rimanti in dante_rimanti:
        if len(rimanti) == 2:
            if rimanti[0] == rimanti [1]:
                dante_two_rimanti_double.append(rimanti)
    #print(len(dante_two_rimanti_double))
    #print(dante_two_rimanti_double)
    #1

    a_two_rimanti = []
    for canto in of_rimanti_list:
        for sub_list in canto:
            if len(sub_list) == 2:
                a_two_rimanti.append(sorted(sub_list))
    #print(len(a_two_rimanti))
    # 4842

    set_group_two = set(tuple(i) for i in a_two_rimanti)
    print('set_group_two len', len(set_group_two))
    # 3408

    # See if any of the groups of two rimanti is made of the same word
    a_two_rimanti_double = []
    for canto in of_rimanti_list:
        for sub_list in canto:
            if len(sub_list) == 2:
                if sub_list[0] == sub_list[1]:
                    a_two_rimanti_double.append(sub_list)
    #print(len(a_two_rimanti_double))
    #print(a_two_rimanti_double)
    # 25

    # Calculating the total number of groups of three rimanti in Orlando Furioso
    of_three_rimanti = []
    number_of_three_rimanti_of = 0
    for canto in of_rimanti_list:
        for sub_list in canto: 
            if len(sub_list) == 3:
                number_of_three_rimanti_of += 1
                of_three_rimanti.append(sorted(sub_list))
    #print(number_of_three_rimanti_of)
    # The number is 9684

    #How many of the groups of three are made up of the same words but in different order?
    set_group_three = set(tuple(i) for i in of_three_rimanti)
    #print(len(set_group_three))
    # 7824 sorted

    #Maaking the set of tuples in a list so as to facilitate the comparaison with the list of lists
    unset = []
    for rimanti in set_group_three:
        unset.append(list(rimanti))

    # Calculating the number of riprese of Dante by Ariosto for complete groups of three
    three_rimanti_sorted = []
    for of_sublist in set_group_three:
        for d_sublist in dante_rimanti:
            if sorted(of_sublist) == sorted(d_sublist):
                three_rimanti_sorted.append(sorted(of_sublist))
                break
    #print(len(three_rimanti_sorted))
    # 406 --> sorted!
    # 850 not sorted

    # Calculating the number of full riprese of a group of three in Ariosto but composed by two groups in Dante (of two or three)
    three_a = []
    for of_rimanti in unset:
        if of_rimanti not in three_rimanti_sorted:
            three_a.append(of_rimanti)
    #print(len(three_a))
    # 7418

    # Creating combinations out of all the rimanti in the Divina Commedia 
    dante_paires = []
    for rimanti in dante_rimanti:
        x_combinations = list((itertools.combinations(sorted(rimanti), 2)))
        dante_paires.append(x_combinations)
    #print(dante_paires)

    #Creating a flattened list of tuples 
    dante_flattened = []
    for sub_list in dante_paires:
        for sub_tuple in sub_list:
            dante_flattened.append(sub_tuple)
    #print(dante_flattened)

    # Full rirpese by more than one group in Dante
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

    #print(len(captured))
    # 930

    #Calculating the partial riprese of a group of three
    three_b = []
    for of_rimanti in three_a:
        if of_rimanti not in captured:
            three_b.append(of_rimanti)
    #print(len(three_b))
    # 6488

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
    #print(len(three_partial))
    # # 2317

    ### Groups of two rimanti ####

    # Complete riprese of groups of two

    two_rimanti_sorted = []
    for a_rimanti in a_two_rimanti:
        for d_sublist in dante_two_rimanti:
            if a_rimanti == d_sublist:
                two_rimanti_sorted.append(a_rimanti)
                break
    print('two_rimanti riprese len:', len(two_rimanti_sorted))
    # 112
    set_complete_two = set(tuple(i) for i in two_rimanti_sorted)
    print(len(set_complete_two))
    # 42

    two_a = []
    for sub_two in set_group_two:
        if sub_two not in set_complete_two:
            two_a.append(sub_two)
    print(len(two_a))
    # 3366

    ### Ariosto prende il gruppo di due da un gruppo di tre di D ###
    two_from_three = []
    two_from_three_tuple = []
    for sub_two in two_a:
        if sub_two in dante_flattened:
            two_from_three.append(list(sub_two))
            two_from_three_tuple.append(sub_two)
    # print(len(two_from_three))
    print(type(two_from_three[1]))
    # 815



    ##### Creating the dictionaries ####

    # # Group A: Full riprese of a group of three

    # rimanti_dic = {}
    # for sub_set in three_rimanti_sorted:
    #     key = '_'.join(sub_set)
    #     rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    # for canto in of_rimanti_list:
    #     for of_sublist in canto:
    #         if sorted(of_sublist) in three_rimanti_sorted:
    #             key = '_'.join(sorted(of_sublist))
    #             pos_canto = of_rimanti_list.index(canto) + 1
    #             pos_verso = math.ceil((canto.index(of_sublist)+1)/3)
    #             value = [pos_canto, pos_verso]
    #             rimanti_dic[key]['OF'].append(value)
    
    # # Adding the information regarding the position of the rimanti in Dante's poem
    # for canto in dante_canti:
    #     for dante_sublist in canto:
    #         if sorted(dante_sublist) in three_rimanti_sorted:
    #             key = '_'.join(sorted(dante_sublist))
    #             if dante_canti.index(canto) <= 33:
    #                 posotion_canto = (dante_canti.index(canto)) + 1
    #                 value = [posotion_canto, ((canto.index(dante_sublist))*3)+1]
    #                 rimanti_dic[key]['IF'].append(value)
    #             if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
    #                 posotion_canto = (dante_canti.index(canto)) - 33
    #                 value = [posotion_canto, ((canto.index(dante_sublist))*3)+1]
    #                 rimanti_dic[key]['PG'].append(value)
    #             if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
    #                 posotion_canto = (dante_canti.index(canto)) - 66
    #                 value = [posotion_canto, ((canto.index(dante_sublist))*3)+1]
    #                 rimanti_dic[key]['PD'].append(value)
        
        
    #     myKeys = list(rimanti_dic.keys())
    #     myKeys.sort()
    #     sorted_dict_1 = {i: rimanti_dic[i] for i in myKeys}

    # #print(rimanti_dic)

    # with open ('tesi_master/json_files/dictionaries_json/group_A.json', 'w') as dic:
    #     json.dump(sorted_dict_1, dic)
    # with open ('tesi_master/json_files/dictionaries_json/group_A.txt', 'w') as dic:
    #     json.dump(sorted_dict_1, dic)

    # #### Group B: The group of three in Ariosto is a ripresa of two groups of Dante
    # rimanti_dic = {}
    # for sub_set in captured:
    #     key = '_'.join(sub_set)
    #     rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    # for canto in of_rimanti_list:
    #     for of_sublist in canto:
    #         if sorted(of_sublist) in captured:
    #             key = '_'.join(sorted(of_sublist))
    #             pos_canto = of_rimanti_list.index(canto) + 1
    #             pos_verso = math.ceil((canto.index(of_sublist)+1)/3)
    #             value = [pos_canto, pos_verso]
    #             rimanti_dic[key]['OF'].append(value)
    
    # # Adding the information regarding the position of the rimanti in Dante's poem
    # for canto in dante_canti:
    #     for dante_sublist in canto:
    #         d_combinations = list(itertools.combinations(sorted(dante_sublist), 2))
    #         for entry in captured_dante:
    #             if entry[1] in d_combinations or entry[2] in d_combinations:
    #                 key = '_'.join(sorted(entry[0]))
    #                 if dante_canti.index(canto) <= 33:
    #                     posotion_canto = (dante_canti.index(canto)) + 1
    #                     value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                     rimanti_dic[key]['IF'].append(value)
    #                 if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
    #                     posotion_canto = (dante_canti.index(canto)) - 33
    #                     value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                     rimanti_dic[key]['PG'].append(value)
    #                 if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
    #                     posotion_canto = (dante_canti.index(canto)) - 66
    #                     value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                     rimanti_dic[key]['PD'].append(value)

    # myKeys = list(rimanti_dic.keys())
    # myKeys.sort()
    # B_dic = {i: rimanti_dic[i] for i in myKeys}
    
    # with open ('tesi_master/json_files/dictionaries_json/group_B.json', 'w') as dic:
    #     json.dump(B_dic, dic)
    # with open ('tesi_master/json_files/dictionaries_json/group_B.txt', 'w') as dic:
    #     json.dump(B_dic, dic)

    ### Group C: Partial riprese of groups of three in Ariosto
    # rimanti_dic = {}
    # for sub_set in three_partial:
    #     key = '_'.join(sub_set)
    #     rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    # for canto in of_rimanti_list:
    #     for of_sublist in canto:
    #         if sorted(of_sublist) in three_partial:
    #             key = '_'.join(sorted(of_sublist))
    #             pos_canto = of_rimanti_list.index(canto) + 1
    #             pos_verso = math.ceil((canto.index(of_sublist)+1)/3)
    #             value = [pos_canto, pos_verso]
    #             rimanti_dic[key]['OF'].append(value)
    
    # # Adding the information regarding the position of the rimanti in Dante's poem
    # for canto in dante_canti:
    #     for dante_sublist in canto:
    #         d_combinations = list(itertools.combinations(sorted(dante_sublist), 2))
    #         for entry in three_partial_dante:
    #             if entry[1] in d_combinations:
    #                 key = '_'.join(sorted(entry[0]))
    #                 if dante_canti.index(canto) <= 33:
    #                     posotion_canto = (dante_canti.index(canto)) + 1
    #                     value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                     rimanti_dic[key]['IF'].append(value)
    #                 if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
    #                     posotion_canto = (dante_canti.index(canto)) - 33
    #                     value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                     rimanti_dic[key]['PG'].append(value)
    #                 if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
    #                     posotion_canto = (dante_canti.index(canto)) - 66
    #                     value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                     rimanti_dic[key]['PD'].append(value)

    # myKeys = list(rimanti_dic.keys())
    # myKeys.sort()
    # C_dic = {i: rimanti_dic[i] for i in myKeys}
    
    # with open ('tesi_master/json_files/dictionaries_json/group_C.json', 'w') as dic:
    #     json.dump(C_dic, dic)
    # with open ('tesi_master/json_files/dictionaries_json/group_C.txt', 'w') as dic:
    #     json.dump(C_dic, dic)


    ## Group D: Full ripresa of a group of two
    two_rimanti_dic = {}
    for sub_set in set_complete_two:
        key = '_'.join(sub_set)
        two_rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in two_rimanti_sorted:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil(canto.index(of_sublist)/3)
                value = [pos_canto, pos_verso]
                two_rimanti_dic[key]['OF'].append(value)
    
    for canto in dante_canti:
        for dante_sublist in canto:
            if sorted(dante_sublist) in two_rimanti_sorted:
                key = '_'.join(sorted(dante_sublist))
                if dante_canti.index(canto) <= 33:
                    posotion_canto = (dante_canti.index(canto)) + 1
                    position_verse = (canto.index(dante_sublist))
                    if position_verse == 0:
                        value = [posotion_canto, (position_verse + 1)]
                        two_rimanti_dic[key]['IF'].append(value)
                    elif position_verse > 0:
                        value = [posotion_canto, ((position_verse * 3) + 2)]
                        two_rimanti_dic[key]['IF'].append(value)
                if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                    posotion_canto = (dante_canti.index(canto)) - 33
                    position_verse = (canto.index(dante_sublist))
                    if position_verse == 0:
                        value = [posotion_canto, (position_verse + 1)]
                        two_rimanti_dic[key]['PG'].append(value)
                    elif position_verse > 0:
                        value = [posotion_canto, ((position_verse * 3) + 2)]
                        two_rimanti_dic[key]['PG'].append(value)
                if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                    posotion_canto = (dante_canti.index(canto)) - 66
                    position_verse = (canto.index(dante_sublist))
                    if position_verse == 0:
                        value = [posotion_canto, (position_verse + 1)]
                        two_rimanti_dic[key]['PD'].append(value)
                    elif position_verse > 0:
                        value = [posotion_canto, ((position_verse * 3) + 2)]
                        two_rimanti_dic[key]['PD'].append(value)

    myKeys = list(two_rimanti_dic.keys())
    myKeys.sort()
    D_group = {i: two_rimanti_dic[i] for i in myKeys}

    with open ('tesi_master/json_files/dictionaries_json/group_D.json', 'w') as dic:
        json.dump(D_group, dic)
    with open ('tesi_master/json_files/dictionaries_json/group_D.txt', 'w') as dic:
        json.dump(D_group, dic)


    # #### Group E: A group of two in Ariosto partially riprende a group of three in Dante
    # two_rimanti_dic = {}
    # for sub_set in two_from_three:
    #     key = '_'.join(sub_set)
    #     two_rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # for canto in of_rimanti_list:
    #     for of_sublist in canto:
    #         if sorted(of_sublist) in two_from_three:
    #             key = '_'.join(sorted(of_sublist))
    #             pos_canto = of_rimanti_list.index(canto) + 1
    #             pos_verso = math.ceil(canto.index(of_sublist)/3)
    #             value = [pos_canto, pos_verso]
    #             two_rimanti_dic[key]['OF'].append(value)
    
    # for canto in dante_canti:
    #     for dante_sublist in canto:
    #         d_combinations = list(itertools.combinations(sorted(dante_sublist), 2))
    #         for sub_tuple in two_from_three_tuple:
    #             if sub_tuple in d_combinations:
    #                 key = '_'.join(sorted(sub_tuple))
    #                 if dante_canti.index(canto) <= 33:
    #                     posotion_canto = (dante_canti.index(canto)) + 1
    #                     position_verse = (canto.index(dante_sublist))
    #                     if position_verse == 0:
    #                         value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                         two_rimanti_dic[key]['IF'].append(value)
    #                     elif position_verse > 0:
    #                         value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                         two_rimanti_dic[key]['IF'].append(value)
    #                 if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
    #                     posotion_canto = (dante_canti.index(canto)) - 33
    #                     position_verse = (canto.index(dante_sublist))
    #                     if position_verse == 0:
    #                         value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                         two_rimanti_dic[key]['PG'].append(value)
    #                     elif position_verse > 0:
    #                         value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                         two_rimanti_dic[key]['PG'].append(value)
    #                 if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
    #                     posotion_canto = (dante_canti.index(canto)) - 66
    #                     position_verse = (canto.index(dante_sublist))
    #                     if position_verse == 0:
    #                         value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                         two_rimanti_dic[key]['PD'].append(value)
    #                     elif position_verse > 0:
    #                         value = [dante_sublist, [posotion_canto, ((canto.index(dante_sublist))*3)+1]]
    #                         two_rimanti_dic[key]['PD'].append(value)

    # myKeys = list(two_rimanti_dic.keys())
    # myKeys.sort()
    # D_group = {i: two_rimanti_dic[i] for i in myKeys}

    # with open ('tesi_master/json_files/dictionaries_json/group_E.json', 'w') as dic:
    #     json.dump(D_group, dic)
    # with open ('tesi_master/json_files/dictionaries_json/group_E.txt', 'w') as dic:
    #     json.dump(D_group, dic)


if __name__ == "__main__":
    main()