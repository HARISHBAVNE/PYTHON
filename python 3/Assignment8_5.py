#Q5.Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.
# Piyush
import threading
    
def DisplayF(lock,e):
    e.set()
    lock.acquire()
    no = 50
    print("Numbers in forword order")
    for i in range(1,no+1):
        print(i,end = " ")
    print()
    lock.release()
    e.clear()
def DisplayR(lock,e):
    e.wait()
    lock.acquire()
    no = 50
    print("Numbers in reverse order")
    for i in range((no),0,-1):
        print(i,end = " ")
    print()
    lock.release()
    
def main():
    print("Inside main")
    lock = threading.Lock()
    e = threading.Event()
    t1 = threading.Thread(target = DisplayF,args = (lock,e))
    t2 = threading.Thread(target = DisplayR,args = (lock,e))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("End process")
if __name__ == "__main__":
    main()
