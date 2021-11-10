#Q1. Write a recursive program which display below pattern.
#Input : 5
#Output : * * * * *

#solution

def Display(no):   
     i = 0
     if (i<no):
        print("*",end = " ")
        Display(no-1)
    
def main():
    value = int(input("Enter a number:"))
    Display(value)

# Code starter
if __name__ == "__main__":
    main()


  
