import sqlite3
import matplotlib as plt
#connect to the tweets database
conn = sqlite3.connect("/home/jim/code/java/twitter016/tweets.sqlite")
c = conn.cursor()

c.execute("select * from tbl1")


#create a dictionary to count how often words are used
wordlist= {}

#shit this is actually really fast
#see if I can make a statistical algorithm whihc
#identifies popular keywords so a second pass to extract
#sentiment data is not needed
    

for i in c.fetchall():
    #parse out the things
    text = i[0]
    num = i[1]
    
    #convert to all lowercase for easier processing
    text = text.lower()
    words = text.split()
    
    for w in words:
        if(w in wordlist):
            wordlist[w] += 1
        else:
            wordlist[w] = 1
    #print(text)
#http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

wordsort = sorted(wordlist,key=wordlist.__getitem__, reverse=True)
wordoccurrences = sorted(wordlist.values(), reverse=True)
#plt.loglog(wordoccurences) #this is cool

top3hunna = wordsort[0:499]
print "rank\t#\tword"

for i in range(len(top3hunna)):
    try:
        print "%d\t%d\t%s" %(i,wordlist[top3hunna[i]], top3hunna[i])
    except UnicodeEncodeError:
        pass

#check to see the net favoriability ratings of certain strings

