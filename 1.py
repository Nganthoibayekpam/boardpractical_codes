#Write the definition of a method countnow(places) to find and display those place names, in which
#there are more than 7 characters.
#For example: If the list places contains. ["MELBOURNE", "TOKYO", "PINKCITY", "BEIJING", "SUNCITY]
#The following should get displayed :MELBOURNE PINKCITY

def countnow(places):
    for x in places:
        if len(x)>7:
            print (x)
places = ["Melborn", "Tokyo", "Pinkcity", "Beijing", "Suncity"]
countnow(places)