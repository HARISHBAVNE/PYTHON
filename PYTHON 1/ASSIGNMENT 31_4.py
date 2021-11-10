# 4. Write application which accept file name from user and display size of file.
# Input : Demo.txt
# Output : File size is 56 bytes
import os
def FileSize(fname):
    fd = open(fname,'r')
    size = os.path.getsize(fname)
    print(f"Size of file:{size}bytes")

def main():
    FileName = input("Enter file name")
    FileSize(FileName)
    
if __name__ == "__main__":
    main()
