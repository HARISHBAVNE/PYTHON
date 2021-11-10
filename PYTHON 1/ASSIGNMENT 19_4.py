# 4. Accept N numbers from user and accept Range, Display all elements from
# that range
# Input : N : 6
# Start: 60
# End : 90
# Elements : 85 66 3 76 93 88
# Output : 85 66 76 88
# Input : N : 6
# Start: 30
# End : 50
# Elements : 85 66 3 76 93 88
# Output = 
def Occurence(Numbers,Start,End):
    for i in range(len(Numbers)):
        if ((Numbers[i]>Start)and(Numbers[i]<End)):
            print(Numbers[i],end = " ")
            
def main():
    Numbers = []
    size = int(input("Enter a number of element:"))
    
    print("Enter a elements")
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    Start = int(input("Enter Starting point:"))
    End = int(input("Enter Ending point:"))
    Occurence(Numbers,Start,End)
    
if __name__ == "__main__":
    main()