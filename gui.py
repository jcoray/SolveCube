#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gui.py
#  
#  Gives the user a GUI to input the cube
#
#  Derived Matthew Uy's cube_solver.cpp program 
#  https://github.com/matt2uy/Cube-Solver
#


from Tkinter import *
import sys

yellow_face = ['y', 'y', 'y',
               'y', 'y', 'y',
               'y', 'y', 'y']

white_face = ['w', 'w', 'w',
              'w', 'w', 'w',
              'w', 'w', 'w']

blue_face = ['b', 'b', 'b',
             'b', 'b', 'b',
             'b', 'b', 'b']

red_face = ['r', 'r', 'r',
            'r', 'r', 'r',
            'r', 'r', 'r']

green_face = ['g', 'g', 'g',
              'g', 'g', 'g',
              'g', 'g', 'g']

orange_face = ['o', 'o', 'o',
               'o', 'o', 'o',
               'o', 'o', 'o']

color_totals = [0]*6

###### Gui functions ########
def enter_yellow_face():
    top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
    bord = [top,mid,btm]
    counter = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

    def change_color(x, b=bord):
        # seems like x is the square number out of the 9 squares
        #global counter
        r=x/3
        c=x%3
        if b[r][c] == 0:
            b[r][c]= 5
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 0
            yellow_face[x] = 'w'

        elif counter[x] == 0:
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 1
            yellow_face[x] = 'b'

        elif counter[x] == 1:
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 2
            yellow_face[x] = 'r'

            ### keep following the cycle of white-yellow-red...
        elif counter[x] == 2:
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 3
            yellow_face[x] = 'g'

        elif counter[x] == 3:
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 4
            yellow_face[x] = 'o'

        elif counter[x] == 4:
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 5
            yellow_face[x] = 'y'

        elif counter[x] == 5:
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 0
            yellow_face[x] = 'w'

    root = Tk()
    root.title('Enter Yellow Face | Red on Top')

    class Knop():
        """This is the docstring of the class"""

        def __init__(self, i, master=None):
            self.nummer = i
            self.row = i/3
            self.col = i%3
            def human_move():
                change_color(self.nummer)
            self.ss = Button(root, command=human_move, bg='yellow', activebackground='yellow', width=10, height=5)
            self.ss.grid(row=self.row, column=self.col) 
            
            next_face = Button(root, text="Next Face",  command=root.destroy)
            next_face.grid(row=4, column=1)  

    bb = range(9)
    for i in range(9):
        bb[i]= Knop(i, master=root)

    mainloop()

def enter_white_face():
    top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
    bord = [top,mid,btm]
    counter = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

    def change_color(x, b=bord):
        # seems like x is the square number out of the 9 squares
        r=x/3
        c=x%3
        if b[r][c] == 0:
            b[r][c]= 5
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 0
            white_face[x] = 'b'

        elif counter[x] == 0:
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 1
            white_face[x] = 'r'

        elif counter[x] == 1:
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 2
            white_face[x] = 'g'

            ### keep following the cycle of white-yellow-red...
        elif counter[x] == 2:
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 3
            white_face[x] = 'o'

        elif counter[x] == 3:
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 4
            white_face[x] = 'y'

        elif counter[x] == 4:
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 5
            white_face[x] = 'w'

        elif counter[x] == 5:
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 0
            white_face[x] = 'b'

    root = Tk()
    root.title('Enter White Face | Orange on Top')

    class Knop():
        """This is the docstring of the class"""

        def __init__(self, i, master=None):
            self.nummer = i
            self.row = i/3
            self.col = i%3
            def human_move():
                change_color(self.nummer)
            self.ss = Button(root, command=human_move, bg='white', activebackground='white', width=10, height=5)
            self.ss.grid(row=self.row, column=self.col) 
            
            next_face = Button(root, text="Next Face",  command=root.destroy)
            next_face.grid(row=4, column=1)

    bb = range(9)
    for i in range(9):
        bb[i]= Knop(i, master=root)

    mainloop()

def enter_blue_face():
    top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
    bord = [top,mid,btm]

    counter = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

    def change_color(x, b=bord):
        # seems like x is the square number out of the 9 squares
        r=x/3
        c=x%3
        if b[r][c] == 0:
            b[r][c]= 5
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 0
            blue_face[x] = 'r'

        elif counter[x] == 0:
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 1
            blue_face[x] = 'g'

        elif counter[x] == 1:
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 2
            blue_face[x] = 'o'

            ### keep following the cycle of white-yellow-red...
        elif counter[x] == 2:
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 3
            blue_face[x] = 'y'

        elif counter[x] == 3:
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 4
            blue_face[x] = 'w'

        elif counter[x] == 4:
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 5
            blue_face[x] = 'b'

        elif counter[x] == 5:
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 0
            blue_face[x] = 'r'

    root = Tk()
    root.title('Enter Blue Face | White on Top')

    class Knop():
        """This is the docstring of the class"""

        def __init__(self, i, master=None):
            self.nummer = i
            self.row = i/3
            self.col = i%3
            def human_move():
                change_color(self.nummer)
            self.ss = Button(root, command=human_move, bg='blue', activebackground='blue', width=10, height=5)
            self.ss.grid(row=self.row, column=self.col) 
            
            next_face = Button(root, text="Next Face",  command=root.destroy)
            next_face.grid(row=4, column=1) 

    bb = range(9)
    for i in range(9):
        bb[i]= Knop(i, master=root)

    mainloop()

def enter_red_face():
    top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
    bord = [top,mid,btm]

    counter = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

    def change_color(x, b=bord):
        # seems like x is the square number out of the 9 squares
        r=x/3
        c=x%3
        if b[r][c] == 0:
            b[r][c]= 5
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 0
            red_face[x] = 'g'

        elif counter[x] == 0:
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 1
            red_face[x] = 'o'

        elif counter[x] == 1:
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 2
            red_face[x] = 'y'

            ### keep following the cycle of white-yellow-red...
        elif counter[x] == 2:
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 3
            red_face[x] = 'w'

        elif counter[x] == 3:
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 4
            red_face[x] = 'b'

        elif counter[x] == 4:
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 5
            red_face[x] = 'r'

        elif counter[x] == 5:
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 0
            red_face[x] = 'g'

    root = Tk()
    root.title('Enter Red Face | White on Top')

    class Knop():
        """This is the docstring of the class"""

        def __init__(self, i, master=None):
            self.nummer = i
            self.row = i/3
            self.col = i%3
            def human_move():
                change_color(self.nummer)
            self.ss = Button(root, command=human_move, bg='red', activebackground='red', width=10, height=5)
            self.ss.grid(row=self.row, column=self.col) 
            
            next_face = Button(root, text="Next Face",  command=root.destroy)
            next_face.grid(row=4, column=1) 

    bb = range(9)
    for i in range(9):
        bb[i]= Knop(i, master=root)

    mainloop()

def enter_green_face():
    top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
    bord = [top,mid,btm]

    counter = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

    def change_color(x, b=bord):
        # seems like x is the square number out of the 9 squares
        r=x/3
        c=x%3
        if b[r][c] == 0:
            b[r][c]= 5
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 0
            green_face[x] = 'o'

        elif counter[x] == 0:
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 1
            green_face[x] = 'y'

        elif counter[x] == 1:
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 2
            green_face[x] = 'w'

            ### keep following the cycle of white-yellow-red...
        elif counter[x] == 2:
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 3
            green_face[x] = 'b'

        elif counter[x] == 3:
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 4
            green_face[x] = 'r'

        elif counter[x] == 4:
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 5
            green_face[x] = 'g'

        elif counter[x] == 5:
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 0
            green_face[x] = 'o'

    root = Tk()
    root.title('Enter Green Face | White on Top')

    class Knop():
        """This is the docstring of the class"""

        def __init__(self, i, master=None):
            self.nummer = i
            self.row = i/3
            self.col = i%3
            def human_move():
                change_color(self.nummer)
            self.ss = Button(root, command=human_move, bg='green', activebackground='green', width=10, height=5)
            self.ss.grid(row=self.row, column=self.col) 
            
            next_face = Button(root, text="Next Face",  command=root.destroy)
            next_face.grid(row=4, column=1)

    bb = range(9)
    for i in range(9):
        bb[i]= Knop(i, master=root)

    mainloop()

def enter_orange_face():
    top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
    bord = [top,mid,btm]

    counter = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

    def change_color(x, b=bord):
        # seems like x is the square number out of the 9 squares
        r=x/3
        c=x%3
        if b[r][c] == 0:
            b[r][c]= 5
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 0
            orange_face[x] = 'y'

        elif counter[x] == 0:
            bb[x].ss.configure(bg='white', activebackground='white')
            counter[x] = 1
            orange_face[x] = 'w'

        elif counter[x] == 1:
            bb[x].ss.configure(bg='blue', activebackground='blue')
            counter[x] = 2
            orange_face[x] = 'b'

            ### keep following the cycle of white-yellow-red...
        elif counter[x] == 2:
            bb[x].ss.configure(bg='red', activebackground='red')
            counter[x] = 3
            orange_face[x] = 'r'

        elif counter[x] == 3:
            bb[x].ss.configure(bg='green', activebackground='green')
            counter[x] = 4
            orange_face[x] = 'g'

        elif counter[x] == 4:
            bb[x].ss.configure(bg='orange', activebackground='orange')
            counter[x] = 5
            orange_face[x] = 'o'

        elif counter[x] == 5:
            bb[x].ss.configure(bg='yellow', activebackground='yellow')
            counter[x] = 0
            orange_face[x] = 'y'

    root = Tk()
    root.title('Enter Orange Face | White on Top')

    class Knop():
        """This is the docstring of the class"""

        def __init__(self, i, master=None):
            self.nummer = i
            self.row = i/3
            self.col = i%3
            def human_move():
                change_color(self.nummer)
            self.ss = Button(root, command=human_move, bg='orange', activebackground='orange', width=10, height=5)
            self.ss.grid(row=self.row, column=self.col) 
            
            next_face = Button(root, text="Solve Cube!",  command=root.destroy)
            next_face.grid(row=4, column=1) 

    bb = range(9)
    for i in range(9):
        bb[i]= Knop(i, master=root)

    mainloop()

def print_face(current_face):
    print current_face[0], current_face[1], current_face[2]
    print current_face[3], current_face[4], current_face[5]
    print current_face[6], current_face[7], current_face[8]

def print_cube():
    print "Yellow Face: "
    print_face(yellow_face)

    print "White Face: "
    print_face(white_face)

    print "Blue Face: "
    print_face(blue_face)

    print "Red Face: "
    print_face(red_face)

    print "Green Face: "
    print_face(green_face)

    print "Orange Face: "
    print_face(orange_face)

def legal_cube_check():
    if yellow_face[4] != 'y' or white_face[4] != 'w' or blue_face[4] != 'b' or red_face[4] != 'r' or green_face[4] != 'g' or orange_face[4] != 'o': 
        print "ERROR: Incorrect center pieces, Try Again"
        sys.exit(1)
    for i, color in enumerate(color_totals):
		#  Check if there are 8 facets per color (excluding centers). 
		if color != 8:
			print "ERROR: Total number of color (",i,") pieces was", color, "out 8."
			sys.exit(1)

def enter_cube():
    enter_yellow_face()
    enter_white_face()
    enter_blue_face()
    enter_red_face()
    enter_green_face()
    enter_orange_face()

############# Script start ###################

# do gui stuff
def to_facets():

	facets = {x:'#' for x in range(1,49)} #  Create dict to hold facets
	position = 0
	position_no_centers = 0
	for face in [white_face, green_face,  red_face, 
				 blue_face,  orange_face, yellow_face]:
		for facet_color in face:
			position += 1 
			if position in [5,14,23,32,41,50]: #  ignore centers
				continue
			else:
				position_no_centers += 1
			facet = ''
			if facet_color is 'w':
				facet = 'U'
				color_totals[0] += 1
			elif facet_color is 'g':
				facet = 'L'
				color_totals[1] += 1
			elif facet_color is 'r':
				facet = 'F'
				color_totals[2] += 1
			elif facet_color is 'b':
				facet = 'R'
				color_totals[3] += 1
			elif facet_color is 'o':
				facet = 'B'
				color_totals[4] += 1
			elif facet_color is 'y':
				facet = 'D'
				color_totals[5] += 1
			facets[position_no_centers] = facet
	legal_cube_check()
	return facets
	

def main():
	print """
http://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Rubik%E2%80%99s_cube_colors.svg/2000px-Rubik%E2%80%99s_cube_colors.svg.png
+----------------+--------------+ 
| Color in Front | Color on Top |
+----------------+--------------+
|1)   Yellow (D) | Red          |
|2)    White (U) | Orange       |
|3)     Blue (R) | White        |
|4)      Red (F) | White        |
|5)    Green (L) | White        |
|6)   Orange (B) | White        |
+----------------+--------------+
"""
	enter_cube()

	facets = {x:'#' for x in range(1,49)} #  Create dict to hold facets
	position = 0
	position_no_centers = 0

	for face in [white_face, green_face,  red_face, 
				 blue_face,  orange_face, yellow_face]:
		for facet_color in face:
			position += 1 
			if position in [5,14,23,32,41,50]: #  ignore centers
				continue
			else:
				position_no_centers += 1
			facet = ''
			if facet_color is 'w':
				facet = 'U'
				color_totals[0] += 1
			elif facet_color is 'g':
				facet = 'L'
				color_totals[1] += 1
			elif facet_color is 'r':
				facet = 'F'
				color_totals[2] += 1
			elif facet_color is 'b':
				facet = 'R'
				color_totals[3] += 1
			elif facet_color is 'o':
				facet = 'B'
				color_totals[4] += 1
			elif facet_color is 'y':
				facet = 'D'
				color_totals[5] += 1
			facets[position_no_centers] = facet
	legal_cube_check()
	print facets
	return 0

if __name__ == '__main__':
	main()
