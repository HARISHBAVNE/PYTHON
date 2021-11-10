#Q10. Write a program which accept name from user and display length of its name.
#Input : Marvellous Output : 10


#Solution:

#function for length of given name 
def length(name):
    return len(name)

def main():
    print("Enter your name")
    Name = input()          # Accept name from user.
    ans = length(Name)
    print(ans)

# Code starter
if __name__ == "__main__":
    main()
