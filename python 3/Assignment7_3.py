#Q3. Write a program which contains one class named as Numbers. Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.SumFactors() method will return addition of all factors. 
# Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self,Value):
        self.Value = Value
    
    def Factors(self,No):
        print("Factors are")
        for i in range(1,int(No/2)+1):
            if (No%i) == 0:
                print(i,end = " ")
    
    def ChkPrime(self,No):
        flag = 0
        for i in range(2,int(No/2)+1):
            if No%i == 0:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False
    
    def ChkPerfect(self,No):
        sum = 0
        for i in range(1,int(No/2)+1):
            if No%i == 0:
                sum = sum + i
        if sum == No:
            return True
        else:
            return False
            
    def SumFactors(self,No):
        Add = 0
        for i in range(1,int(No/2)+1):
            if (No%i) == 0:
                Add = Add + i
        return Add
        
    
    
def main():
    No = int(input("Enter Number"))
    obj = Arithmetic(No)
    obj.Factors(No)
    Ret = obj.ChkPrime(No)
    if Ret == True:
        print(f"\n{No} is Prime number")
    else:
        print(f"\n{No} is not prime")
    
    Ret = obj.ChkPerfect(No)
    if Ret == True:
        print(f"{No} is Perfect Number")
    else:
        print(f"{No} is Non Perfect Number")
    
    Ret = obj.SumFactors(No)
    print(f"Addition of {No}'s Factor is:",Ret)
if __name__ == "__main__":
    main()
