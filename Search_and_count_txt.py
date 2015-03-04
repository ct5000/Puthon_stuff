import re, operator

testfile = open("c:/Python27/Eksamensprojekt/Test.txt", "r")
testtext = testfile.read()
testtext = testtext.lower()
words = re.split(r'[ ^|^,|^.]+', testtext)
wordcount = {}
for w in words:
    if not (w in wordcount.keys()):
        wordcount[w] = 1
    else:
        wordcount[w] += 1
sorted_wordcount = sorted(wordcount.items(), key = operator.itemgetter(1))
sorted_wordcount.reverse()
print ("The most used word is: " + sorted_wordcount[0][0] + " and it is used: "
       + str(sorted_wordcount[0][1])) + " times"
print ("The next most used word is: " + sorted_wordcount[1][0] + " and it is used: "
       + str(sorted_wordcount[1][1])) + " times"
print ("The third most used word is: " + sorted_wordcount[2][0] + " and it is used: "
       + str(sorted_wordcount[2][1])) + " times"
testfile.close()
