# python3

import sys
import threading
import numpy as np


def compute_height(n,parents,depth):

    node=int(parents[n])
    

    depth=depth+1

    
    
    if(node!=-1):
        return compute_height(node,parents,depth)
        
        
    return int(depth)
    





def main():
    # implement input form keyboard and from files
    text=input()
    text2=input()
    
    
    
    if(text.startswith("F")):
        filename="test/"+text2
        if(filename.endswith("a")):return

        file=open(filename,"r")
        n=int(file.readline())
        text=(file.readline())

        lst=text.split()

        arr=np.asarray(lst)

        max_height = int(0)
        hg=int(0)
        a=int(0)
    
        i=int(0)

        while(i<n):
            hg=compute_height(i,arr,a)
        
            if(int(hg)>int(max_height)):max_height=hg
            i+=1

        print(max_height)

    elif(text.startswith("I")):
        n=int(text2)

        text3=input()

        lst=text3.split()

        arr=np.asarray(lst)

        max_height = int(0)
        hg=int(0)
        a=int(0)
    
        i=int(0)

        while(i<n):
            hg=compute_height(i,arr,a)
        
            if(int(hg)>int(max_height)):max_height=hg
            i+=1

        print(max_height)

    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
