import re

def main():
    # ## 1. Inferno
    # # Open file
    # with open ("/Users/tessacattaneo/Desktop/tesi_master/If.txt", "r") as If:
    #     Inferno = If.read()

    # # Split main file into each canto
    # canti = re.split('canto\s[ivx]+\n', Inferno)

    # # Creating a file for each individual canto
    # for item in canti:
    #     index = str((canti.index(item)))
    #     filepath = '/Users/tessacattaneo/Desktop/tesi_master/Inferno/If_'+index+'.txt'
    #     if len(item) != 0:
    #         with open (filepath, 'w') as a:
    #             a.write(item)

    # ## 2. Purgatorio
    # # Open file
    # with open ("/Users/tessacattaneo/Desktop/tesi_master/Pd.txt", "r") as Pg:
    #     Purgatorio = Pg.read()

    # # Split main file into each canto
    # canti = re.split('canto\s[ivx]+\n', Purgatorio)

    # # Creating a file for each individual canto
    # for item in canti:
    #     index = str((canti.index(item)))
    #     filepath = '/Users/tessacattaneo/Desktop/tesi_master/Purgatorio/Pg_'+index+'.txt'
    #     if len(item) != 0:
    #         with open (filepath, 'w') as a:
    #             a.write(item)
    
    # ## 3. Paradiso
    # # Open file
    # with open ("/Users/tessacattaneo/Desktop/tesi_master/Pd.txt", "r") as Pd:
    #     Paradiso = Pd.read()

    # # Split main file into each canto
    # canti = re.split('canto\s[ivx]+\n', Paradiso)

    # # Creating a file for each individual canto
    # for item in canti:
    #     index = str((canti.index(item)))
    #     filepath = '/Users/tessacattaneo/Desktop/tesi_master/Paradiso/Pd_'+index+'.txt'
    #     if len(item) != 0:
    #         with open (filepath, 'w') as a:
    #             a.write(item)

    ## 4. Orlando Furioso
    with open ("/Users/tessacattaneo/Desktop/tesi_master/orlando_furioso.txt", "r") as OF:
        Orlando_furioso = OF.read()

    # Split main file into each canto
    canti = re.split('[A-Z]{2,}\s[A-Z]{2,}\n', Orlando_furioso)

    # Creating a file for each individual canto
    for item in canti:
        index = str((canti.index(item)))
        filepath = '/Users/tessacattaneo/Desktop/tesi_master/OF/Of_'+index+'.txt'
        if len(item) != 0:
            with open (filepath, 'w') as a:
                a.write(item)

if __name__ == "__main__":
    main()