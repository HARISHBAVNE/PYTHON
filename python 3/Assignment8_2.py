#Q2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.
import threading

def Factor(fun,no,lock):
    fun(no,lock)

def Evenfactor(no,lock):
    lock.acquire()
    print("Even factors are")
    for i in range(1,(no//2)+1):
        if ((no%i) == 0):
            if ((i%2) == 0):
                print(i,end = " ")
    print()
    lock.release()
def Oddfactor(no,lock):
    lock.acquire()
    print("Odd factors are")
    for i in range(1,(no//2)+1):
        if ((no%i) == 0):
            if ((i%2) != 0):
                print(i,end = " ")
    print()    
    lock.release()
def main():
    print("Inside main")
    value = int(input("Enter the number:"))
    lock = threading.Lock()
    
    t1 = threading.Thread(target = Factor,args = (Evenfactor,value,lock,))
    t2 = threading.Thread(target = Factor,args = (Oddfactor,value,lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("Exit from main")

if __name__ =="__main__":
    main()
