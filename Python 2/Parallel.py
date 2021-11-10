import os
import time
import multiprocessing

def square(num):
    return num**2
    
    
# serail processing
def serailprocessing(number):
    start = time.time()
    slist = []
    for i in range(1,number+1):
        slist.append(square(i))
    end = time.time()
    print("List of serial processing:",slist)
    print("Time taken for serail processing:",end-start)
   
# parallel processing
def parallelprocessing(number):
    start = time.time()
    pobj = multiprocessing.Pool()
    result = pobj.map(square,range(1,number+1))
    end = time.time()
    print("List of parallel processing:",result)
    print("Time taken for Parallel processing:",end-start)
    
def main():
    number = int(input("Enter a number"))
    
    serailprocessing(number)
    parallelprocessing(number)
    
if __name__ == "__main__":
    main()