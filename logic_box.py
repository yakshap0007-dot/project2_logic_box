print("hello sir,i give a many option to you to choose from you select one of them")

while True:
    print("option 1: Generate  a selected pattern")
    print("option 2: Analyze a range of numbers with the given criteria")
    print("option 3: Exit the program")

    option=int(input("enter your option:"))
    if option == 1:
        print("enter your row number:")
        row=int(input())
        for i in range(row):
            for j in range(i+1):
                print("*",end="")
                i=i+1
            print()

    elif option == 2:
        # option=int(input())
        start=int(input("enter the start number:"))
        stop=int(input("enter the stop number:"))

        sum=0

        for i in range(start,stop+1):
            if i%2==0:
                print(i," is even:")
            else:
                print(i," is odd:")

                sum = sum + i
        total=sum 
        print("Sum of all values=",total)

    elif option == 3:
        print("thank you for using this program")
        print("good bye")
        break

    else:
        print("invalid option, please try again")