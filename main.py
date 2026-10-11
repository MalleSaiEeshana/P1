
print("LOOP ART DESIGNER")
print("1. Triangle Pattern")
print("2. Floyd's Triangle")
print("3. Diamond Pattern")

choice = int(input("Choose a pattern (1-3): "))
rows = int(input("Enter the number of rows: "))

if choice == 1:
    # Triangle Pattern
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

elif choice == 2:
    # Floyd's Triangle
    number = 1

    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()

elif choice == 3:
    # Diamond Pattern - upper half
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

    # Diamond Pattern - lower half
    for i in range(rows - 1, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

else:
    print("Invalid choice! Please choose 1, 2, or 3.")
