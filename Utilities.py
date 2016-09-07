"""
Author: CHANDRAMOHAN T N
File: Utilities.py 
"""

import re

# Calculates accuracy of the model
def Accuracy_model(p_tags, o_tags):
    acc = 0.0
    for i in range(len(p_tags)):
        i_acc = 0
        for j in range(len(p_tags[i])):
            if p_tags[i][j] == o_tags[i][j]:
                i_acc += 1
        acc += (i_acc * 1.0 / len(p_tags[i]))
    print('Accuracy of model: ' + str(acc))

# Calculates accuracy of the item
def Accuracy_item(p_tags, o_tags):
    acc = 0
    for i in range(len(p_tags)):
        if p_tags[i] == o_tags[i]:
            acc += 1
    print('Total: ' + str(len(p_tags)))
    print('Correct: ' + str(acc))
    acc = acc * 1.0 / len(p_tags)
    #print('Accuracy: ' + str(acc))

# Reads data and tags from the input file
def Get_data(i_file):
    fp = open(i_file, 'r')
    data = []
    tags = []
    while 1:
        line = fp.readline()
        if not line:
            fp.close()
            break
        else:
            line = line[0:len(line) - 1]
            items = line.split()
            w = []
            t = []
            for i in items:
                item = i.split('/')
                w.append(item[0])
                t.append(item[1])
            data.append(w)
            tags.append(t)
    print('Data parsed ......')
    return data, tags

# Encodes the data and tags
def Convert_data(data, tags, d_vocab, t_vocab):
    d = []
    t = []
    for i in data:
        item = []
        for j in i:
            item.append(d_vocab[j])
        d.append(item)
    for i in tags:
        item = []
        for j in i:
            if '-' in j:
                items = j.split('-')
                for k in items:
                    if (len(k) > 1) and (k != 'hl') and (k != 'tl') and (k != 'nc') and (k != 'fw'):
                        item.append(t_vocab[k])
            else:
                if len(j) > 1:
                    item.append(t_vocab[j])
        t.append(item)
    print('Data converted ........')
    return d, t

# Creates vocabulary for data and tags
def Get_vocabulary(data, tags):
    d_vocab = {}
    t_vocab = {}
    count = 0
    f = open('C:\Users\Chandramohan\Desktop\@IIT\POS Tagger\Data\Tags.txt', 'w')
    for i in data:
        for j in i:
            if j not in d_vocab:
                d_vocab[j] = count
                count += 1
    count = 0
    for i in tags:
        for j in i:
            if '-' in j:
                items = j.split('-')
                for k in items:
                    if (len(k) > 1) and (k != 'hl') and (k != 'tl') and (k != 'nc') and (k != 'fw'):
                        if k not in t_vocab:
                            t_vocab[k] = count
                            count += 1
                            f.write(k + '\n')
            else:
                if len(j) > 1:
                    if j not in t_vocab:
                        t_vocab[j] = count
                        count += 1
                        f.write(j + '\n')
    print('Vocabulary generated ........')
    f.close()
    return d_vocab, t_vocab
            
