import itertools
import math

def main():

    a = [['A', 'B', 'W'], ['X', 'Y', 'U']]

    x = [['B', 'C'], ['A', 'B', 'X'], ['A', 'B', 'E'], ['X', 'Y', 'H'], ['Y', 'F', 'Z']]

    x_paires = []
    for rimanti in x:
        x_combinations = list((itertools.combinations(sorted(rimanti), 2)))
        x_paires.append(x_combinations)

    flattened = []
    for sub_list in x_paires:
        for tuple in sub_list:
            flattened.append(tuple)
    print(flattened)

    captured = []
    for a_list in a:
        a_combinations = list(itertools.combinations(sorted(a_list), 2))
        if a_combinations[0] in flattened:
            captured.append(a_list)
        elif a_combinations[1] in flattened:
            captured.append(a_list)
        elif a_combinations[2] in flattened:
            captured.append(a_list)
    
    print(captured)
        

    # print(captured)

    # a = [['A', 'B', 'C'], ['X', 'Y', 'Z']]

    # x = [[[['B', 'C'], ['A', 'B', 'X'], ['B', 'C', 'E']]]]

    # indexes = []
    # x_paires = []
    # for cantica_idx, cantica in enumerate(x):
    #     for canto_idx, canto in enumerate(cantica):
    #         for rimanti_idx, rimanti in enumerate(canto):
    #             x_combinations = list(itertools.combinations(rimanti, 2))
    #             x_paires.append(x_combinations)
    #             indexes.append((x_combinations, [cantica_idx, canto_idx, rimanti_idx]))
    
    # x_paires_sorted = []
    # for rimanti in x_paires:
    #     for couples in rimanti: 
    #         x_paires_sorted.append(sorted(couples))

    # caputred = []
    # for a_list in a:
    #     a_combinations = [list(itertools.combinations(a_list, 2))]
    #     if all(set(combination) in x_paires_sorted for combination in a_combinations):
    #         caputred.append([a_list, a.index(a_list)])
    # print(caputred) 

    # caputred = []
    # for a_list in a:
    #     for idx, couple in enumerate(x_paires_sorted):
    #         if (a_list[0] in couple and a_list[1] in couple):
    #             t = [a_list[0], a_list[2]]
    #             u = [a_list[1], a_list[2]]
    #             for couple in x_paires_sorted:
    #                 if t == couple:
    #                     caputred.append([a_list, t, indexes[idx]])
    #                     break
    #                 elif u == couple:
    #                     caputred.append([a_list, t, indexes[idx]])
    #                     break
    #         elif (a_list[0] in couple and a_list[2] in couple):
    #             t = [a_list[1], a_list[2]]
    #             u = [a_list[0], a_list[1]]
    #             for couple in x_paires_sorted:
    #                 if t == couple:
    #                     caputred.append([a_list, t, indexes[idx]])
    #                     break
    #                 elif u == couple:
    #                     caputred.append([a_list, t, indexes[idx]])
    #                     break
    #         elif (a_list[1] in couple and a_list[2] in couple):
    #             t = [a_list[0], a_list[2]]
    #             u = [a_list[0], a_list[1]]
    #             for couple in x_paires_sorted:
    #                 if t == couple:
    #                     caputred.append([a_list, t, indexes[idx]])
    #                     break
    #                 elif u == couple:
    #                     caputred.append([a_list, t, indexes[idx]])
    #                     break
    # print(caputred) 

    # position = []
    # for element in caputred:
    #     for rimanti in x_paires:
    #         for couples in rimanti:
    #             if element[1] == couples:
    #                 if x_paires.index(rimanti) == 0:
    #                     verso = (x_paires.index(rimanti) + 1)
    #                 elif x_paires.index(rimanti) != 0:
    #                     verso = ((x_paires.index(rimanti) +1) * 3)
    #                 # print(x_paires.index(rimanti))
    #                 # print(rimanti)
    #                 #verso = (x_paires.index(rimanti) + 2)
    #                 # print(verso)
    #                 # canto = x_paires.index(rimanti)
    #                 position.append([rimanti, verso])

        
    # print(position)                     

if __name__ == "__main__":
    main()