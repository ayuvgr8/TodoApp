try:

    width = float(input("Enter the width of the rectangle:  "))
    length = float(input("Enter the width of the rectangle:  "))

    if width == length:
        exit("That looks like a square with width equal to length")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number !")

