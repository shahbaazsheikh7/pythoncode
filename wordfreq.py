# Program to compute most used words in a text file
import string
import matplotlib.pyplot as plt

fname = input("Enter the filname: ")

try:
    fhand = open(fname)
except:
    print("Invalid filename")
    exit()

wordcount = {}
cnt = 0

for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.strip()
    line = line.lower()
    words = line.split()
    if len(words)==0:
        continue
    for word in words:
        wordcount[word] = wordcount.get(word,0) + 1
        cnt = cnt + 1
        #print(count)

wordlist = []
#print(type(wordcount.items()))
for word,count in wordcount.items():
    wordlist.append((count,word))   #wordlist is list of tuples-- (count,word)
#print(type(wordlist[0])) 
wordlist.sort(reverse=True)

print(fname,"contains",cnt,"words")
print("The 10 most used words in %s are: "%fname)

count_list = []
word_list = []

for count,word in wordlist[:10]:
    print(word,count)
    word_list.append(word)
    count_list.append(count)

plt.xlabel("Words",color="Green")
plt.ylabel("Number of Occurences",color="Green")
plt.title("Top 10 most used words in '%s'"%fname,color="Green")
#plt.legend("'%s' has %d words"%(fname,cnt))
plt.bar(word_list,count_list)
plt.show()
