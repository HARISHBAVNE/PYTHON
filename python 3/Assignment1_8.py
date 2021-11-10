#Q8. Write a program which accept number from user and print that number of “*” on screen.
#Input : 5 Output : * * * * *

#Solution:


def stars(value):
    return ("*  " * (value))

def main():
    print("Enter a number howmuch time to print * on screen")
    no = int(input())
    ans = stars(no)
    print(ans)

# Code starter
if __name__ == "__main__":
    main()    
