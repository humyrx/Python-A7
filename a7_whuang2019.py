###########################################################################
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
        if (self.red, self.green, self.blue) in colors.values():
            for key,val in colors.items():
                if val == (self.red, self.green, self.blue):
                    return key
        else:
            self.red = round(self.red,1)
            self.green = round(self.green,1)
            self.blue = round(self.blue,1)
            return str((self.red, self.green, self.blue))


    def __repr__(self):
        # print a representaion of object
        return self.__str__()




###############################################################################################
######################################## MAIN FUNCTION ########################################

def main_function():
    color_one = input("Enter the name or (r, g, b) values for color 1: ")
    color_two = input("Enter the name or (r, g, b) values for color 2: ")

    try:
        check = eval(color_one)
    except:
        check = colors[color_one]
    color1 = Color(check[0],check[1],check[2])

    try:
        check = eval(color_two)
    except:
        check = colors[color_two]
    color2 = Color(check[0],check[1],check[2])

    print("Color1 + Color2 = ", color1 + color2)
    print("Color1 - Color2 = ", color1 - color2)

    option = input("Would you like to try again? (y for yes, others for no)") ## Ask if the user want to try again 
    while True:
       if option=="y":
          main_function() ##If yes, run the main function again
       else:
          print("Goodbye")
          loop = False
          exit()

main_function()









       
            
           