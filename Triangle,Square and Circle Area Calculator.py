print ('Welcome to your favourite area calculator\n')

type = input("Please choose from those shapes to calculate its area (Circle, Triangle, Square, Rectangle)\n").lower()

if type == "rectangle" :
    length =
    width = float(input ("please type the width of the rectangle\n"))
    r_area = length * width
    print ("The area =", r_area)

elif type == "square":
    length = float(input("Please type the length of the square\n"))
    s_area = length * width
    print("The area =", s_area)

elif type == "circle" :
    radius = float(input("Please type the radius of the circle\n"))
    c_area = 3.14 * radius**2
    print("The area =", c_area)

elif type == "triangle" :
    base = float(input("Please type the base of the triangle\n"))
    height = float(input("Please type the height of the triangle\n"))
    t_area = 0.5 * base * height
    print("The area =", t_area)

else :
    print ("Please type one of the shapes mentioned above and try again")
