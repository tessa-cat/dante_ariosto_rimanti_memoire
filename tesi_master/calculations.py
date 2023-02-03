import re
import json

def main():

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

    # Orlando Furioso
    OrlandoFurioso = open('orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # Trying first with one canto for each
    if_1_list = inferno_rimanti_list[0]
    of_1_list = of_rimanti_list[45]

    value = 0
    # First we cycle through the sublists of rimanti in the specific Dante canto
    for sub_list in if_1_list:
        # Determining the index of the sub_list in question because otherwise I will get lost
        if_index = if_1_list.index(sub_list)
        # First and last pair of rimanti of each canto
        if if_index == 0 or if_index == (len(if_1_list) - 1):
           # Cycling through the list of the rimanti in the Orlando Furioso to check against
           for sub_list in of_1_list:
               # Again index of each sublist to not get lost
               of_index = of_1_list.index(sub_list)
               # This statement is true if both the rimanti in the Dante's canto are found in one of the sub_list of rimanti of the Ariosto canto
               if if_1_list[if_index][0] in of_1_list[of_index] and if_1_list[if_index][1] in of_1_list[of_index]:
                   print(if_1_list[if_index][0], if_1_list[if_index][1], of_1_list[of_index])
        # Sub_lists of three rimanti
        elif if_index != 0 and if_index != (len(if_1_list) - 1):
            for sub_list in of_1_list:
                # The sub_lists are as follows: [A, B, C]
                # 1 complete point assigned if all three are in the OF sub_list
                # First case, A and B are in one of the OF sub_lists (1/3 points)
                if if_1_list[if_index][0] in of_1_list[of_index] and if_1_list[if_index][1] in of_1_list[of_index]:
                   print(if_1_list[if_index][0], if_1_list[if_index][1],of_1_list[of_index])
                # Second case, A and C are in one of the OF sub_lists (1/3 points)
                if if_1_list[if_index][0] in of_1_list[of_index] and if_1_list[if_index][2] in of_1_list[of_index]:
                    print(if_1_list[if_index][0], if_1_list[if_index][2],of_1_list[of_index])
                # Third case, B and C are in one of the OF sub_lists (1/3 points)
                if if_1_list[if_index][1] in of_1_list[of_index] and if_1_list[if_index][2] in of_1_list[of_index]:
                   print(if_1_list[if_index][1], if_1_list[if_index][2],of_1_list[of_index])

if __name__ == "__main__":
    main()