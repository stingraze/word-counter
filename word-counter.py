#Script from:https://codereview.stackexchange.com/questions/103773/count-the-frequency-of-words-in-a-text-file
#Modified by Tsubasa Kato on April 26th, 2019 for personal use.
from collections import Counter
#change the file name to your needs.
with open("./thoughts-cypher-stingraze.txt") as f:
	wordcount = Counter(f.read().split())

#To print sorted wordcount:
#print (sorted(wordcount))

path = "./wordcount.txt"
#Open path and write to file
with open(path, mode='w') as f:
    f.write('\n'.join(wordcount))

#open file and  print each line
with open(path) as f:
    print(f.read())