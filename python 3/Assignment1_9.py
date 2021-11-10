#Q9. Write a program which display first 10 even numbers on screen.
#Output : 2 4 6 8 10 12 14 16 18 20


#Solution:

# Function for calculate first 20 even numbers
def even(value):
    i = 0
    ev = []
    for i in range (1,value):
        if i % 2 == 0:
            ev.append(i)      #  list Append method to insert element in list
        i += 1
        if len(ev) == 10:
            break
    return (ev)

def main():
    print(even(100))

# Code starter
if __name__ == "__main__":
    main()
