import json
import itertools
import math
import re

def main():
    # Script H: cleanup of the json files to print in the Appendix of the mémoire. Each dictionary is a little different so they could not be cleand up all at the same time

    # Category A
    with open('json_files/dictionaries_json/group_A.json', 'r') as dictionary:
        json_1_dic = dictionary.read()

    clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    no_uglies = re.sub(r'(\])\,\s(\}\,)', r'\1\2', no_double_spaces)
    no_virgolette = re.sub(r'\"', '', no_uglies)
    no_curly_1 = re.sub(r'\{', '', no_virgolette)
    no_curly_2 = re.sub(r'\}', '', no_curly_1)
    puntovirgola = re.sub(r'(\d{1,3}\,\s\d{1,3}),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', no_curly_2)
    puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    no_rimanti_par = re.sub(r'\[(\D{2,})\,(\s\D{2,})\]\,(\s)', r'\1\2\3', puntovirgola_2)
    
    with open("json_files/dictionaries_json/groupA.txt", "w") as testing:
        testing.write(no_rimanti_par)


    # Category B
    with open('json_files/dictionaries_json/group_B.json', 'r') as dictionary:
        json_1_dic = dictionary.read()

    clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    no_uglies = re.sub(r'(\])\,\s(\}\,)', r'\1\2', no_double_spaces)
    no_virgolette = re.sub(r'\"', '', no_uglies)
    no_curly_1 = re.sub(r'\{', '', no_virgolette)
    no_curly_2 = re.sub(r'\}', '', no_curly_1)
    puntovirgola = re.sub(r'(\d{1,3}\,\s\d{1,3}),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', no_curly_2)
    puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    no_rimanti_par = re.sub(r'\[(\D{2,})\,(\s\D{2,})\]\,(\s)', r'\1\2\3', puntovirgola_2)
    
    with open("json_files/dictionaries_json/groupB.txt", "w") as testing:
        testing.write(no_rimanti_par)


    # Category C
    with open('json_files/dictionaries_json/group_C.json', 'r') as dictionary:
        json_1_dic = dictionary.read()

    clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    no_uglies = re.sub(r'\]\, (\}\,)', r'\1', no_double_spaces)
    no_double_par = re.sub(r'\](\}\,)', r'\1', no_uglies)
    no_virgolette = re.sub(r'\"', '', no_double_par)
    no_curly_1 = re.sub(r'\{', '', no_virgolette)
    no_curly_2 = re.sub(r'\}', '', no_curly_1)
    puntovirgola = re.sub(r'(\d{1,3}\,\s\d{1,3}),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', no_curly_2)
    puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    last_par = re.sub(r'(\[\d{1,3}\,\s\d{1,3})(\;\n)', r'\1]\2', puntovirgola_2)
    no_rimanti_par = re.sub(r'\[(\w{2,})\,(\s\w{2,})\,(\s\w{2,})\]\,(\s)', r'\1\2\3\4', last_par)

    with open("json_files/dictionaries_json/groupC.txt", "w") as testing:
        testing.write(no_rimanti_par)


    # Category D
    with open('json_files/dictionaries_json/group_D.json', 'r') as dictionary:
        json_1_dic = dictionary.read()

    clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    no_uglies = re.sub(r'\]\, (\}\,)', r'\1', no_double_spaces)
    no_double_par = re.sub(r'\](\}\,)', r'\1', no_uglies)
    no_virgolette = re.sub(r'\"', '', no_double_par)
    no_curly_1 = re.sub(r'\{', '', no_virgolette)
    no_curly_2 = re.sub(r'\}', '', no_curly_1)
    puntovirgola_1 = re.sub(r'\,(\n)', r';\1', no_curly_2)
    square_par = re.sub(r'([I, F, P, D, G]{2}\:\s\[\d{1,3}\,\s\d{1,3})(;)', r'\1]\2', puntovirgola_1)
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', square_par)
    
    with open("json_files/dictionaries_json/groupD.txt", "w") as testing:
        testing.write(puntovirgola_2)

    # Category E
    with open('json_files/dictionaries_json/group_E.json', 'r') as dictionary:
        json_1_dic = dictionary.read()

    clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    no_uglies = re.sub(r'\]\, (\}\,)', r'\1', no_double_spaces)
    no_double_par = re.sub(r'\](\}\,)', r'\1', no_uglies)
    no_virgolette = re.sub(r'\"', '', no_double_par)
    no_curly_1 = re.sub(r'\{', '', no_virgolette)
    no_curly_2 = re.sub(r'\}', '', no_curly_1)
    puntovirgola = re.sub(r'(\d{1,3}\,\s\d{1,3}),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', no_curly_2)
    puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    last_par = re.sub(r'(\[\d{1,3}\,\s\d{1,3})(\;\n)', r'\1]\2', puntovirgola_2)
    no_rimanti_par = re.sub(r'\[(\w{2,})\,(\s\w{2,})\,(\s\w{2,})\]\,(\s)', r'\1\2\3\4', last_par)
    

    with open("json_files/dictionaries_json/groupE.txt", "w") as testing:
        testing.write(no_rimanti_par)


    

if __name__ == "__main__":
    main()