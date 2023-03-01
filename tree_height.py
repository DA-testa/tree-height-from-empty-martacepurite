# python3

import sys
import threading
import numpy as np


def depth_of_node(n,parents,depth):

    node=int(parents[n])
    

    depth=depth+1

    
    
    if(node!=-1):
        return depth_of_node(node,parents,depth)
        
        
    return int(depth)
    


def compute_height(n, parents):

    # Write this function
    max_height = int(0)
    hg=int(0)
    a=int(0)
    
    i=int(0)

    while(i<n):
        hg=depth_of_node(i,parents,a)
        
        if(int(hg)>int(max_height)):max_height=hg
        i+=1
    

    
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    text=input()
    text2=input()
    
    
    if(text.startswith("F")):
        filename=input()
        if(filename.startswith("a")):return
        
        file=open(filename,"r")
        n=int(file.readline())
        text=(file.readline())

        lst=text.split()

        arr=np.asarray(lst)

        h=compute_height(n,arr)

        print(h)

    else:
        n=int(text)

        

        lst=text2.split()

        arr=np.asarray(lst)

        h=compute_height(n,arr)

        print(h)

    
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
