from peremen_1 import *
arr=[]
a=0
def sbor():
    i=0
    obj={}
    while i<len(shablon):
        obj[shablon[i]]=d[peremen_name[i]][a]
        i+=1
    return obj
while a<len(name):
    arr.append(sbor())
    a+=1