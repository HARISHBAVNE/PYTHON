# 2. Accept N numbers from user and display all such elements which are
# divisible by 5.
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 85 80

def Display(Numbers):
    for i in range(len(Numbers)):
        if Numbers[i]%5 == 0:
            print(Numbers[i],end = " ")
            
def main():
    Numbers = []
    size = int(input("Enter number of elements:"))
    
    print("Enter a elements")
    for i in range(size):
        value = int(input("Element {}:".format(i+1)))
        Numbers.append(value)
    Display(Numbers)
    
if __name__ == "__main__":
    main()