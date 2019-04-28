#Written by Tsubasa Kato April 28th, 2019
#Used and modified code from: https://stackoverflow.com/questions/16801246/how-do-you-write-a-counter-to-a-file-in-order
from collections import Counter


with open('./thoughts-cypher-stingraze.txt', 'r') as inputfile:
    data = inputfile.read().split()

counted = Counter(data)


with open("./test.txt" , mode='w') as outputfile:
    for k,v in  counted.most_common():
        outputfile.write( "{} {}\n".format(k,v) )