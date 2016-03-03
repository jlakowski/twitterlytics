import numpy as np
import sqlite3
import matplotlib.pyplot as plt
#connect to the tweets database
conn = sqlite3.connect("/home/jim/code/java/twitter016/tweets.sqlite")
c = conn.cursor()

c.execute("select * from tbl1")

trumpscores = np.array([])
cruzscores = np.array([])
hilscores = np.array([])
rubus = np.array([])
bernscores = np.array([])
#could use an object here
#gonna use parrllel arrays instead

indtoc = {0:'trump', 1:'cruz', 2:'hillary', 3:'rubus', 4:'bernie'}

for i in c.fetchall():
    text = i[0]
    num = i[1]
    
    text = text.lower()
    if("trump" in text or "donald" in text):
        trumpscores= np.append(trumpscores, num)
    if('ted' in text or 'cruz' in text):
        cruzscores = np.append(cruzscores, num)
    if('hillary' in text or 'clinton' in text):
        hilscores = np.append(hilscores, num)
    if('marco' in text or 'rubio' in text):
        rubus = np.append(rubus, num)
    if('bernie' in text or 'sanders' in text):
        bernscores = np.append(bernscores, num)

scoresvec = [trumpscores, cruzscores, hilscores, rubus, bernscores]
meanvec = np.array([])
stdvec = np.array([])
numvec = np.array([])
count = 0
plt.close("all")
print('person\tmean\t\tstd\t\tnumtweets')
for i in scoresvec:
    meanvec = np.append(meanvec, i.mean())
    stdvec = np.append(stdvec, i.std())
    numvec = np.append(numvec, len(i))
    nbins = i.max()-i.min()
    plt.figure(indtoc[count])
    plt.hist(i, nbins, log=True)
    plt.xlabel('Tweet Emotional Score')
    plt.ylabel('Number of occurrences')
    plt.title(indtoc[count])
    print "%s\t%f\t%f\t%d" %(indtoc[count], i.std(), i.mean(), len(i))
    count +=1
