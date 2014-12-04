#! /usr/bin/env python
# -*- coding=utf8 -*-

'''
处理快递单号
'''

def readCSV1(filename):
    f = open(filename, 'r')
    deliver_nos = []
    deliver_info = {}
    for line in f.read().split('\n')[:-1]:
        items = line.split(',')
        #print items[7],"宅急送"
        if items[7] == '宅急送':
            #print items[7]
            deliver_nos.append(items[1])
            deliver_info[items[1]] = items[2]
    return deliver_nos[1:],deliver_info
    
def readCSV2(filename):
    f = open(filename, 'r')
    deliver_nos = []
    deliver_info = {}
    for line in f.read().split('\n')[:-1]:
        #import pdb; pdb.set_trace()
        items = line.split(',')
        deliver_nos.append(items[0])
        deliver_info[items[0]] = items[15]
        #pdb.set_trace()
    return deliver_nos[1:],deliver_info
    
def deliverHandler(list1, list2):
    answer1, answer2 = [],[]
    for item in list1:
        if item not in list2:
            answer1.append(item)
    for item in list2:
        if item not in list1:
            answer2.append(item)
    return answer1,answer2
    
def deliver_fee_compare(dict1,dict2):
    f = open('compare_fee.txt','w')
    for key in dict1.keys():
        try:
            if float(dict1[key]) - float(dict2[key]) > 1.0:
                f.write(key + ',' + dict1[key] + ',' + dict2[key] + '\n')
        except(KeyError):
            f.write('wrong number:' + key + '\n')
    f.close()
    
def testReadCSV():
    filename = 'in.csv'
    deliver_nos = readCSV(filename)
    print len(deliver_nos)
    print deliver_nos[:10],deliver_nos[-10:]
    
if __name__ == '__main__':
    list1,dict1 = readCSV1('in.csv')
    list2,dict2 = readCSV2('out.csv')
    answer1, answer2 = deliverHandler(list1,list2)
    f = open('in.txt','w')
    for item in answer1:
        f.write(item + '\n')
    f.close()
    f = open('out.txt','w')
    for item in answer2:
        f.write(item + '\n')
    f.close()
    deliver_fee_compare(dict1,dict2)
    
