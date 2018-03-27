#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 16:34
# @Author  : Aries
# @Site    : 
# @File    : homework3_1.py
# @Software: PyCharm Community Edition
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : XXXXXX@gmail.com
# @Site    :
from svmutil import *
import csv
def fun1(filename,newfile):#reader
    with open(newfile, 'w') as newf:
        with open(filename,'r') as f:
            csvReader = csv.reader(f)
            next(csvReader)
            for row in csvReader:
                if(row[-1]=='1'):
                    newf.write("+1")
                else:
                    newf.write("-1")
                for i in range(1,4):
                    newf.writelines(" "+str(i)+":"+row[i])
                newf.write('\n')

if __name__ == '__main__':
    fun1('data3.csv','newdata3.txt')
    y, x = svm_read_problem('newdata3.txt')
    m = svm_train(y[:20], x[:20], '-c 4')
    p_label, p_pacc, p_val = svm_predict(y[20:], x[20:], m)
    #y,x=svm_read_problem('data3.csv')