import re
import os

def main():

    # Script B: the cleaned-up files are split by canto

    # Dante's Divina Commedia
    # Directory where the .txt files are contained
    folder = 'cleaned_up_files'

    # Cycling through each Commedia file
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        with open (filepath, "r") as text:
            text_to_split = text.read()
                
        # The canti of the Commedia are split by finding their start (canto+roman number+new line)
        if filename != 'orlando_furioso.txt':
            canti = re.split('canto\s[ivx]+\n', text_to_split)
            cantica = filename[:-4]

            # The canti are indexed for the purpose of clarity
            for item in canti:
                index = str((canti.index(item)))
                if index == '1' or index == '2' or index == '3' or index == '4' or index == '5' or index == '6' or index == '7' or index == '8' or index == '9':
                    filepath = cantica+'/0'+index+'_'+filename
                else:
                    filepath = cantica+'/'+index+'_'+filename
                if len(item) != 0:
                    with open (filepath, 'w') as a:
                        a.write(item)

        # Orlando Furioso
        if filename == 'orlando_furioso.txt':
            canti = re.split('CANTO\s.*\n', text_to_split)

            # Creating a file for each individual canto
            for item in canti:
                index = str((canti.index(item)))
                if index == '1' or index == '2' or index == '3' or index == '4' or index == '5' or index == '6' or index == '7' or index == '8' or index == '9':
                    filepath = 'OF/0'+index+'_Of.txt'
                else:
                    filepath = 'OF/'+index+'_Of.txt'
                if len(item) != 0:
                    with open (filepath, 'w') as a:
                        a.write(item)



if __name__ == "__main__":
    main()