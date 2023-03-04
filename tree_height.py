# python3

import sys
import threading
import numpy as np


def depth_of_node(n,parents,deptharr):

    if(parents[n]==-1):return 1

    if(deptharr[n]!=0):return deptharr[n]

    deptharr[n]=depth_of_node(parents[n],parents,deptharr)+1

    return deptharr[n]
    


def compute_height(n, parents):

    max_height = int(0)
    
    i=int(0)

    dparr=np.zeros(n,dtype=int)

    while(i<n):
        dparr[i]=depth_of_node(i,parents,dparr) 
         
        i+=1
    
    max_height=np.amax(dparr)

    return max_height


def main():
    text=input()
    text2=input()
    
    if(text.startswith("F")):
        filename="test/"+text2
        if(filename.endswith("a")):return

        file=open(filename,"r")
        n=int(file.readline())
        text=(file.readline())

        lst=text.split()

        arr=np.asarray(lst,dtype=int)

        h=compute_height(n,arr)

        print(h)

    elif(text.startswith("I")):
        n=int(text2)

        text3=input()

        lst=text3.split()

        arr=np.asarray(lst,dtype=int)

        h=compute_height(n,arr)

        print(h)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27) 
threading.Thread(target=main).start()