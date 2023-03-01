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

    dante_rimanti = []
    if_rimanti = []
    pg_rimanti = []
    pd_rimanti = []
    for canto in inferno_rimanti_list:
        for sub_list in canto:
            dante_rimanti.append(sub_list)
            if_rimanti.append(sub_list)
    for canto in purgatorio_rimanti_list:
        for sub_list in canto:
            dante_rimanti.append(sub_list)
            pg_rimanti.append(sub_list)
    for canto in paradiso_rimanti_list:
        for sub_list in canto:
            dante_rimanti.append(sub_list)
            pd_rimanti.append(sub_list)

    

    #print(dante_rimanti)

    # Orlando Furioso
    OrlandoFurioso = open('/Users/tessacattaneo/Desktop/Dante_Rime/tesi_master/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # number_of_three_rimanti_of = 0
    # for canto in of_rimanti_list:
    #     for sub_list in canto: 
    #         if len(sub_list) == 3:
    #             number_of_three_rimanti_of += 1
    # print(number_of_three_rimanti_of)
    ## The number is 9684

    # three_rimanti_sorted = []
    # for a_canto in of_rimanti_list:
    #     for of_sublist in a_canto: 
    #         if len(of_sublist) == 3:
    #             for d_sublist in dante_rimanti:
    #                 if sorted(of_sublist) == sorted(d_sublist):
    #                     value = str(of_sublist) + str(of_rimanti_list.index(a_canto)) + ' '+ str(a_canto.index(of_sublist))
    #                     three_rimanti_sorted.append(value)
    #                     #print(of_sublist, of_rimanti_list.index(a_canto), a_canto.index(of_sublist))
    #                     break
    # #print(three_rimanti_sorted)
    # print(len(three_rimanti_sorted))
    ## The length is 840

    three_rimanti_if = []
    for a_canto in of_rimanti_list:
        for of_sublist in a_canto: 
            if len(of_sublist) == 3:
                for d_sublist in if_rimanti:
                    if sorted(of_sublist) == sorted(d_sublist):
                        # value = str(of_sublist) + str(of_rimanti_list.index(a_canto)) + ' '+ str(a_canto.index(of_sublist))
                        three_rimanti_if.append(of_sublist)
                        break
    #print(three_rimanti_sorted)
    #print(len(three_rimanti_if))

    three_rimanti_pg = []
    for a_canto in of_rimanti_list:
        for of_sublist in a_canto: 
            if len(of_sublist) == 3:
                for d_sublist in pg_rimanti:
                    if sorted(of_sublist) == sorted(d_sublist):
                        # value = str(of_sublist) + str(of_rimanti_list.index(a_canto)) + ' '+ str(a_canto.index(of_sublist))
                        three_rimanti_pg.append(of_sublist)
                        break
    #print(three_rimanti_sorted)
    #print(len(three_rimanti_pg))

    three_rimanti_pd = []
    for a_canto in of_rimanti_list:
        for of_sublist in a_canto: 
            if len(of_sublist) == 3:
                for d_sublist in pd_rimanti:
                    if sorted(of_sublist) == sorted(d_sublist):
                        # value = str(of_sublist) + str(of_rimanti_list.index(a_canto)) + ' '+ str(a_canto.index(of_sublist))
                        three_rimanti_pd.append(of_sublist)
                        break
    #print(three_rimanti_sorted)
    #print(len(three_rimanti_pd))


    #print(three_rimanti_if)
    if_sorted = []
    for sub_list in three_rimanti_if:
        if_sorted.append(sorted(sub_list))

    if_set = set(tuple(i) for i in if_sorted)
    print(len(if_set)) # 186 --> it could be interesting to see if the rimanti are all taken from the same place. For example, if we were to make a list of all the repetitions and see if they are repeated in Dante as well then we could easily compare the verses in question and truly try to understand if it is a citation, a coincidence, an "easy" rhyme, or citations of different places of Dante.
    print(if_set)

    # for sub_list_if in three_rimanti_if:
    #     for sub_list_pg in three_rimanti_pg:
    #         if sorted(sub_list_if) == sorted(sub_list_pg):
    #             print(sub_list_if)



if __name__ == "__main__":
    main()