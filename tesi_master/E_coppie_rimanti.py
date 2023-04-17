import re
import json
import itertools

def main():
    # Script E: In this script the amount of riprese by Ariosto
    # of Dante's work is calculated as follows. Because the rimanti
    # can be distinguished in groups of three or groups of two (see readme)
    # the groups of three rimanti are split in three groups of two rimanti.
    # The groups of two are all put together. If the group of two in Ariosto
    # is also present in Dante than a point is assigned over the total.

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

    #Creating a comprehensive list of all rimanti across the Commedia
    dante_rimanti = []
    # INFERNO
    # Extracting sub_lists from each canto
    if_opera_completa = []
    for canto in inferno_rimanti_list :
        for gruppo_rimanti in canto:
            if_opera_completa.append(gruppo_rimanti)

    # Creating a list of sub lists, which contain each a couple of rimanti who rhyme between them
    if_coppie_rimanti = []
    for gruppo_rimanti in if_opera_completa :
        if len(gruppo_rimanti) < 3:
            if_coppie_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                if_coppie_rimanti.append(combination)
                dante_rimanti.append(combination) 

   #print(len(if_coppie_rimanti))
   
    # PURGATORIO
    pg_opera_completa = []
    for canto in purgatorio_rimanti_list :
        for gruppo_rimanti in canto:
            pg_opera_completa.append(gruppo_rimanti)

    pg_coppie_rimanti = []
    for gruppo_rimanti in pg_opera_completa :
        if len(gruppo_rimanti) < 3:
            pg_coppie_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                pg_coppie_rimanti.append(combination)
                dante_rimanti.append(combination)

    #print(len(pg_coppie_rimanti))

    # PARADISO
    pd_opera_completa = []
    for canto in paradiso_rimanti_list :
        for gruppo_rimanti in canto:
            pd_opera_completa.append(gruppo_rimanti)

    pd_coppie_rimanti = []
    for gruppo_rimanti in pd_opera_completa :
        if len(gruppo_rimanti) < 3:
            pd_coppie_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                pd_coppie_rimanti.append(combination)
                dante_rimanti.append(combination)

    #print(len(pd_coppie_rimanti))
    #print(len(dante_rimanti))
    # ORLANDO FURIOSO
    of_opera_completa = []
    for canto in of_rimanti_list :
        for gruppo_rimanti in canto:
            of_opera_completa.append(gruppo_rimanti)

    of_coppie_rimanti = []
    for gruppo_rimanti in of_opera_completa :
        if len(gruppo_rimanti) < 3:
            of_coppie_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                of_coppie_rimanti.append(combination)

    #print(len(of_coppie_rimanti))

    of_len_tokens = len(of_coppie_rimanti)

    ## TOKENS
    # How many couples of rimanti are composed by the same word?
    # This is important to know because a high enough value means the impossibility of working with sets instead of lists
    double_rimanti = 0
    for coppia in of_coppie_rimanti:
        if coppia[0] == coppia[1]:
            double_rimanti += 1
    #print(double_rimanti)

    #calcolo = (double_rimanti/33894)*100
    #print(calcolo)
    # About 1%

    # Making sure that the list is composed of sublists
    new_of_list = []
    for coppia in of_coppie_rimanti:
        new_coppia = list(coppia)
        new_of_list.append(new_coppia)
    #print(new_of_list)

    #Trying to sort the sublists so that then I can compare them without using sets
    of_sorted = []
    for sub_list in new_of_list:
        of_sorted.append(sorted(sub_list))
    print(len(of_sorted))

    # Making sure that all sub lists are in fact a list
    new_dante_list = []
    for coppia in dante_rimanti:
        new_coppia = list(coppia)
        new_dante_list.append(new_coppia)
    #print(new_dante_list)

    d_sorted = []
    for sub_list in new_dante_list:
        d_sorted.append(sorted(sub_list))
    print(len(d_sorted))

    #Inferno
    new_if_list = []
    for coppia in if_coppie_rimanti:
        new_coppia = list(coppia)
        new_if_list.append(new_coppia)
    
    if_sorted = []
    for sub_list in new_if_list:
        if_sorted.append(sorted(sub_list))
    #Purgatorio
    new_pg_list = []
    for coppia in pg_coppie_rimanti:
        new_coppia = list(coppia)
        new_pg_list.append(new_coppia)
    
    pg_sorted = []
    for sub_list in new_pg_list:
        pg_sorted.append(sorted(sub_list))
    #Paradiso
    new_pd_list = []
    for coppia in pd_coppie_rimanti:
        new_coppia = list(coppia)
        new_pd_list.append(new_coppia)
    
    pd_sorted = []
    for sub_list in new_pd_list:
        pd_sorted.append(sorted(sub_list))

    # Caculating how many of the couples used by Ariosto are taken from Dante
    tokens = 0
    for of_sub_list in of_sorted:
        for d_sublist in d_sorted:
            if of_sub_list == d_sublist:
                #print(of_sub_list, d_sublist)
                tokens += 1
                break
    print(tokens)

    if_tokens = 0
    for of_sub_list in of_sorted:
        for if_sublist in if_sorted:
            if of_sub_list == if_sublist:
                if_tokens += 1
                break

    pg_tokens = 0
    for of_sub_list in of_sorted:
        for pg_sublist in pg_sorted:
            if of_sub_list == pg_sublist:
                pg_tokens += 1
                break                
    
    pd_tokens = 0
    for of_sub_list in of_sorted:
        for pd_sublist in pd_sorted:
            if of_sub_list == pd_sublist:
                pd_tokens += 1
                break
    
    ## TYPES
    #Creating a set of tuples
    of_set = set(tuple(i) for i in of_sorted)
    set_length = len(of_set)

    d_set = set(tuple(i) for i in d_sorted)
    print(len(d_set))

    types = 0
    for of_sub_list in of_set:
        for d_sublist in d_set:
            if of_sub_list == d_sublist:
                #print(of_sub_list, d_sublist)
                types += 1
                break
    print(types)

    
    percentage_tokens = (tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto - tokens: ', percentage_tokens)
    # Percentage of citations by Ariosto - tokens:  29.860742314273914
    # After adjustment: Percentage of citations by Ariosto - tokens:  30.29444739481914

    if_percentage_tokens = (if_tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto from Inferno - tokens: ', if_percentage_tokens)
    # Percentage of citations by Ariosto from Inferno - tokens:  18.74373045376763
     # After adjustment: Percentage of citations by Ariosto from Inferno - tokens:  18.903050687437304

    pg_percentage_tokens = (pg_tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto from Purgatorio - tokens: ', pg_percentage_tokens)
    # Percentage of citations by Ariosto from Purgatorio - tokens:  18.224464506992387
    # After adjustment: Percentage of citations by Ariosto from Purgatorio - tokens:  18.43984185991621

    pd_percentage_tokens = (pd_tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto from Paradiso - tokens: ', pd_percentage_tokens) 
    # Percentage of citations by Ariosto from Paradiso - tokens:  15.091166578155427  
    # After adjustment: Percentage of citations by Ariosto from Paradiso - tokens:  15.315395055172006

    percentage_types = (types/set_length)*100
    print('Percentage of citations by Ariosto - types: ', percentage_types)
    # Percentage of citations by Ariosto - types:  13.803837229045222
    # After adjustment: Percentage of citations by Ariosto - types:  14.233845804731379


if __name__ == "__main__":
    main()