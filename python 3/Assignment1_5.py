#Q.5.Write a program which display 10 to 1 on screen.
#Output : 10 9 8 7 6 5 4 3 2 1


#Solution:

# Function for Reverse order
def RevN(num):
    for i in range(num,0,-1):
        print(i,end = " ")

def main():
    RevN(10)

# Code starter    
if __name__ == "__main__":
    main()
