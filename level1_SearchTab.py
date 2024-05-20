#coding: utf-8

#import

#Matsuda turn start
while True:
    FileName = input("Please input the file name to check (only .txt file!): ")
    if FileName.endswith('.txt'):
        print("The text file is " + '"' + FileName + '"')
        break
    else:
        print("Invalid file extension. Please input a .txt file.")
#Matsuda turn end

SearchingWord = input("Please input the searching word: ")
print("The searching word is " + '"' + SearchingWord + '"')

FilePath = '/Network/Servers/stdfsv1/vol/vol7/home3/s1300079/AAuP/' + FileName
print(FilePath)

f = open(FilePath)

sf =fr.split()

rsf = []

for word in sf:
    rsf.append(word.replace(',', ''))

for i in range(len(rsf) - 1):
    rsf[i] = rsf[i].replace('.', '')

print(rsf)

fr = f.read()

if fr.find(SearchingWord) != -1:
    print("Found " + '"' + SearchingWord + '"' + " !")
else:
    print("Not found " + '"' + SearchingWord + '"' + " !")

