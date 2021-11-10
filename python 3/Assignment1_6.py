#Q6.Write a program which accept number from user and check whether that number is positive or
#negative or zero.
#Input : 11 Output : Positive Number
#Input : -8 Output : Negative Number
#Input : 0 Output : Zero


#Solution

# Function for number is positive or negative
def PNZ(value):
    if value > 0:
        return "Positive Number"
    elif value < 0:
        return "Negative Number"
    else:
        return "Zero"

def main():
    print("Enter a number for checking positive or negative")
    num = int(input())
    ans = PNZ(num)
    print(f"{num} is: ",ans)

# Code starter
if __name__ == "__main__":
    main()
