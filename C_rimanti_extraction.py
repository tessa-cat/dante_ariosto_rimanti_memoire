import re
import os
import json


def main():
    # Script C: Extracting the rimanti from each canto

    # Some words present different spelling, since the two works have a long written tradition
    # editions vary greatly. The different spellings are here accounted for, even though
    # with this method it's impossible to determine weather or not all different spellings of 
    # the same word were found. This was done by creating an alphabetized list of all rimanti which
    # appeared in only one of the works, then manually reading through it and finding possible 
    # couples of differently spelled words. This type of work is impossible to accomplish 
    # without a thorough knowledge of the italian language and at least some notion of 
    # of how it evolved through history.

    words_replace = [
        ['abandona', 'abbandona'],
        ['abandoni', 'abbandoni'],
        ['abandono', 'abbandono'],
        ['abonda', 'abbonda'],
        ['acanto', 'accanto'],
        ['aguto', 'acuto'],
        ['aguta', 'acuta'],
        ['aguti', 'acuti'],
        ['agute', 'acute'],
        ['adorna', 'addorna'],
        ['adombra', 'aombra'],
        ['aguati', 'agguati'],
        ['altretanto', 'altrettanto'],
        ['argomenti', 'argumenti'],
        ['argomento', ' argumento'],
        ['avampa', 'avvampa'],
        ['avede', 'avvede'],
        ['aventa', 'avventa'],
        ['avicini', 'avvicini'],
        ['avolti', 'avvolti'],
        ['benetetto', 'benedetto'],
        ['camina', 'cammina'],
        ['camino', 'cammino'],
        ['castiga', 'gastiga'],
        ['cavalieri', 'cavallieri'],
        ['cheta', 'quieta'],
        ['cobrire', 'coprire'],
        ['comandato', 'commandato'],
        ['concedi', 'conciedi'],
        ['coscienza', 'conscienza'],
        ['consperso', 'cosperso'],
        ['costante', 'constante'],
        ['desira', 'disira'],
        ['devote', 'divote'],
        ['dimanda', 'domanda'],
        ['dispose', 'dispuose'],
        ['dimanda', 'domanda'],
        ['dimando', 'domando'],
        ['entrata', 'intrata'],
        ['entrai', 'intrai'],
        ['entrare', 'intrare'],
        ['esausto', 'essausto'],
        ['eterna', 'etterna'],
        ['eterno', 'etterno'],
        ['evangelista', 'vangelista'],
        ['evangelo', 'vangelo'],
        ['gualoppo', 'galoppo'],
        ['iguali', 'uguali'],
        ['imperadrice', 'imperatrice'],
        ['imperadore', 'imperatore'],
        ['entrare', 'intrare'],
        ['isnella', 'snella'],
        ['istrane', 'strane'],
        ['matutina', 'mattutina'],
        ['mbianca', 'imbianca'],
        ['mpiastro', 'impiastro'],
        ['mpresa', 'impresa'],
        ['ncarco', 'incarco'],
        ['ncontra', 'incontra'],
        ['ncrebbe', 'increbbe'],
        ['nganno', 'inganno'],
        ['nganni', 'inganni'],
        ['ngegno', 'ingegno'],
        ['ngegni', 'ingegni'],
        ['ngrossa', 'ingrossa'],
        ['nnamora', 'innamora'],
        ['nobiltade', 'nobilitade'],
        ['nsegna', 'insegna'],
        ['nsembre', 'insembre'],
        ['nsieme', 'insieme'],
        ['ntelletto', 'intelletto'],
        ['ntesa', 'intesa'],
        ['ntese', 'intese'],
        ['nteso', 'inteso'],
        ['nvito', 'invito'],
        ['nvoglia', 'invoglia'],
        ['nvolti', 'involti'],
        ['opinione', 'oppinione'],
        ['ormai', 'oramai'],
        ['pellegrina', 'peregrina'],
        ['ramenta', 'rammenta'],
        ['recetto', 'ricetto'],
        ['reposta', ' riposta'],
        ['respetto', 'rispetto'],
        ['reciso', 'riciso'],
        ['ritruova', 'ritrova'],
        ['ritruove', 'ritrove'],
        ['segnore', 'signore'],
        ['soblima', 'sublima'],
        ['soblima', 'sublima'],
        ['sone', 'suone'],
        ['suprema', 'supprema'],
        ['ubidente', 'ubbidiente'],
        ['ubidente', 'ubbidiente'],
        ['zafiro', 'zaffiro'],
    ]

    # ### INFERNO ###
    # # Directory
    # folder = 'Inferno'

    # #Comprehensive list of all the rimanti sublists by canto
    # inferno_rimanti_list = []

    # for filename in sorted(os.listdir(folder)):
    #     if filename.endswith('.txt'):
    #         filepath = os.path.join(folder, filename)

    #         # Opening the canto in read mode
    #         with open (filepath, 'r') as testing:
    #             canto = testing.read()
            
    #         # Accounting for different writing
    #         characters = canto.replace('à', 'a').replace('â', 'a').replace('è', 'e').replace('é', 'e').replace('ê', 'e').replace('ï', 'i').replace('í', 'i').replace('ì', 'i').replace('î', 'i').replace('ò', 'o').replace('ó', 'o').replace('ô', 'o').replace('ü', 'u').replace('ù', 'u').replace('ú', 'u')

    #         # Keeping only the rimante !this might not work for some rimanti!
    #         rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

    #         # Putting the rimanti in a list
    #         rimanti_list = rimanti.split("\n")
    #         # Making sure there are no empty entraces in the list
    #         if "" in rimanti_list:
    #             rimanti_list.remove("")

    #         #Making sure that the same rimanti's have the same written spelling
    #         for rimante in rimanti_list:
    #             r_i = rimanti_list.index(rimante)
    #             for list in words_replace:
    #                 if rimante in list:
    #                     rimanti_list[r_i] = list[1]

    #         if_rimanti_list = []
    #         # First set of rhymes A (B) A
    #         rimanti = rimanti_list[0], rimanti_list[2]
    #         if_rimanti_list.append(rimanti)

    #         # All of the rhymes in sets of three
    #         for rimante in range (1, len(rimanti_list)-5, 3):
    #             rimanti = rimanti_list[rimante], rimanti_list[rimante+2], rimanti_list[rimante+4]
    #             if_rimanti_list.append(rimanti)
            
    #         # Last set of rhymes X (Y) X
    #         rimanti = rimanti_list[-3], rimanti_list[-1]
    #         if_rimanti_list.append(rimanti)

    #         inferno_rimanti_list.append(if_rimanti_list)

    # ## PURGATORIO ###
    # #Directory
    # folder = 'Purgatorio'

    # #Comprehensive list of all the rimanti sublists by canto
    # purgatorio_rimanti_list = []

    # for filename in sorted(os.listdir(folder)):
    #     if filename.endswith('.txt'):
    #         filepath = os.path.join(folder, filename)

    #         # Opening the canti in read mode
    #         with open (filepath, 'r') as testing:
    #             canto = testing.read()

    #         # Accounting for different writing
    #         characters = canto.replace('à', 'a').replace('â', 'a').replace('è', 'e').replace('é', 'e').replace('ê', 'e').replace('ï', 'i').replace('í', 'i').replace('ì', 'i').replace('î', 'i').replace('ò', 'o').replace('ó', 'o').replace('ô', 'o').replace('ü', 'u').replace('ù', 'u').replace('ú', 'u')

    #         # Keeping only the rimante !this might not work for some rimanti!
    #         rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

    #         # Putting the rimanti in a list
    #         rimanti_list = rimanti.split("\n")
    #         # Making sure there are no empty entraces in the list
    #         if "" in rimanti_list:
    #             rimanti_list.remove("")

    #         #Making sure that the same rimanti's have the same written spelling
    #         for rimante in rimanti_list:
    #             r_i = rimanti_list.index(rimante)
    #             for list in words_replace:
    #                 if rimante in list:
    #                     rimanti_list[r_i] = list[1]

    #         pg_rimanti_list = []
    #         # First set of rhymes A (B) A
    #         rimanti = rimanti_list[0], rimanti_list[2]
    #         pg_rimanti_list.append(rimanti)  

    #         # All of the rhymes in sets of three
    #         for rimante in range (1, len(rimanti_list)-5, 3):
    #             rimanti = rimanti_list[rimante], rimanti_list[rimante+2], rimanti_list[rimante+4]
    #             pg_rimanti_list.append(rimanti)  
            
    #         # Last set of rhymes X (Y) X
    #         rimanti = rimanti_list[-3], rimanti_list[-1]
    #         pg_rimanti_list.append(rimanti) 

    #         purgatorio_rimanti_list.append(pg_rimanti_list)


    # ### PARADISO ###
    # # Directory
    # folder = 'Paradiso'

    # #Comprehensive list of all the rimanti sublists by canto
    # paradiso_rimanti_list = []

    # for filename in sorted(os.listdir(folder)):
    #     if filename.endswith('.txt'):
    #         filepath = os.path.join(folder, filename)

    #         # Opening the canti in read mode
    #         with open (filepath, 'r') as testing:
    #             canto = testing.read()

    #         # Accounting for different writing
    #         characters = canto.replace('à', 'a').replace('â', 'a').replace('è', 'e').replace('é', 'e').replace('ê', 'e').replace('ï', 'i').replace('í', 'i').replace('ì', 'i').replace('î', 'i').replace('ò', 'o').replace('ó', 'o').replace('ô', 'o').replace('ü', 'u').replace('ù', 'u').replace('ú', 'u')

    #         # Keeping only the rimante !this might not work for some rimanti!
    #         rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

    #         # Putting the rimanti in a list
    #         rimanti_list = rimanti.split("\n")
    #         # Making sure there are no empty entraces in the list
    #         if "" in rimanti_list:
    #             rimanti_list.remove("")
            
    #         #Making sure that the same rimanti's have the same written spelling
    #         for rimante in rimanti_list:
    #             r_i = rimanti_list.index(rimante)
    #             for list in words_replace:
    #                 if rimante in list:
    #                     rimanti_list[r_i] = list[1]

    #         pd_rimanti_list = []
    #         # First set of rhymes A (B) A
    #         rimanti = rimanti_list[0], rimanti_list[2]
    #         pd_rimanti_list.append(rimanti)  

    #         # All of the rhymes in sets of three
    #         for rimante in range (1, len(rimanti_list)-5, 3):
    #             rimanti = rimanti_list[rimante], rimanti_list[rimante+2], rimanti_list[rimante+4]
    #             pd_rimanti_list.append(rimanti)  
            
    #         # Last set of rhymes X (Y) X
    #         rimanti = rimanti_list[-3], rimanti_list[-1]
    #         pd_rimanti_list.append(rimanti)

    #         paradiso_rimanti_list.append(pd_rimanti_list)

    # ### ORLANDO FURIOSO ###
    # Directory
    folder = 'OF'

    #Comprehensive list of all the rimanti sublists by canto
    of_rimanti_list = []

    for filename in sorted(os.listdir(folder)):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder, filename)

            # Opening the canti in read mode
            with open (filepath, 'r') as testing:
                canto = testing.read()

            # Lowercase now because before the uppercase was used to split up the canti
            lowercase = canto.lower()

            # Accounting for different writing --> the problem with this is that the autors not only write some words differently, but within the works themselves a word can be spelled differently. How do I account for the magin of error? 
            characters = lowercase.replace('à', 'a').replace('â', 'a').replace('è', 'e').replace('é', 'e').replace('ê', 'e').replace('ï', 'i').replace('í', 'i').replace('ì', 'i').replace('î', 'i').replace('ò', 'o').replace('ó', 'o').replace('ô', 'o').replace('ü', 'u').replace('ù', 'u').replace('ú', 'u')

            # Keeping only the rimante !this might not work for some rimanti!
            rimanti = re.sub(r"(.*)(\s)(\w+)(\n)", r"\3\4", characters)

            # Putting the rimanti in a list
            rimanti_list = rimanti.split("\n")
            # Making sure there are no empty entraces in the list
            if "" in rimanti_list:
                rimanti_list.remove("")
            
            #Making sure that the same rimanti's have the same written spelling
            for rimante in rimanti_list:
                r_i = rimanti_list.index(rimante)
                for list in words_replace:
                    if rimante in list:
                        rimanti_list[r_i] = list[1]

            list = []
            # Cycling through the list of rimanti to aggregate the ones that rhyme
            for rimante in range (0, len(rimanti_list), 8):
                # First set of rhymes A (B) A (B) A
                rimanti_A = rimanti_list[rimante], rimanti_list[rimante+2], rimanti_list[rimante+4]
                list.append(rimanti_A)
                # Second set B (A) B (A) B
                rimanti_B = rimanti_list[rimante+1], rimanti_list[rimante+3], rimanti_list[rimante+5]
                list.append(rimanti_B)
                # Last set C C
                rimanti_C = rimanti_list[rimante+6], rimanti_list[rimante+7]
                list.append(rimanti_C)
            of_rimanti_list.append(list)
    
    # # Printing all rimanti in json files
    # with open ('json_files/rimanti_json/inferno_rimanti.json', 'w') as inf:
    #     json.dump(inferno_rimanti_list, inf)

    # with open ('json_files/rimanti_json/purgatorio_rimanti.json', 'w') as purg:
    #     json.dump(purgatorio_rimanti_list, purg)

    # with open ('json_files/rimanti_json/paradiso_rimanti.json', 'w') as para:
    #     json.dump(paradiso_rimanti_list, para)

    with open ('json_files/rimanti_json/orlando_rimanti.json', 'w') as orl:
        json.dump(of_rimanti_list, orl)

if __name__ == "__main__":
    main()

