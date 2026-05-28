'''Write a python program that accept a line of text from user and perform following
operation on it.
1. Toggle case
2. Title case
3. Sentence case
4. Exit
Note: Menu will be repeated until user select Exit option.'''

text = input("Enter a line of text: ")

while True:
    print("\n1. Toggle case")
    print("2. Title case")
    print("3. Sentence case")
    print("4. Exit")

    choice = int(input("Enter number: "))

    if choice == 1:
        print(text.swapcase())
    elif choice == 2:
        print(text.title())
    elif choice == 3:
        print(text.capitalize())
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid number")