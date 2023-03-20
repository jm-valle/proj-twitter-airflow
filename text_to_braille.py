from pybraille import convertText, convertFile
import pandas as pd

braille = convertFile("test.txt") #The convertFile function breaks when there is a double quote, fix it


f = open("19-2000.txt", 'w')
f.write(braille)
f.close()

data = pd.read_csv("gorillaz_lyrics.csv") # READ THE CSV ,GET THE LYRICS, REMOVE DOUBLE QUOTES, CONVERT TO BRAILLE


