def Substraction(no1,no2):                         #100
    return no1-no2

def SmartSub(funcName):                         #200
    def decorator(a,b):                         #300
        if a < b :
            a,b = b,a
        return funcName(a,b)                    #call 100
    return decorator                            #return 300
    
def main():                                     #400
    sub = SmartSub(Substraction)                #call 200(100) contains 300 
    no1 = int(input("Enter first number:"))
    no2 = int(input("Enter second number:"))
    
    ret = sub(no1,no2)                          #
    print("Substraction is:",ret)
    
if __name__ == "__main__":                      #Call 400
    main()
