import re
import json
import itertools

def main():
    # Script E: In this script the amount of riprese of Dante's work by Ariosto is calculated as follows: because the rimanti can be distinguished in groups of three or groups of two the groups of three rimanti are split in three couples of two rimanti. The groups of two are then added to the couples. If the group of two in Ariosto is also present in Dante than a point is assigned over the total.

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
            dante_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                if_coppie_rimanti.append(combination)
                dante_rimanti.append(combination) 
   
    # PURGATORIO
    pg_opera_completa = []
    for canto in purgatorio_rimanti_list :
        for gruppo_rimanti in canto:
            pg_opera_completa.append(gruppo_rimanti)

    pg_coppie_rimanti = []
    for gruppo_rimanti in pg_opera_completa :
        if len(gruppo_rimanti) < 3:
            pg_coppie_rimanti.append(gruppo_rimanti)
            dante_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                pg_coppie_rimanti.append(combination)
                dante_rimanti.append(combination)

    # PARADISO
    pd_opera_completa = []
    for canto in paradiso_rimanti_list :
        for gruppo_rimanti in canto:
            pd_opera_completa.append(gruppo_rimanti)

    pd_coppie_rimanti = []
    for gruppo_rimanti in pd_opera_completa :
        if len(gruppo_rimanti) < 3:
            pd_coppie_rimanti.append(gruppo_rimanti)
            dante_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                pd_coppie_rimanti.append(combination)
                dante_rimanti.append(combination)

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

    of_len_tokens = len(of_coppie_rimanti)

    ## TOKENS
    # How many couples of rimanti are composed by the same word?
    # This is important to know because a high enough value means the impossibility of working with sets instead of lists
    double_rimanti = 0
    for coppia in of_coppie_rimanti:
        if coppia[0] == coppia[1]:
            double_rimanti += 1
    print(double_rimanti)

    calcolo = (double_rimanti/33894)*100
    # About 1%

    # Making sure that the list is composed of sublists
    new_of_list = []
    for coppia in of_coppie_rimanti:
        new_coppia = list(coppia)
        new_of_list.append(new_coppia)

    #Trying to sort the sublists so that then I can compare them without using sets
    of_sorted = []
    for sub_list in new_of_list:
        of_sorted.append(sorted(sub_list))

    # Making sure that all sub lists are in fact a list
    new_dante_list = []
    for coppia in dante_rimanti:
        new_coppia = list(coppia)
        new_dante_list.append(new_coppia)

    d_sorted = []
    for sub_list in new_dante_list:
        d_sorted.append(sorted(sub_list))

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

    # Caculating how many of the couples used by Ariosto coincide with Dante's
    # Over the whole Commedia
    tokens = 0
    for of_sub_list in of_sorted:
        if of_sub_list in d_sorted:
                tokens += 1

    # In Inferno
    if_tokens = 0
    for of_sub_list in of_sorted:
        if of_sub_list in if_sorted:
            if_tokens += 1

    # In Purgatorio
    pg_tokens = 0
    for of_sub_list in of_sorted:
        if of_sub_list in pg_sorted:
            pg_tokens += 1               
    
    # In Paradiso
    pd_tokens = 0
    for of_sub_list in of_sorted:
        if of_sub_list in pd_sorted:
            pd_tokens += 1
    
    ## TYPES
    #Creating a set of tuples to reduce the couples of rimanti from tokens to types
    of_set = set(tuple(i) for i in of_sorted)
    set_length = len(of_set)

    d_set = set(tuple(i) for i in d_sorted)

    if_set = set(tuple(i) for i in if_sorted)

    pg_set = set(tuple(i) for i in pg_sorted)

    pd_set = set(tuple(i) for i in pd_sorted)

    # Caculating how many of the couples used by Ariosto coincide with Dante's
    types = 0
    for of_sub_list in of_set:
        if of_sub_list in d_set: 
            types += 1
    print(types)

    types_if = 0
    for of_sub_list in of_set:
        if of_sub_list in if_set: 
            types_if += 1
    print(types_if)

    types_pg = 0
    for of_sub_list in of_set:
        if of_sub_list in pg_set: 
            types_pg += 1
    print(types_pg)

    types_pd = 0
    for of_sub_list in of_set:
        if of_sub_list in pd_set: 
            types_pd += 1
    print(types_pd)

    # Tokens
    percentage_tokens = (tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto - tokens: ', percentage_tokens)
    # Percentage of citations by Ariosto - tokens:  30.53637812002124

    if_percentage_tokens = (if_tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto from Inferno - tokens: ', if_percentage_tokens)
    # Percentage of citations by Ariosto from Inferno - tokens:  18.903050687437304

    pg_percentage_tokens = (pg_tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto from Purgatorio - tokens: ', pg_percentage_tokens)
    # Percentage of citations by Ariosto from Purgatorio - tokens:  18.43984185991621

    pd_percentage_tokens = (pd_tokens/of_len_tokens)*100
    print('Percentage of citations by Ariosto from Paradiso - tokens: ', pd_percentage_tokens) 
    # Percentage of citations by Ariosto from Paradiso - tokens:  15.315395055172006

    # Types
    percentage_types = (types/set_length)*100
    print('Percentage of citations by Ariosto - types: ', percentage_types)
    # Percentage of citations by Ariosto - types:  14.42105860327906

    if_percentage_types = (types_if/set_length)*100
    print('Percentage of citations by Ariosto - types: ', if_percentage_types)
    # Percentage of citations by Ariosto from Inferno - types:  7.244567992284563

    pg_percentage_types = (types_pg/set_length)*100
    print('Percentage of citations by Ariosto - types: ', pg_percentage_types)
    # Percentage of citations by Ariosto from Purgatorio - types:  7.159471265671981

    pd_percentage_types = (types_pd/set_length)*100
    print('Percentage of citations by Ariosto - types: ', pd_percentage_types)
    # Percentage of citations by Ariosto from Paradiso - types:  5.911385942020764


if __name__ == "__main__":
    main()