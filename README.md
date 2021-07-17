# Assignment 7: Color addition and subtraction
## COP 4045 Intro to Python
## Dr. Oge Marques
## Group Members
### Humyra Chowdhury Z23405864
### Weiyi Huang Z23502284
### Santiago Monsalve-Mejia Z23502722


# Description
A simple program for performing addition and subtraction using colors. The implementation of this program used classes and object-oriented programming. The user is asked two enter the name or rgb values for two colors, which will then be used to perform the operations.

# Process
## Assignment of Task
Design of the solution: Humyra Chowdhury / Weiyi Huang / Santiago Monsalve-Mejia

Code of the solution: Humyra Chowdhury / Weiyi Huang

Documentation of the solution: Humyra Chowdhury / Weiyi Huang / Santiago Monsalve-Mejia

## Planning
Prior to implementation of the code, the team discussed the algorithm and general flow that will be used to implement the program. Along with this, we also refreshed our understanding of classes and OOP.

# Implementation 
## Project Notes
While designing this "app", we need to do some research to know about and understand how to perform addition and subtraction using colors. We start by designing a class Color with three attributes(the amount of R,G and B in a floating point representation, withing the range from 0 to 1). Our class implements an initializer (“constructor”) that also include code to coerce the r,g,b values into required range (by clipping values below 0 or above 1). We also have a string representation method for "pretty printing" the contents of a Color object. Also, we create a dictionary with the color name as key and the values as the associated RGB tuples.
## Screenshot
![screenshot](/a7screenshot.png)

# Testing
## Testing the Solution
## Future Improvements
For the future improvements, we could prompt user to choose colors on the system, and the program will display the result color image onto the screen. Besides, we also could allow user to chose more than two colors and have more complex calculation.
