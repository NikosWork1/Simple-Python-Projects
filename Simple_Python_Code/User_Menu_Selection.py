choice= 0
while choice!=4:
    print('\nMenu:')
    print("1.Option A")
    print("2.Option B")
    print("3.Option C")
    print("4.Exit")
    choice= int(input("Enter your choice(1-4): "))
    if choice==1:
        print("You selected option A")
    elif choice==2:
        print("You selected option B")
    elif choice==3:
        print("You selected option C")
    elif choice==4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input")
