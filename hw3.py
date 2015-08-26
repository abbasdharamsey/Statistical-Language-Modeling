# Abbas Dharamsey

import operator
import math
# from numpy import *

#list of all the words in the vocab
vocabFile = open('hw3_vocab.txt', 'r')
vocab = [x.strip('\n') for x in vocabFile.readlines()]

#list of all the counts of the unigram file
uni = []
uniTotal = 0
uniFile = open('hw3_unigram.txt', 'r')
for num in uniFile:
    uni.append(int(num))
    uniTotal += int(num)

# Answer to part 3.3(a)
print "3.3(a) Unigram Probabilities of words that start with the letter 'S'"
print "---------------------------------------------------------------------"
for i in range(len(vocab)):
    word = vocab[i]
    if word[0] == 's' or word[0] == 'S':
        print "   " + word + " "*(12-len(word)) + str((float(uni[i])/float(uniTotal)))
    # if word == "SOLD": 
    #     print "sold " + str(i)
    # if word == "INSURANCE": 
    #     print "insurance " + str(i)
    # if word == "FIRE": 
    #     print "fire " + str(i)
    # if word == "OFFICIALS": 
        # print "OFFICIALS " + str(i)
print "\n"


biFile = open('hw3_bigram.txt', 'r')
bi_main_list = []
curlist = []
curIndex = 0
partCProbs = []
partDProbs = []

for line in biFile:
    tempLine = line.split()
    firstIndex = int(tempLine[0])-1
    secondIndex = int(tempLine[1])-1
    if curIndex != firstIndex:
        bi_main_list.append(curlist)
        for i in range(firstIndex - curIndex - 1):
            bi_main_list.append([])
        curIndex = firstIndex
        curlist = [(secondIndex, float(tempLine[2])/float(uni[curIndex]))]
    else:
        curlist.append((secondIndex, float(tempLine[2])/float(uni[curIndex])))

    if vocab[firstIndex] == '<s>' and vocab[secondIndex] == 'THE':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
        partDProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'THE' and vocab[secondIndex] == 'STOCK':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'STOCK' and vocab[secondIndex] == 'MARKET':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'MARKET' and vocab[secondIndex] == 'FELL':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'FELL' and vocab[secondIndex] == 'BY':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'BY' and vocab[secondIndex] == 'ONE':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'ONE' and vocab[secondIndex] == 'HUNDRED':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'HUNDRED' and vocab[secondIndex] == 'POINTS':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'POINTS' and vocab[secondIndex] == 'LAST':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'LAST' and vocab[secondIndex] == 'WEEK':
        partCProbs.append(float(tempLine[2])/float(uni[curIndex]))

    if vocab[firstIndex] == 'THE' and vocab[secondIndex] == 'FOURTEEN':
        partDProbs.append(float(tempLine[2])/float(uni[curIndex]))
        partDProbs.append(0)
    if vocab[firstIndex] == 'FOURTEEN' and vocab[secondIndex] == 'OFFICIALS':
        partDProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'OFFICIALS' and vocab[secondIndex] == 'SOLD':
        partDProbs.append(float(tempLine[2])/float(uni[curIndex]))
        partDProbs.append(0)
    if vocab[firstIndex] == 'SOLD' and vocab[secondIndex] == 'FIRE':
        partDProbs.append(float(tempLine[2])/float(uni[curIndex]))
    if vocab[firstIndex] == 'FIRE' and vocab[secondIndex] == 'INSURANCE':
        partDProbs.append(float(tempLine[2])/float(uni[curIndex]))




# Answer to part 3.3(b)
print "3.3(b) Top 10 Bigram Probabilities of words that follow the word 'One'"
print "---------------------------------------------------------------------"
oneProb = bi_main_list[vocab.index('ONE')]
oneProb.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word = vocab[oneProb[i][0]]
    print "   " + word + " "*(12-len(word)) + str(oneProb[i][1])
print "\n"


partC = ['<s>', 'THE', 'STOCK', 'MARKET', 'FELL', 'BY', 'ONE', 'HUNDRED', 'POINTS', 'LAST', 'WEEK']

print "3.3(c) The Unigram and Bigram log likelihood"
print "--------------------------------------------"


cUSum = 0
for word in partC:
    if word == '<s>':
        continue
    cUSum += math.log(float(uni[vocab.index(word)])/uniTotal)

print "   Unigram:" + " "*(10-len(word)-1) + str(cUSum)

cBSum = 0
for prob in partCProbs:
    cBSum += math.log(prob)

print "   Bigram:" + " "*(10-len(word)) + str(cBSum) + '\n'

print "3.3(d) The Unigram and Bigram log likelihood"
print "--------------------------------------------"

dUProbs = []
dUSum = 0
par = "THE FOURTEEN OFFICIALS SOLD FIRE INSURANCE"
partD = par.split()
for word in partD:
    if word == '<s>':
        continue
    dUSum += math.log(float(uni[vocab.index(word)])/uniTotal)
    dUProbs.append(float(uni[vocab.index(word)])/uniTotal)
print "   Unigram:" + " "*(15-len(word)-1) + str(dUSum)



print "   Bigram:" + " "*(15-len(word)) + "Undefined\n"

print "3.3(e) The Lambda likelihood"
print "--------------------------------------------"

# else:
#     dBSum = 0
#     for prob in partDProbs:
#         dBSum += math.log(prob)
#     print "   Bigram:" + " "*(15-len(word)) + str(dBSum)
maxLamb = 0
lMax = -100
lambDa = 0.00
end = []
while lambDa <= 1:
    lSum = 0
    for i in range(len(dUProbs)):
        var = (dUProbs[i]*lambDa + (1-lambDa)*partDProbs[i])
        if var == 0:
            lSum += -float('inf')
            break  
        lSum += math.log(var)
    if lSum > lMax:
        lMax = lSum 
        maxLamb = lambDa
    end.append((lambDa, lSum))
    lambDa+=.01
print "   Plot points:"
print end

print "   Max Lm function:" + " "*(3) + str(lMax) 

print "   Max Lambda:" + " "*(8) + str(maxLamb)

