#Q6. Write a program which accept one number and display below pattern.
#Input : 5
#Output :
#* * * * *
#* * * *
#* * *
#* *
#*


#solution

def Pattern(value):
    for row in range(value+1,0,-1):
        for col in range(row):
            print("* ",end = " ")
        print()

def main():
    print("Enter a number for printing pattern")
    num = int(input())
    pat = Pattern(num)

#Code starter
if __name__ == "__main__":
    main()
