# coding: utf-8
# from os import X_OK
import re

############################################## MAKING  XML ##############################################

############################################## STEP 1 ##############################################

with open ("Play.txt", 'r') as test:
    text = test.read()

#Deleting all new lines.
text = text.replace("\n", " ")

#Crating tables for all SPEAKER. elements.
NAMES = ["ALGERNON.", "LANE.", "JACK.", "LADY BRACKNELL.", "GWENDOLEN.", "MISS PRISM.", "CECILY.", "CHASUBLE.", "MERRIMAN.", "GWENDOLEN and CECILY.", "JACK and ALGERNON."]
#Creating tables for all speakers contained in the <speaker who="Name"> tag.
names = ["Algernon", "Lane", "Jack", "Lady Bracknell", "Gwendolen", "Miss Prism", "Cecily", "Chasuble", "Merriman", "Gwendolen and Cecily", "Jack and Algernon"]

#Adding <sp>, <speaker>, and </speaker>, <p> (and new lines) to wrap around SPEAKER. by 'replacing' them. HOWEVER: this won't add the final </p> tag to the scene
for i in range(len(NAMES)):
    text = text.replace(NAMES[i], "\n<sp>\n<speaker who='"+names[i]+"'> "+NAMES[i]+" </speaker>")

#Wrapping <stage> around all square brackets []. This doesn't distinguish between types of stages.
text = text.replace("[", "\n<stage>[") #adding the <stage> tag at the start of square brackets
text = text.replace("]", "]</stage>") #adding </stage> at the end of square brackets

#Wrapping <header> around SCENE
text = text.replace("SCENE", "\n<header>SCENE</header>\n")

#Wrapping <header> around FIRST ACT
text = text.replace("FIRST ACT", "\n<header>FIRST ACT</header>\n")
#Wrapping <header> around SECOND ACT
text = text.replace("SECOND ACT", "\n<header>SECOND ACT</header>\n")
#Wrapping <header> around THIRD ACT
text = text.replace("THIRD ACT", "\n<header>THIRD ACT</header>\n")

#WRAPPING <actDrop> around ACT DROP
text = text.replace("ACT DROP", "\n<header>ACT DROP</header>\n")

#Wrapping <header> around TABLEAU
text = text.replace("TABLEAU", "\n<header>TABLEAU</header>\n")

#replace BLA (manually added) with <stage type="setting">
text = text.replace("BLA", "<stage>")

#replace BLO (manually added)with </stage>
text = text.replace("BLO", "</stage>\n")

#Wrapping <Title> around The Importance of Being Earnest
text = text.replace("The Importance of Being Earnest", "<title>The Importance of Being Earnest</title>\n")

#Wrapping <subtitle> around A Trivial Comedy for Serious People
text = text.replace("A Trivial Comedy for Serious People", "<subtitle>A Trivial Comedy for Serious People</subtitle>")

#Adding the XML declaration, the root element, and opening the text and front elements + adding in the file.xsl ref
text = text.replace("<title>", "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>\n<?xml-stylesheet type='text/xsl' href='file.xsl'?>\n<play>\n<text>\n<front>\n<title>")

#Closing the front element and opening the body element
text = text.replace("</subtitle>", "</subtitle>\n</front>\n<body>")

#Closing the body and the text elements
text = text.replace("TABLEAU</header>", "TABLEAU</header>\n</body>\n</text>\n</play>")


#Closing the <sp> element
text = text.replace("<sp>","</sp>\n<sp>")



with open("play_v2.xml", "w") as testing:
    testing.write(text)

############################################## STEP 2 ##############################################

with open("play_v2.xml", "r") as testingp:
    prettyp = testingp.read()
#Trying to put the <p> in using regex
x_new = re.sub(r"(</speaker>)(.*)\s{0,}\n", r"\1\n<p>\2</p>\n", prettyp)


with open ("play_v3.xml", "w") as alltheps:
    alltheps.write(x_new)

############################################## STEP 3 ##############################################

with open("play_v3.xml", "r") as testingp:
    prettyp = testingp.read()

#Fixing some <p> issues
x_newS = re.sub(r"(</stage>)(.*)\s{0,}\n", r"\1\n<p>\2</p>\n", prettyp)

with open ("play_v4.xml", "w") as alltheps:
    alltheps.write(x_newS)

############################################## STEP 4 ##############################################    

with open ("play_v4.xml", 'r') as help:
    text = help.read()

#More <p> issues
wannaCry = re.sub(r"<p>\s{0,}</p>\n", r'', text)

with open ("play_v5.xml", 'w') as help:
    help = help.write(wannaCry)

#team F for Frenever give up

############################################## STEP 5 ############################################## 


with open ("play_v5.xml", 'r') as helpMore:
    text = helpMore.read()

#Changing the <stage> name to <stage_setting> for subsequent tree clarity
#For the first stage setting
text = text.replace("<stage> Morning-room in Algernon’s flat in Half-Moon Street. The room is luxuriously and artistically furnished. The sound of a piano is heard in the adjoining room. </stage>", "<stageSetting> Morning-room in Algernon’s flat in Half-Moon Street. The room is luxuriously and artistically furnished. The sound of a piano is heard in the adjoining room. </stageSetting>")
#For the second stage setting
text = text.replace("<stage> Garden at the Manor House. A flight of grey stone steps leads up to the house. The garden, an old-fashioned one, full of roses. Time of year, July. Basket chairs, and a table covered with books, are set under a large yew-tree. </stage>", "<stageSetting> Garden at the Manor House. A flight of grey stone steps leads up to the house. The garden, an old-fashioned one, full of roses. Time of year, July. Basket chairs, and a table covered with books, are set under a large yew-tree. </stageSetting>")
#For the third stage setting
text = text.replace("<stage> Morning-room at the Manor House. </stage>", "<stageSetting> Morning-room at the Manor House. </stage_setting>")

#Fixing the first <sp> order issue to fit the <stage> into it
text = text.replace("<stage>[Lane is arranging afternoon tea on the table, and after the music has ceased, Algernon enters.]</stage>\n</sp>\n<sp>\n<speaker who='Algernon'> ALGERNON. </speaker>", "<sp>\n<stage>[Lane is arranging afternoon tea on the table, and after the music has ceased, Algernon enters.]</stage>\n<speaker who='Algernon'> ALGERNON. </speaker>")

#Fixing the second <sp> order issue to fit the <stage> into it
text = text.replace("<stage>[Miss Prism discovered seated at the table. Cecily is at the back watering flowers.]</stage>\n</sp>\n<sp>\n<speaker who='Miss Prism'> MISS PRISM. </speaker>", "<sp>\n<stage>[Miss Prism discovered seated at the table. Cecily is at the back watering flowers.]</stage>\n<speaker who='Miss Prism'> MISS PRISM. </speaker>")

#Fixing the third <sp> order issue to fit the <stage> into it
text = text.replace("<stage>[Gwendolen and Cecily are at the window, looking out into the garden.]</stage>\n</sp>\n<sp>\n<speaker who='Gwendolen'> GWENDOLEN. </speaker>", "<sp>\n<stage>[Gwendolen and Cecily are at the window, looking out into the garden.]</stage>\n<speaker who='Gwendolen'> GWENDOLEN. </speaker>")

#Getting rid of stray </sp>
text = text.replace("looking out into the garden.]</stage>\n</sp>", "looking out into the garden.]</stage>")

#Opening a missing <sp> tag
text = text.replace("-cuff, and smiles.]</stage>", "-cuff, and smiles.]</stage>\n</sp>")

#Properly closing <sp> tags
text = text.replace("vital Importance of Being Earnest.  </p>", "vital Importance of Being Earnest.  </p>\n</sp>")
text = text.replace("ontinues eating.]</stage>", "ontinues eating.]</stage>\n</sp>")

#fixing an inexplicable punctuation error
text = text.replace("_._", ".")


with open ("the_one.xml", 'w') as help:
    help = help.write(text)



############################################## XSL ############################################## 