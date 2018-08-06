# coding: utf-8

print("Py learn program!")
name = input("Your name: ")
print(name,",good day!")

answer = input("Shall we study? (Y/N)\n")

if answer == 'y' or answer == 'Y':
    print("It great select, what you want to do?") 
    wanttodo = input("1 - Study Python. 2 - Study GIT. 3 - Read Pikabu\n")
    if wanttodo == '1':
        print("Good select!")
    elif wanttodo =='2':
        print("You know what to do, well done!")
    elif wanttodo == '3':
        print("Bad choice. Better read PEP-8.")
    else:
        print("Uknown answer")
 
elif answer == 'n' or answer == 'N':   
    print("LOOSER!! BYE")
else:
    print("UKNOWN VALUE")
        print("Uknown answer!")
else:
	print("UKNOWN VALUE!")
