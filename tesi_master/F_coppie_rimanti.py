import re
import json
import itertools

def main():

    # Importing the json files and opening it as a python list
    # Inferno
    inferno = open('tesi_master/inferno_rimanti.json')
    inferno_rimanti_list = json.load(inferno)

    # Purgtorio
    purgatorio = open('tesi_master/purgatorio_rimanti.json')
    purgatorio_rimanti_list = json.load(purgatorio)

    # Paradiso
    paradiso = open('tesi_master/paradiso_rimanti.json')
    paradiso_rimanti_list = json.load(paradiso)

    # Orlando Furioso
    OrlandoFurioso = open('tesi_master/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # INFERNO
    if_opera_completa = []
    for canto in inferno_rimanti_list :
        for gruppo_rimanti in canto:
            if_opera_completa.append(gruppo_rimanti)

    if_coppie_rimanti = []
    for gruppo_rimanti in if_opera_completa :
        if len(gruppo_rimanti) < 3:
            if_coppie_rimanti.append(gruppo_rimanti)
        elif len(gruppo_rimanti) == 3:
            combinations = list(itertools.combinations(gruppo_rimanti, 2))
            for combination in combinations:
                if_coppie_rimanti.append(combination)

    print(len(if_coppie_rimanti))    
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

    print(len(pg_coppie_rimanti))

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

    print(len(pd_coppie_rimanti))

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

    print(len(of_coppie_rimanti))



if __name__ == "__main__":
    main()