# 5. Accept division of student from user and depends on the division
# display exam timing. There are 4 divisions in school as A,B,C,D. Exam
# of division A at 7 AM, B at 8.30 AM, C at 9.20 AM and D at 10.30 AM.
# (Application should be case insensitive)
# Input : C
# Output : Your exam at 9.20 AM
# Input : d
# Output : Your exam at 10.30 AM

def Display(ch):
    if (ch == ord("A")or ch == ord("a")):
        print("Your exam at 7:00 AM.")
    elif (ch == ord("B")or ch == ord("b")):
        print("Your exam at 8:30 AM.")
    elif (ch == ord("C")or ch == ord("c")):
        print("Your exam at 9:20 AM.")
    elif (ch == ord("D")or ch == ord("d")):
        print("Your exam at 10:30 AM.")


def main():
    ch = ord(input("Enter a character:"))
    ret = Display(ch)
    
if __name__ == "__main__":
    main()
