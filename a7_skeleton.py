# ###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###          Assignment 7: Color addition and subtraction               ###
###          -- Team Members --                                         ###
###          Name: Humyra Chowdhury             Z#: 23405864            ###
###          Name: Weiyi Huang                  Z#: 23502284            ###
###          Name: Santiago Monsalve-Mejia      Z#: 23502722            ###
###          Date: Jul 16, 2021                                         ###
### Description: a simple program to perform addition and subtraction   ###
### using colors.                                                       ###
###########################################################################

# dict with the color names as key and the values as the associated RGB tuples
# used when the user enters a color name 
# and after the rgb values have been calculated (reverse look up to see if the rgb values matches a name)
colors = {
    # primary colors
    "red": (1, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
    # secondary colors
    "magenta": (1, 0, 1),
    "yellow": (1, 1, 0),
    "cyan": (0, 1, 1),
    # black and white
    "black": (0, 0, 0),
    "white": (1, 1, 1)
}



class Color(object):
    def __init__(self,r,g,b):
        # coerce values into required range by saturating
        if r < 0: r = 0 # if value is less than 0, make it 0
        if r > 1: r = 1 # if value is greater than 1, make it 1
        self.red = float(r)

        if g < 0: g = 0
        if g > 1: g = 1
        self.green = float(g)

        if b < 0: b = 0
        if b > 1: b = 1
        self.blue = float(b)


    def __add__(self,x):
        # add two colors
        return Color(self.red+x.red, self.green+x.green, self.blue+x.blue)


    def __sub__(self,x):
        # subtract two colors
        return Color(self.red-x.red, self.green-x.green, self.blue-x.blue)


    def __str__(self):
        # convert to a readable string
        rgb = "(" + str(round(self.red, 1)) + ", " + str(round(self.green, 1)) + ", " + str(round(self.blue, 1)) + ")"
        return rgb


    def __repr__(self):
        # print a representaion of object
        return self.__str__()



def convert_userinput(acolor):
    # if user entered the name of the color
    if acolor.isalpha():
        for key in colors: # traverse through the colors dict
            if acolor == key: # if color name matches a key in the colors dict
                acolor_rgb = colors[key] # get and set the rgb values for the color

    # if user entered the (r, g, b) values for the color
    else:
        acolor_arr = acolor.replace("(", "").replace(")", ""). replace(" ", "").split(",") # clean up the input to get an array of numbers
        acolor_rgb = tuple([float(item) for item in acolor_arr]) # convert each element in the array into a float, then convert the array into a tuple

    return Color(acolor_rgb[0], acolor_rgb[1], acolor_rgb[2])



###############################################################################################
######################################## MAIN FUNCTION ########################################
print()
print("To practice our understanding of classes and OOP, a simple program for performing addition and subtraction using colors is implemented. ")
print("The user is asked to enter the name or rgb values for two colors. These colors will then be used to perform the operations. \n")

color1 = input("Enter the name or (r, g, b) values for color 1: ")
color2 = input("Enter the name or (r, g, b) values for color 2: ")

c1 = convert_userinput(color1)
c2 = convert_userinput(color2)

added_c = c1.__add__(c2)
print("Color 1 + Color 2 = ", added_c)

subt_c = c1.__sub__(c2)
print("Color 1 - Color 2 = ", subt_c)





