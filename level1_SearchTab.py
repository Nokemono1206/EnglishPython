#coding: utf-8

#import

try:
    FileName = input("Please input the file name to check (only .txt file!): ")
    print("The text file is " + '"' + FileName + '"')
except KeyboardInterrupt:
    print("\nCtrl+C detected. Program terminated.")

SearchingWord = input("Please input the searching word: ")
print("The searching word is " + '"' + SearchingWord + '"')

FilePath = '/Network/Servers/stdfsv1/vol/vol7/home3/s1300079/AAuP/' + FileName
print(FilePath)

f = open(FilePath)

fr = f.read()

if fr.find(SearchingWord) != -1:
    print("Found " + '"' + SearchingWord + '"' + " !")
else:
    print("Not found " + '"' + SearchingWord + '"' + " !")

