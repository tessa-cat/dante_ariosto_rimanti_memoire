import re
import json

def main():
    # Script D: This script is not particularly useful to the overall work. It simply counts the number of couples of rimanti inside each work, and it's then used for the first calcultion based on couples. A couple of rimanti is defined as the splitting of a group of three rimanti into three couples of two rimanti: for example the group feltro-peltro-veltro would become feltro-peltro; feltro-veltro; and peltro_veltro

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

    # Total number of couples of rimanti in OF
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

    # Total number of couples of rimanti in IF
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

    # Total number of couples of rimanti in PG
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

    # Total number of couples of rimanti in PD
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

    # Total number of couples of rimanti in the whole Commedia
    tot_dante = tot_If + tot_Pg + tot_Pd
    print(tot_dante)

if __name__ == "__main__":
    main()