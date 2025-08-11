# Ask user to input the length of the 3 sides of a triangle
x=int(input("Enter first side:\n"))
y=int(input("Enter second side:\n"))
z=int(input("Enter third side:\n"))
# If all sides are equal print Equilateral
if x == y and y == z:
    print("Equilateral")
# If 2 sides are equal print Isosceles
elif x == y or y == z or x == z:
    print("Isosceles")
# If no sides are equal print Scalene