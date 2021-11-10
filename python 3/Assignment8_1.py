#Q1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.
import threading

def EvenOdd(fun,lock):
    fun(lock)
    
def Even(lock):
    lock.acquire()
    no = 10
    print("Even Numbers are")
    for i in range(1,(no*2)+1):
        if ((i%2) == 0):
            print(i,end = " ")
    print()
    lock.release()
def Odd(lock):
    lock.acquire()
    no = 10
    print("Odd Numbers are")
    for i in range(1,(no*2)+1):
        if ((i%2) != 0):
            print(i,end = " ")
    print()
    lock.release()
    
def main():
    print("Inside main")
    lock = threading.Lock()
    
    t1 = threading.Thread(target = EvenOdd,args = (Even,lock))
    t2 = threading.Thread(target = EvenOdd,args = (Odd,lock))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("End process")
if __name__ == "__main__":
    main()
