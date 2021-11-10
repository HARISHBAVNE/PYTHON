#Q3.Write a recursive program which display below pattern.
#Input : 5
#Output : 5 4 3 2 1

#solution

def Rev(no):
    if no>=1:
        print(no,end = " " )
        Rev(no-1)
   
def main():
    value = int(input("Enter a number:"))
    Rev(value)

# Code starter
if __name__ == "__main__":
        main()
