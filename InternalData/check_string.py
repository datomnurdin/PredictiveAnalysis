#!/usr/bin/python

import os,sys
from scipy import stats
import numpy as np

f=open('data/Customer-country_data_5-5.csv', 'r').readlines()
N=len(f)-1
for i in range(0,N):
    w=f[i].split()
    l1=w[1:8]
    l2=w[8:15]
    try:
        list1=[float(x) for x in l1]
        list2=[float(x) for x in l2]
    except ValueError,e:
        print "error",e,"on line",i
    result=stats.ttest_ind(list1,list2)
    print result[1]