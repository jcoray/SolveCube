#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cube.py
#  
#  Copyright 2015 Jakob Coray <jakob2016@gmail.com> and Gabriel Norris
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details. 
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import subprocess
import gui
import arduino

class Cube(object):
	mappings = {'UF':[7,18],  'UR':[5,26],  'UB':[2,34],  'UL':[4,10], 
				'DF':[42,23], 'DR':[45,31], 'DB':[47,39], 'DL':[44,15], 
				'FR':[21,28], 'FL':[20,13], 'BR':[36,29], 'BL':[37,12], 
				'UFR':[8,19,25], 'URB':[3,27,33], 'UBL':[1,35,9],  'ULF':[6,11,17], 
				'DRF':[43,30,24],'DFL':[41,22,16],'DLB':[46,14,40],'DBR':[48,38,32]}

	ordered_cubies = ('UF',  'UR',  'UB',  'UL',  'DF', 
					  'DR',  'DB',  'DL',  'FR',  'FL', 
					  'BR',  'BL',  'UFR', 'URB', 'UBL', 
					  'ULF', 'DRF', 'DFL', 'DLB', 'DBR')
	
	def __init__(self, facets=None, cubies=None):
		if facets is None:
			facets = {x:'#' for x in range(1,49)} #  Create dict to hold facets
		self.facets = facets
		self.cubies = cubies
	
	def cubies_arg(self):
		return ' '.join(self.cubies) #  String to send to solver program
		
	def set_cubies(self):
		buffer_cubies = list()
		for position, cubie in enumerate(self.ordered_cubies):
			buffer_cubie = str()
			for facet in self.mappings[self.ordered_cubies[position]]:
				buffer_cubie += self.facets[facet]
			buffer_cubies.append(buffer_cubie)
		self.cubies = buffer_cubies
		return self.cubies_arg()
	
	def print_cubies(self):
		print 'Position:', ' '.join(self.ordered_cubies)
		print 'Scramble:', self.cubies_arg()
	
	
	def print_facets(self, method = None):
		if method is None:
			print """
                +----+----+----+
                | 1  | 2  | 3  |
                +----+----+----+
                | 4  | U  | 5  |
                +----+----+----+
                | 6  | 7  | 8  |
+----+----+----++----+----+----++----+----+----++----+----+----+
| 9  | 10 | 11 || 17 | 18 | 19 || 25 | 26 | 27 || 33 | 34 | 35 |
+----+----+----++----+----+----++----+----+----++----+----+----+
| 12 | L  | 13 || 20 | F  | 21 || 28 | R  | 29 || 36 | B  | 37 |
+----+----+----++----+----+----++----+----+----++----+----+----+
| 14 | 15 | 16 || 22 | 23 | 24 || 30 | 31 | 32 || 38 | 39 | 40 |
+----+----+----++----+----+----++----+----+----++----+----+----+
                +----+----+----+
                | 41 | 42 | 43 |
                +----+----+----+	
                | 44 | D  | 45 |
                +----+----+----+
                | 46 | 47 | 48 |
                +----+----+----+"""

def main():
	pins = [9,10,12,11]
	positions = [172, 86, 8, 132, 75,
				 180, 95, 17, 132, 75] 
	#  You may need to manually set the serial port. 
	#  On Linux machines the serial port will be similar 
	#  to '/dev/ttyACM'. Open up a terminal window and type:
	#      $_  ls /dev | grep ttyACM 
	#  to list devices. One of these should be your Arduino.
	robot = arduino.Robot(pins, positions)
	gui.enter_cube()
	input_facets = gui.to_facets()
	rubik = Cube(input_facets)
	rubik.set_cubies()
	rubik.print_cubies()
	#  The solver algorithm is written in c++. It needs to be compiled. 
	solution = subprocess.check_output("./cubecompo " + rubik.cubies_arg(), shell=True)
	#solution = subprocess.check_output("./cubecompo " + ' LU LF LD UB DF RD LB BD RB FU RF RU UBL FLD LBD RUF ULF RBU RDB FDR', shell=True)

	print "Solution:", solution
	robot.solve(solution)
	return 0

if __name__ == '__main__':
	main()
