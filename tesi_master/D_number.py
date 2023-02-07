import re
import json

def main():
    OrlandoFurioso = open('orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # Importing the json files and opening it as a python list
    # Inferno
    inferno = open('inferno_rimanti.json')
    inferno_rimanti_list = json.load(inferno)
    
    # Purgtorio
    purgatorio = open('purgatorio_rimanti.json')
    purgatorio_rimanti_list = json.load(purgatorio)

    # Paradiso
    paradiso = open('paradiso_rimanti.json')
    paradiso_rimanti_list = json.load(paradiso)


    tot_OF = 0

    for canto in of_rimanti_list:
        canto_index = of_rimanti_list.index(canto)
        canto_to_analyse = of_rimanti_list[canto_index]
        for sub_list in canto_to_analyse:
            if len(sub_list) == 2:
                tot_OF += 1
            elif len(sub_list) == 3:
                tot_OF += 3
    
    print(tot_OF)

    tot_If = 0
    for canto in inferno_rimanti_list:
        canto_index = inferno_rimanti_list.index(canto)
        canto_to_analyse = inferno_rimanti_list[canto_index]
        for sub_list in canto_to_analyse:
            if len(sub_list) == 2:
                tot_If += 1
            elif len(sub_list) == 3:
                tot_If += 3
    
    print(tot_If)

    tot_Pg = 0
    for canto in purgatorio_rimanti_list:
        canto_index = purgatorio_rimanti_list.index(canto)
        canto_to_analyse = purgatorio_rimanti_list[canto_index]
        for sub_list in canto_to_analyse:
            if len(sub_list) == 2:
                tot_Pg += 1
            elif len(sub_list) == 3:
                tot_Pg += 3
    
    print(tot_Pg)

    tot_Pd = 0
    for canto in paradiso_rimanti_list:
        canto_index = paradiso_rimanti_list.index(canto)
        canto_to_analyse = paradiso_rimanti_list[canto_index]
        for sub_list in canto_to_analyse:
            if len(sub_list) == 2:
                tot_Pd += 1
            elif len(sub_list) == 3:
                tot_Pd += 3
    
    print(tot_Pd)

    tot_dante = tot_If + tot_Pg + tot_Pd
    print(tot_dante)

if __name__ == "__main__":
    main()