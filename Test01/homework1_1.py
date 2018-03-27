#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 10:11
# @Author  : Aries
# @Site    : 
# @File    : homework1_1.py
# @Software: PyCharm Community Edition
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : XXXXXX@gmail.com
# @Site    :
from numpy import *
from urllib.request import urlopen
import csv
from io import StringIO
#写入大文件和内存占用基本无关
# 20个数据每行写入到"newData.txt"
def format1(filename,newfile):
    circle = 0
    with open(newfile,'w') as newf:
        with open(filename, 'r') as f:
            items= f.read().split()#读取整个文件，占用内存，本次测试大约280M内存
            for item in items:
                newf.write(item+'\t')
                circle = circle + 1
                if circle % 20 == 0:
                    newf.write('\n')# print(values,sep,end,file)

# 一行一行读，减少内存占用
# with open('filename') as file:
#     for line in file:
#         do_things(line)

def format2(filename,newfile):
    circle = 0
    with open(newfile,'w') as newf:
        with open(filename, 'r') as f:
            circle=0
            for line in f:#一行一行读，减少内存占用，本次测试约17M内存
                items=line.split()
                for item in items:
                    newf.write(item + '\t')
                    circle = circle + 1
                    if circle % 20 == 0:
                        newf.write('\n')  # print(values,sep,end,file)


def readcsv1(filename):#reader
    with open(filename,'r') as f:
        csvReader = csv.reader(f)
        cnt=0
        for row in csvReader:
            if cnt==100:
                break
            cnt += 1
            print(row)


def readcsv2(filename):#Dictreader
    with open(filename,'r') as f:
        dictReader = csv.DictReader(f)
        print(dictReader.fieldnames)#打印列名
        # cnt=0
        for row in dictReader:
            # if cnt==10:
            #     break
            # cnt += 1
            print(row)



if __name__ == '__main__':
    #format2('newData.txt','newData1.txt')
    readcsv1('510050sh.csv')
