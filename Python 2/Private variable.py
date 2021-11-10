class student:
    def __init__(self,no):
        self.__rollno = no
    def p(self):
        print(self.__rollno)
def main():
    no = 5
    obj = student(no)
    obj.p()
if __name__ == "__main__":
    main()
