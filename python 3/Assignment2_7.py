#7. Write a program which accept one number and display below pattern.
#Input : 5
#Output :
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

#solution

def Pattern(value):
    for row in range(1,value+1):
        for col in range(1,value+1):
            print(col,end =" ")
        print()

# Code Starter        
def main():
    print("Enter a number for printing pattern")
    num = int(input())
    pat = Pattern(num)

if __name__ == "__main__":
    main()
