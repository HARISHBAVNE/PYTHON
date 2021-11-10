#1. Write a program which displays ASCII table. Table contains symbol,
#Decimal, Hexadecimal and Octal representation of every member from
#0 to 255.

def DisplayASCII():
    print("Dec\tchar\toctal\tHexadecimal")
    for i in range(0,256):
        print(f"{i}\t{chr(i)}\t{oct(i)}\t{hex(i)}")
        
        
def main():
    DisplayASCII()
    
if __name__ == "__main__":
    main()
