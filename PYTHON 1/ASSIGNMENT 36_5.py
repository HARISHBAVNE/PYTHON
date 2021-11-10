#5.Write a recursive program which display below pattern.
#Output : a b c d e f

def Display(No):
    ch =97
    
    for i in range(ch,ch+No):
        print("%c"%i,end = " ")
        
ch = 97    
def DisplayR(No):
    global ch
    c = 97
    if (ch<=c+No):
        print("%c"%ch,end = " ")
        ch +=1
        DisplayR(No)
def main():
    No = int(input("Enter a number"))
    DisplayR(No)


if __name__ == "__main__":
    main()
