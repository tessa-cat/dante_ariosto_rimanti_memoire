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

    # INFERNO
    value_inferno = 0
    for canto_D in inferno_rimanti_list : 
        # Index of each canto in the list
        canto_D_index = inferno_rimanti_list.index(canto_D)
        # Accessing the specific canto to cycle through
        canto_D_to_analyse = inferno_rimanti_list[canto_D_index]

        #Cycling through each canto of Orlando Furioso
        for canto_A in of_rimanti_list:
            canto_A_index = of_rimanti_list.index(canto_A)
            canto_A_to_analyse = of_rimanti_list[canto_A_index]
            # First we cycle through the sublists of rimanti in the specific Dante canto
            for sub_list_D in canto_D_to_analyse:
                # Determining the index of the sub_list in question because otherwise I will get lost
                if_index = canto_D_to_analyse.index(sub_list_D)

                # First and last pair of rimanti of each canto
                if if_index == 0 or if_index == (len(canto_D_to_analyse) - 1):
                # Cycling through the list of the rimanti in the Orlando Furioso to check against
                    for sub_list_A in canto_A_to_analyse:
                        # Again index of each sublist to not get lost
                        of_index = canto_A_to_analyse.index(sub_list_A)
                        # This statement is true if both the rimanti in the Dante's canto are found in one of the sub_list of rimanti of the Ariosto canto
                        if canto_D_to_analyse[if_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[if_index][1] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[if_index][0], canto_D_to_analyse[if_index][1], canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_inferno += 1/3

                # Sub_lists of three rimanti
                elif if_index != 0 and if_index != (len(canto_D_to_analyse) - 1):
                    for sub_list_A in canto_A_to_analyse:
                        # Again index of each sublist to not get lost
                        of_index = canto_A_to_analyse.index(sub_list_A)
                        # The sub_lists are as follows: [A, B, C]
                        # 1 complete point assigned if all three are in the OF sub_list
                        # First case, A and B are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[if_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[if_index][1] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[if_index][0], canto_D_to_analyse[if_index][1],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_inferno += 1/3
                        # Second case, A and C are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[if_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[if_index][2] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[if_index][0], canto_D_to_analyse[if_index][2],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_inferno += 1/3
                        # Third case, B and C are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[if_index][1] in canto_A_to_analyse[of_index] and canto_D_to_analyse[if_index][2] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[if_index][1], canto_D_to_analyse[if_index][2],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_inferno += 1/3
    
    tot_inferno = (value_inferno/33894)*100
    tot_inferno_strg = str(tot_inferno)
    print('Inferno: '+tot_inferno_strg)

    # PURGATORIO
    value_purgatorio = 0
    for canto_D in purgatorio_rimanti_list : 
        # Index of each canto in the list
        canto_D_index = purgatorio_rimanti_list.index(canto_D)
        # Accessing the specific canto to cycle through
        canto_D_to_analyse = purgatorio_rimanti_list[canto_D_index]

        #Cycling through each canto of Orlando Furioso
        for canto_A in of_rimanti_list:
            canto_A_index = of_rimanti_list.index(canto_A)
            canto_A_to_analyse = of_rimanti_list[canto_A_index]
            # First we cycle through the sublists of rimanti in the specific Dante canto
            for sub_list_D in canto_D_to_analyse:
                # Determining the index of the sub_list in question because otherwise I will get lost
                pg_index = canto_D_to_analyse.index(sub_list_D)

                # First and last pair of rimanti of each canto
                if pg_index == 0 or pg_index == (len(canto_D_to_analyse) - 1):
                # Cycling through the list of the rimanti in the Orlando Furioso to check against
                    for sub_list_A in canto_A_to_analyse:
                        # Again index of each sublist to not get lost
                        of_index = canto_A_to_analyse.index(sub_list_A)
                        # This statement is true if both the rimanti in the Dante's canto are found in one of the sub_list of rimanti of the Ariosto canto
                        if canto_D_to_analyse[pg_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pg_index][1] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][0], canto_D_to_analyse[pg_index][1], canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_purgatorio += 1/3

                # Sub_lists of three rimanti
                elif pg_index != 0 and pg_index != (len(canto_D_to_analyse) - 1):
                    for sub_list_A in canto_A_to_analyse:
                        # Again index of each sublist to not get lost
                        of_index = canto_A_to_analyse.index(sub_list_A)
                        # The sub_lists are as follows: [A, B, C]
                        # 1 complete point assigned if all three are in the OF sub_list
                        # First case, A and B are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[pg_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pg_index][1] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][0], canto_D_to_analyse[pg_index][1],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_purgatorio += 1/3
                        # Second case, A and C are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[pg_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pg_index][2] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][0], canto_D_to_analyse[pg_index][2],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_purgatorio += 1/3
                        # Third case, B and C are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[pg_index][1] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pg_index][2] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][1], canto_D_to_analyse[pg_index][2],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_purgatorio += 1/3
    
    tot_purgatorio = (value_purgatorio/33894)*100
    tot_purgatorio_str = str(tot_purgatorio)
    print('Purgatorio: '+tot_purgatorio_str)

    # PARADISO
    value_paradiso = 0
    for canto_D in paradiso_rimanti_list : 
        # Index of each canto in the list
        canto_D_index = paradiso_rimanti_list.index(canto_D)
        # Accessing the specific canto to cycle through
        canto_D_to_analyse = paradiso_rimanti_list[canto_D_index]

        #Cycling through each canto of Orlando Furioso
        for canto_A in of_rimanti_list:
            canto_A_index = of_rimanti_list.index(canto_A)
            canto_A_to_analyse = of_rimanti_list[canto_A_index]
            # First we cycle through the sublists of rimanti in the specific Dante canto
            for sub_list_D in canto_D_to_analyse:
                # Determining the index of the sub_list in question because otherwise I will get lost
                pd_index = canto_D_to_analyse.index(sub_list_D)

                # First and last pair of rimanti of each canto
                if pd_index == 0 or pd_index == (len(canto_D_to_analyse) - 1):
                # Cycling through the list of the rimanti in the Orlando Furioso to check against
                    for sub_list_A in canto_A_to_analyse:
                        # Again index of each sublist to not get lost
                        of_index = canto_A_to_analyse.index(sub_list_A)
                        # This statement is true if both the rimanti in the Dante's canto are found in one of the sub_list of rimanti of the Ariosto canto
                        if canto_D_to_analyse[pd_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pd_index][1] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][0], canto_D_to_analyse[pg_index][1], canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_paradiso += 1/3

                # Sub_lists of three rimanti
                elif pd_index != 0 and pd_index != (len(canto_D_to_analyse) - 1):
                    for sub_list_A in canto_A_to_analyse:
                        # Again index of each sublist to not get lost
                        of_index = canto_A_to_analyse.index(sub_list_A)
                        # The sub_lists are as follows: [A, B, C]
                        # 1 complete point assigned if all three are in the OF sub_list
                        # First case, A and B are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[pd_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pd_index][1] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][0], canto_D_to_analyse[pg_index][1],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_paradiso += 1/3
                        # Second case, A and C are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[pd_index][0] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pd_index][2] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][0], canto_D_to_analyse[pg_index][2],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_paradiso += 1/3
                        # Third case, B and C are in one of the OF sub_lists (1/3 points)
                        if canto_D_to_analyse[pd_index][1] in canto_A_to_analyse[of_index] and canto_D_to_analyse[pd_index][2] in canto_A_to_analyse[of_index]:
                            #print(canto_D_to_analyse[pg_index][1], canto_D_to_analyse[pg_index][2],canto_A_to_analyse[of_index], canto_D_index, canto_A_index)
                            value_paradiso += 1/3
    
    tot_paradiso = (value_paradiso/33894)*100
    tot_paradiso_str = str(tot_paradiso)
    print('Paradiso: '+tot_paradiso_str)

    totale = ((value_inferno + value_purgatorio + value_paradiso)/33894)*100
    totale_str = str(totale)
    print('Totale opera: '+totale_str)

if __name__ == "__main__":
    main()