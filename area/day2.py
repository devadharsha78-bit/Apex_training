while True:
    print("\n1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius: "))
        area = int(3.14 * radius * radius)
        print("Area of Circle =", area)

    elif choice == 2:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = int(length * breadth)
        print("Area of Rectangle =", area)

    elif choice == 3:
        side = float(input("Enter the side: "))
        area = int(side * side)
        print("Area of Square =", area)

    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice")
