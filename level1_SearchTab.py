# coding: utf-8

import datetime
import sys

now = datetime.datetime.now()

print("Please input the file name to check(only .txt file!).")
print("If you retry input the file name, please push Ctrl+c")

while True:
    try:
        FileName = input("Input File: ")
        if FileName.endswith('.txt'):
            print("The text file is " + '"' + FileName + '"' +
                  ", this file exist.")
            # search FilePath(it is different on the computer, so, please change it!)
            FilePath = '/home/student/s1300079/AAuP/' + FileName
            # get Filename except .txt
            PreFileName = FileName.replace('.txt', '')
            f = open(FilePath)
            break
        else:
            print("Please retry(maybe, only .txt can received, so please careful).")
            continue
    except KeyboardInterrupt:
        print("\nCtrl+c is detected. Finish, bye!")
        sys.exit()
    except FileNotFoundError:
        print("Not exist the File! Please retry.")
        continue

fr = f.read()

sf =fr.split()

rsf = []

# except , of words
for word in sf:
    rsf.append(word.replace(',', ''))

# except . of words
for i in range(len(rsf)):
    rsf[i] = rsf[i].replace('.', '')

TotalWords = i

# input to search words
SearchingWord = input("Please input the searching word: ")
print("The searching word is " + '"' + SearchingWord + '"')

# if SearchingWord is not exist in the txt file, print 'Not Found', and terminate program
if fr.find(SearchingWord) == -1:
    print("Not found " + '"' + SearchingWord + '"' + " !")
    sys.exit()

# opening file
fout = open('/home/student/s1300079/AAuP/' + PreFileName + '_'
            + SearchingWord + '_' + str(now.year) + '-' + str(now.month)
            + '-' + str(now.day) + '_' + str(now.hour) + '.' + str(now.minute)
            + '.' + str(now.second) + '.txt', 'w') # Filename with now time

k = 0
flag = 0

for i in range(len(rsf) - 1):
    if rsf[i] == SearchingWord: # if SearchingWord is exist
        k += 1 # k++
        if flag == 0: # print under statement 1 time
            print("Found " + '"' + SearchingWord + '"' + " !")
            print("Print 5 words before and after on Red. Searching Words is Blue.")
            flag = 1 # not print above statement more

        WordsNum = i

        for j in range(-5, 6): # print 5 words before and after
            s = WordsNum + j
            # first, write to new .txt file
            if s < 0:
                continue
            if s >= len(rsf):
                break
            if s == WordsNum:
                fout.write(' *{[' + rsf[s] + ']}* ' + ' ')
            elif (s == (WordsNum + 5)) or (s == len(rsf) - 1):
                fout.write(rsf[s] + '\n')
            elif (s == 0) or (s == WordsNum - 5):
                fout.write(str(k) + '. ' + rsf[s] + ' ')
            else:
                fout.write(rsf[s] + ' ')

            # next, print in the terminal(Changing colour!)
            if s == WordsNum:
                print('\033[1m' + '\033[4m' + '\033[34m' + rsf[s] + '\033[0m', end = ', ')
            elif (s == (WordsNum + 5)) or (s == len(rsf) - 1):
                print('\033[31m' + rsf[s] + '\033[0m')
            elif (s == 0) or (s == WordsNum - 5):
                print(str(k) + '. ' + '\033[31m' + rsf[s] + '\033[0m', end = ', ')
            else:
                print('\033[31m' + rsf[s] + '\033[0m', end = ', ')

Preratio = k/TotalWords
Rratio = round(Preratio, 3)
ratio = round(Rratio * 100, 3)
print("The ratio of " + '"' + SearchingWord + '"' +
      " = " + str(ratio) + "%")
