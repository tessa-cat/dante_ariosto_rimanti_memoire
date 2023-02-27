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

    dante_rimanti = []
    for canto in inferno_rimanti_list:
        dante_rimanti.append(canto)
    for canto in purgatorio_rimanti_list:
        dante_rimanti.append(canto)
    for canto in paradiso_rimanti_list:
        dante_rimanti.append(canto)

    #print(len(dante_rimanti))

    # Orlando Furioso
    OrlandoFurioso = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    for a_canto in of_rimanti_list:
        for of_sublist in a_canto: 
            if len(of_sublist) == 3:
                for d_canto in dante_rimanti:
                    for d_sublist in d_canto:
                        if sorted(of_sublist) == sorted(d_sublist):
                            print(of_sublist)
                            break


if __name__ == "__main__":
    main()