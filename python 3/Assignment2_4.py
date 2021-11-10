#Q4.Write a program which accept one number form user and return addition of its factors.
#Input : 12 Output : 16 (1+2+3+4+6)


#solution
def AddF(n):
    fact = []
    for i in range(1,n):
        if n%i == 0:
            fact.append(i)
             
    sum = 0
    for j in range(len(fact)):
        sum = sum + fact[j]
        j = j + 1
    return sum

def main():
    num = int(input("Enter a number:"))
    ans = AddF(num)
    print(ans)
    
#Code starter
if __name__ == "__main__":
    main()
