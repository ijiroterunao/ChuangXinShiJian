#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 21:41
# @Author  : Aries
# @Site    : 
# @File    : homework1_2.py
# @Software: PyCharm Community Edition
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : XXXXXX@gmail.com
# @Site    :
import csv
import codecs
import numpy as np
import pandas as pd
import os


# 写入"newData.txt"
def fun1(filename, newfile):
    circle = 0
    with open(newfile, 'w') as newf:
        with open(filename, 'r') as f:
            items = f.read().split()
            for item in items:
                newf.write(item + '\t')
                circle = circle + 1
                if circle % 20 == 0:
                    newf.write('\n')  # print(values,sep,end,file)


def func1(dest_file):
    F = codecs.open(dest_file, 'r', 'gbk')
    content = F.read()
    F.close()
    print(content)


def func2(dest_file):
    dest_Data = pd.read_csv(dest_file,'gbk')
    print(dest_Data)  # 输出数据
    data = dest_Data.iloc[0:892, 0:12]  # 读取所有数据
    print("------------------out")
    print(data)
    # pandas数据格式为DataFrame,转化为numpy数组格式，方便处理
    print(data.as_matrix(columns=None))
    print(data.shape)

if __name__ == '__main__':
    dest_file='510050sh.csv'
    #func1(dest_file)
    func2(dest_file)