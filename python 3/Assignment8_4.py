#Q4.Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.
import threading
import os

def Small(s,lock):
    lock.acquire()
    count = 0
    for i in (s):
        if ((i >= 'a') and (i <= 'z')):
            count = count + 1
    print("Count of Small letters:",count)
    threading.current_thread().name = "Small"
    print("Name of thread is:",threading.current_thread().name)
    print("Id of small thread is:",os.getpid())
    print()
    lock.release()

def Capital(s,lock):
    lock.acquire()
    count = 0
    for i in (s):
        if ((i >= 'A') and (i <= 'Z')):
            count = count + 1
    print("Count of Capital letters:",count)
    threading.current_thread().name = "Capital"
    print("Name thread is:",threading.current_thread().name)
    print("Id of Capital thrad is:",os.getpid())
    print()
    
    lock.release()

def Digits(s,lock):
    lock.acquire()
    count = 0
    for i in (s):
        if ((i >= "0") and (i <= "9")):
            count = count + 1
    print("Count of digits:",count)
    threading.current_thread().name = "Digits"
    print("Name of thread is:",threading.current_thread().name)
    print("Id of Digit thread is:",os.getpid())
    print()
    
    lock.release()
def main():
    print("Inside main")
    string = input("Enter a string:")
    
    lock = threading.Lock()
    
    t1 = threading.Thread(target = Small,args = (string,lock))
    t2 = threading.Thread(target = Capital,args = (string,lock))
    t3 = threading.Thread(target = Digits,args = (string,lock))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("Exit from main")

if __name__ =="__main__":
    main()
