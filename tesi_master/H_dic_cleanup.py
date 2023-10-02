import json
import itertools
import math
import re

def main():
    # with open('tesi_master/json_files/dictionaries_json/groups_three_from_two.txt', 'r') as dictionary:
    # # Reading from json file
    #     json_1_dic = dictionary.read()

    # clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    # clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    # clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    # no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    # new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    # no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    # no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    # no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    # no_uglies = re.sub(r'\]\, (\}\,)', r'\1', no_double_spaces)
    # no_double_par = re.sub(r'\](\}\,)', r'\1', no_uglies)
    # no_par = re.sub(r'(\[\"\w{2,}\"\, \"\w{2,}\"\]\, \d{1,3}\,\s\d{1,3})\](\,\s\")', r'\1\2', no_double_par)
    # no_virgolette = re.sub(r'\"', '', no_par)
    # last_cleanup = re.sub(r'(\[\w{2,}\,\s\w{2,}\]\,\s\d{1,3}\,\s\d{1,3})\](\,\s\[\w{2,}\,)', r'\1\2', no_virgolette)
    # no_curly_1 = re.sub(r'\{', '', last_cleanup)
    # no_curly_2 = re.sub(r'\}', '', no_curly_1)
    # puntovirgola = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s\D{2}\:\s\[)', r'\1;\2', no_curly_2)
    # puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    

    # with open("tesi_master/json_files/dictionaries_json/dic1.txt", "w") as testing:
    #     testing.write(puntovirgola_1)

    # with open('tesi_master/json_files/dictionaries_json/groups_three_from_three.txt', 'r') as dictionary:
    # # Reading from json file
    #     json_1_dic = dictionary.read()

    # clean_file_if = re.sub(r'"IF": \[\],', '', json_1_dic)
    # clean_file_pg = re.sub(r'"PG": \[\],', '', clean_file_if)
    # clean_file_pd = re.sub(r'"PD": \[\]', '', clean_file_pg)
    # no_underscore = re.sub(r'\_', ' ', clean_file_pd)
    # new_lines = re.sub(r'(\},) (")', r'\1\n\2', no_underscore)
    # no_multiple_open = re.sub(r'\[{2,}', r'[', new_lines)
    # no_multiple_close = re.sub(r'\]{2,}', r']', no_multiple_open)
    # no_double_spaces = re.sub(r'\s{2,}', ' ', no_multiple_close)
    # no_uglies = re.sub(r'\]\, (\}\,)', r'\1', no_double_spaces)
    # no_double_par = re.sub(r'\](\}\,)', r'\1', no_uglies)
    # no_par = re.sub(r'(\[\"\w{2,}\"\, \"\w{2,}\"\, \"\w{2,}\"\]\, \d{1,3}\,\s\d{1,3})\](\,\s\")', r'\1\2', no_double_par)
    # no_virgolette = re.sub(r'\"', '', no_par)
    # last_cleanup = re.sub(r'(\[\w{2,}\,\s\w{2,}\,\s\w{2,}\]\,\s\d{1,3}\,\s\d{1,3})\](\,\s\[\w{2,}\,)', r'\1\2', no_virgolette)
    # no_curly_1 = re.sub(r'\{', '', last_cleanup)
    # no_curly_2 = re.sub(r'\}', '', no_curly_1)
    # puntovirgola = re.sub(r'(\d{1,3}\,\s\d{1,3}),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', no_curly_2)
    # puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    # puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    

    # with open("tesi_master/json_files/dictionaries_json/dic2.txt", "w") as testing:
    #     testing.write(puntovirgola_2)

    with open('tesi_master/json_files/dictionaries_json/groups_two_from_three.txt', 'r') as dictionary:
    # Reading from json file
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
    no_par = re.sub(r'(\[\"\w{2,}\"\, \"\w{2,}\"\, \"\w{2,}\"\]\, \d{1,3}\,\s\d{1,3})\](\,\s\")', r'\1\2', no_double_par)
    no_virgolette = re.sub(r'\"', '', no_par)
    last_cleanup = re.sub(r'(\[\w{2,}\,\s\w{2,}\,\s\w{2,}\]\,\s\d{1,3}\,\s\d{1,3})\](\,\s\[\w{2,}\,)', r'\1\2', no_virgolette)
    no_curly_1 = re.sub(r'\{', '', last_cleanup)
    no_curly_2 = re.sub(r'\}', '', no_curly_1)
    puntovirgola = re.sub(r'(\d{1,3}\,\s\d{1,3}),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', no_curly_2)
    puntovirgola_1 = re.sub(r'\,(\n)', r';\1', puntovirgola)
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    no_square = re.sub(r'(\[\w{2,}\,\s\w{2,}\,\s\w{2,}\],\s\d{1,3}\,\s\d{1,3})]', r'\1', puntovirgola_2 )
    

    with open("tesi_master/json_files/dictionaries_json/dic3.txt", "w") as testing:
        testing.write(no_square)

    with open('tesi_master/json_files/dictionaries_json/groups_of_two.txt', 'r') as dictionary:
    # Reading from json file
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
    

    with open("tesi_master/json_files/dictionaries_json/dic4.txt", "w") as testing:
        testing.write(puntovirgola_2)
    
    with open('tesi_master/json_files/dictionaries_json/groups_of_three.txt', 'r') as dictionary:
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
    puntovirgola_2 = re.sub(r'(\[\d{1,3}\,\s\d{1,3}\]),(\s[I, F, P, D, G]{2}\:)', r'\1;\2', puntovirgola_1)
    square_par = re.sub(r'(\[\d{1,3}\,\s\d{1,3})(\;\n)', r'\1]\2', puntovirgola_2)
    

    with open("tesi_master/json_files/dictionaries_json/dic5.txt", "w") as testing:
        testing.write(square_par)

if __name__ == "__main__":
    main()