#4.Write a recursive program which display below pattern.
#Output : A B C D E F

def Display(No):
    ch =65
    
    for i in range(ch,ch+No):
        print("%c"%i,end = " ")
        
ch = 65    
def DisplayR(No):
    global ch
    c = 65
    if (ch<=c+No):
        print("%c"%ch,end = " ")
        ch +=1
        DisplayR(No)
def main():
    No = int(input("Enter a number"))
    DisplayR(No)


if __name__ == "__main__":
    main()
