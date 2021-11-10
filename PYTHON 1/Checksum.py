import hashlib
def Checksum(name,blocksize = 1024):
    hobj = hashlib.md5()

    fd = open(name,'rb')
    buffer = fd.read(blocksize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fd.read(blocksize)
    print(hobj.hexdigest())
def main():
    name = input("Enter a file name:")
    Checksum(name)
    
if __name__ == "__main__":
    main()
