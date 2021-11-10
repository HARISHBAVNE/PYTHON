#Q 2. Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5

#solution
    
i = 1
def Display(no):
    global i
    if (i <= no):
        print(i,end=" ")
        i = i+1
        Display(no)
        
def main():
    value =int(input("Enter a number:"))
    Display(value)

#Code starter
if __name__ == "__main__":
    main()
