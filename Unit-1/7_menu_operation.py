# Menu driven program for list operations

lst = []

while True:
    print("\nMENU")
    print("1. Create List")
    print("2. Display List")
    print("3. Add Element")
    print("4. Delete Element")
    print("5. Sort List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many elements? "))
        lst = []
        for i in range(n):
            element = int(input("Enter element: "))
            lst.append(element)
        print("List created successfully.")

    elif choice == 2:
        print("List:", lst)

    elif choice == 3:
        element = int(input("Enter element to add: "))
        lst.append(element)
        print("Element added.")

    elif choice == 4:
        element = int(input("Enter element to delete: "))
        if element in lst:
            lst.remove(element)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == 5:
        lst.sort()
        print("List sorted.")

    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
