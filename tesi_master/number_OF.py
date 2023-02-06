import re
import json

def main():
    OrlandoFurioso = open('orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    tot_couple_rimanti = 0

    for canto in of_rimanti_list:
        canto_index = of_rimanti_list.index(canto)
        canto_to_analyse = of_rimanti_list[canto_index]
        for sub_list in canto_to_analyse:
            if len(sub_list) == 2:
                tot_couple_rimanti += 1
            elif len(sub_list) == 3:
                tot_couple_rimanti += 3
    
    print(tot_couple_rimanti)

if __name__ == "__main__":
    main()