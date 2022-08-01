# Author: Fransiskus Agapa

############################################
# main class would have shared name of variable
# sub class would inherit from main class and
# would be able to access data in main class using
# super function - super()
############################################

class SharedName:

    def __init__(self, length, height):
        self.length = length
        self.height = height


class Rectangular(SharedName):

    def __init__(self, length, height, width):
        super().__init__(length, height)
        self.width = width

    def volume(self):
        return self.length * self.width * self.height


class Cube(SharedName):

    def __init__(self, length, height):
        super().__init__(length, height)

    def volume(self):
        return self.length * self.length * self.length


class Cylinder(SharedName):

    def __init__(self, pi_val, length, height, radius):
        super().__init__(length, height)
        self.pi_val = pi_val
        self.radius = radius

    def volume(self):
        return self.pi_val * self.radius * self.radius * self.height


print("\n== Volume of Shape ==")
print("1. Rectangular")
print("2. Cube")
print("3. Cylinder")
print("E. Exit")
choice = input("choice: ").lower()                 # make user input to lower case, make is easier for while-loop condition

place_holder = 0                                   # some shapes will not use all the variable name in main (parent) class
pi_value = 3.1428                                  # some shapes need pi value to calculate its volume

while choice != 'e':
    if choice == '1':
        print("\n[ Rectangular ]\n")
        try:                                       # just in case user input is not digit
            print("Input the length: ", end=" ")   # end=" ' - just to make the prompt the user input in one line
            r_len = int(input())
            print("Input the height: ", end=" ")
            r_hei = int(input())
            print("input the width: ", end=" ")
            r_wid = int(input())
            rectangular = Rectangular(r_len, r_hei, r_wid)
            print("\n[ The volume of rectangular: " + str(rectangular.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    elif choice == '2':
        print("\n[ Cube ]\n")
        try:
            print("Input the length/side: ", end=" ")
            c_len_sid = int(input())
            cube = Cube(c_len_sid, place_holder)  # cube only need one value to calculate it volume, we put a place_holder to meet declaration in main
            print("\n[ The volume of cube: " + str(cube.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    elif choice == '3':
        print("\n[ Cylinder ]\n")  # pi * r^2 * h
        try:
            print("Input the radius(half diameter): ", end=" ")
            cy_rad = int(input())
            print("Input the height: ", end=" ")
            cy_hei = int(input())
            cylinder = Cylinder(pi_value, place_holder, cy_hei, cy_rad)
            print("\n[ The volume of cylinder: " + str(cylinder.volume()) + " ]")
        except ValueError:
            print("\n[ Invalid input - Digit only ]")

    else:
        print("\n[ Invalid choice ]")

    choice = input("\nchoice: ").lower()


print("\n== Exit Program ==")
