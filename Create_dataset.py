"""
Author: CHANDRAMOHAN T N
File: Create_dataset.py 
"""

import os

folder = "C:\Users\Chandramohan\Desktop\@IIT\POS Tagger\Data"
train = folder + '\Test.txt'
g = open(train, 'w')

files = os.listdir(folder + '\Test')
for f in files:
    fp = open(folder + '\Test\\' + f, 'r')
    while 1:
        line = fp.readline()
        if not line:
            fp.close()
            break
        else:
            if len(line) > 1:
                item = []
                line = line.strip()
                items = line.split()
                for i in items:
                    if i[0].isalpha() == True:
                        item.append(i)
                l = len(item)
                if l > 0:
                    for i in range(l):
                        g.write(item[i])
                        if l != i:
                            g.write(' ')
                    g.write('\n')
    print('Read ' + str(f))
g.close()
print('Dataset created .....')
