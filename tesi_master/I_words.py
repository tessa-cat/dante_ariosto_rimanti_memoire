import re
import json
import itertools

def main():
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

    dante_rimanti = []
    for canto in inferno_rimanti_list:
        for sub_list in canto:
            for word in sub_list:
                dante_rimanti.append(word)
    for canto in purgatorio_rimanti_list:
        for sub_list in canto:
            for word in sub_list:
                dante_rimanti.append(word)
    for canto in paradiso_rimanti_list:
        for sub_list in canto:
            for word in sub_list:
                dante_rimanti.append(word)

    dante_set = set(dante_rimanti)

    # print(len(dante_rimanti))
    # print(len(dante_set))

    of_rimanti = []
    for canto in of_rimanti_list:
        for sub_list in canto:
            for word in sub_list:
                of_rimanti.append(word)

    of_set = set(of_rimanti)
    
    # print(len(of_rimanti))
    # print(len(of_set))
    #print(of_rimanti)
    #print(of_set)

    all_different_rimanti = of_set.union(dante_set)
    # print(len(all_different_rimanti))
    # print(all_different_rimanti)

    rimanti_sorted = sorted(all_different_rimanti)

    my_list = []
    for word in dante_set:
        if word not in of_set:
            my_list.append(word)

    for word in of_set:
        if word not in dante_set:
            my_list.append(word)

    new_list = sorted(my_list)
            

    print(len(new_list))

    with open ('different_rimanti.json', 'w') as rimanti:
        json.dump(new_list, rimanti)

if __name__ == "__main__":
    main()