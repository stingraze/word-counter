#Script from:https://codereview.stackexchange.com/questions/103773/count-the-frequency-of-words-in-a-text-file
#Modified by Tsubasa Kato on April 26th, 2019 for personal use.
import string
from collections import Counter
path1 = "spider_1.dat"
#change the file name to your needs.
with open(path1) as f:
	wordcount_split = Counter(f.read().split())
	wordcount_split2 = f.read().split()


to_sort = Counter(''.join(wordcount_split2))

with open("./kv.txt") as f:
    for k,v in  to_sort.most_common():
        f.write( "{} {}\n".format(k,v) )

print (wordcount_split)

myDict = wordcount_split

#myList = [k for k, v in myDict.items() if v > 1]

#print key and value
for k, v in myDict.items():
		print k, '\t', v
#To print sorted wordcount:
#print (sorted(wordcount_split))


#no_punc_wordcount = wordcount.translate(None, string.punctuation)

path = "./wordcount.txt"
#Open path and write to file
with open(path, mode='w') as f:
    f.write('\n'.join(wordcount_split))

#open file and  print each line
#with open(path) as f:
#   print(f.read())