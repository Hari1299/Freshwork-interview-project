import threading
from threading import*
import time
dict={}

def create(k,v,t=0):
    if k in dict:
        print("already exists")
    else:
        if(k.isalpha()):
            if len(dict)<(1024*1020*1024) and v<=(16*1024*1024):
                if t==0:
                    j=[v,t]
                else:
                    j=[v,time.time()+t]
                if len(k)<=32:
                    dict[k]=j
            else:
                print("limit exceeded")
        else:
            print("Invalid key")
def read(k):
    if k not in dict:
        print("does not exist")
    else:
        a=dict[k]
        if a[1]!=0:
            if time.time()<a[1]:
                string=str(k)+":"+str(a[0])
                return string
            else:
                print("key has expired")
        else:	
            string=str(k)+":"+str(a[0])
            return string
def delete(k):
    if k not in dict:
        print("does not exist")
    else:
        a=dict[k]
        if a[1]!=0:
            if time.time()<a[1]:
                del dict[k]
                print("key is deleted")
            else:
                print("key has expired")
        else:
            del dict[k]
            print("key is deleted")
