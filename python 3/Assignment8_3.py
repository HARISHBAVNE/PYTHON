#Q3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.
import threading

def Factor(fun,list,lock):
    fun(list,lock)

def Evenlist(list,lock):
    lock.acquire()
    print()
    Add = 0
    for i in (list):
        if ((i%2) == 0):
           Add = Add+i 
    print("Addition of Even Number is:",Add)        
    lock.release()
def Oddlist(list,lock):
    lock.acquire()
    print()
    Add = 0
    for i in (list):
        if ((i%2)!= 0):
            Add = Add + i
    print("Adition of Odd Number is:",Add)
    lock.release()
def main():
    print("Inside main")
    arr = []
    print("Enter the number of Elements:")
    size = int(input())
    print("Enter the elements")
    for i in range(size):
        print(f"Enter element:{i+1}")
        value = int(input())
        arr.append(value)
    print("Enterd list is:",arr)
    
    lock = threading.Lock()
    
    t1 = threading.Thread(target = Factor,args = (Evenlist,arr,lock,))
    t2 = threading.Thread(target = Factor,args = (Oddlist,arr,lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("Exit from main")

if __name__ =="__main__":
    main()
