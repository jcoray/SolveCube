#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  arduino.py
#  
#  Copyright 2015 Gabriel Norris <gabe.norris@ymail.com> Jakob Coray <jakob2016@gmail.com>
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
#
# "We cannot solve our problems with the same thinking that we used
#  when we created them."
#                           -Albert Einstein

from pyfirmata import Arduino, util
#  https://media.readthedocs.org/pdf/pyfirmata/latest/pyfirmata.pdf
import sys
import time

class Cube(object):
	def __init__(self):
		self.orient = {'D':'D', 'F':'F', 'R':'R', 'B':'B', 'L':'L', 'U':'U',} # TODO Does this really need to be it's own class?
class Claw(object):
	def __init__(self, arduino, wrist_pin, hand_pin, positions, hand_delay, quarter_turn_delay):
		arduino.servo_config(wrist_pin, 1000, 2000, 90) 
		arduino.servo_config(hand_pin, 1000, 2000, 90)
		self.wrist = arduino.digital[wrist_pin]
		self.hand = arduino.digital[hand_pin]
		
		self.home_turn_deg = positions[0]
		self.quarter_turn_deg = positions[1]
		self.half_turn_deg = positions[2]
		self.open_hand_deg = positions[3]
		self.close_hand_deg = positions[4]
		
		self.quarter_turn_delay = quarter_turn_delay
		self.half_turn_delay = quarter_turn_delay * 2
		self.hand_delay = hand_delay
		
	def home_turn(self):
		self.wrist.write(self.home_turn_deg)
		time.sleep(self.quarter_turn_delay)
	def quarter_turn(self):
		self.wrist.write(self.quarter_turn_deg)
		time.sleep(self.quarter_turn_delay)
	def half_turn(self):
		self.wrist.write(self.half_turn_deg)
		time.sleep(self.half_turn_delay)

	def open_hand(self):
		self.hand.write(self.open_deg)
		time.sleep(self.hand_delay)
	def close_hand(self):
		self.hand.write(self.close_deg)
		time.sleep(self.hand_delay)
		
		
class Robot(object):
	def __init__(self, serial_port, pins, positions, hand_delay=.25, quarter_turn_delay=.5):
		sys.stdout.write("Connecting to Arduino...") #  Print w/o \n
		#  On Linux machines the serial port will be similar 
		#  to '/dev/ttyACM'. Open up a terminal window and type:
		#      $_  ls /dev | grep ttyACM 
		#  to list devices. One of these should be your Arduino.
		arduino = Arduino(serial_port)
		print "Connected."
		print "Configuring Arduino..."
		iterator = util.Iterator(arduino)
		iterator.start()
		sys.stdout.write("    Configuring down_claw... ") #  Print w/o \n
		self.claw_down = Claw(arduino, pins[0], pins[1], positions[0:4], delay_hand, quarter_turn_delay)
		print "Done."
		sys.stdout.write("    Configuring up_claw... ") #  Print w/o \n
		self.claw_right = Claw(arduino, pins[2], pins[3], positions[5:9], delay_hand, quarter_turn_delay)
		print "Done."
		print "Configured."
		
		self.cube = Cube()
		
	def rotate_90(face):
		buffer_orient = {'D':'D', 'F':'F', 'R':'R', 'B':'B', 'L':'L', 'U':'U',}
		face_orient = self.cube.orient 
		#  Find ...
		for orient in self.cube.orient:
			if face is self.cube.orient[orient]:
				face_orient = self.cube.orient[orient]
		if face_orient is 'D': #  Face held in claw_down
			self.claw_down.quarter_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
		elif face_orient is 'F': 
			self.claw_right.open_hand()
			self.claw_down.quarter_turn()
			self.claw_right.close_hand()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			self.claw_right.quarter_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
		elif face_orient is 'R': #  Face held in claw_right
			self.claw_right.quarter_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
		elif face_orient is 'B':
			self.claw_down.open_hand()
			self.claw_right.quarter_turn()
			self.claw_down.close_hand()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
			self.claw_down.quarter_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
		elif face_orient is 'L':
			self.claw_right.open_hand()
			self.claw_down.half_turn()
			self.claw_right.close_hand()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			self.claw_right.quarter_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
		elif face_orient is 'U':
			self.claw_down.open_hand()
			self.claw_right.half_turn()
			self.claw_down.close_hand()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
			self.claw_down.quarter_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
		#  Update the orientation. TODO this is not updated for the dict
		for ii_orient, ii_face in enumerate(buffer_orient):
			self.cube.orient[ii_orient] = ii_face
		return self.cube.orient
		
	def rotate_180(face): 
		buffer_orient = []
		face_orient
		for orient, iiface in enumerate(self.cube.orient):
			if face = iiface:
				face_orient = orient
		
		if face_orient is 0: #  Face held in claw_down
			self.claw_down.half_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			buffer_orient[0] = self.cube.orient[0] #  The face in the claw does not move
			buffer_orient[1] = self.cube.orient[4] #  L -> F
			buffer_orient[2] = self.cube.orient[1] #  F -> R
			buffer_orient[3] = self.cube.orient[2] #  R -> B
			buffer_orient[4] = self.cube.orient[3] #  B -> L
			buffer_orient[5] = self.cube.orient[5] #  Top does not move
		elif face_orient is 1: 
			pass
		elif face_orient is 2: #  Face held in claw_down
			self.claw_right.half_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
		elif face_orient is 3:
			pass
		elif face_orient is 4:
			pass
		elif face_orient is 5:
			pass
		
		#  Update the orientation. 
		for ii_orient, ii_face in enumerate(buffer_orient):
			self.cube.orient[ii_orient] = ii_face
		return self.cube.orient

	def solve(self, solution):
		prev = 0
		moves = []
		error_count = 0
		for char in solution:
			if char.isdigit():
				#  Invert the move and add it to the list. E.g. 'U2' -> [2,'U']
				moves.append([int(char), str(prev)]) 
			else:
				prev = char
		for step in moves:
			rotations = step[0]
			face = step[1]
			if rotations is 1:
				self.rotate_90(face)
			elif rotations is 2:
				self.rotate_180(face)
			elif rotations is 3:
				self.rotate_180(face)
				self.rotate_90(face)
		print "SOLVED!"
	
	def test(self):
		test_solution = "U1U3 D1D3 R1R3 L1L3 F1F3"
		print "Testing robot. Test pattern:", test_solution
		self.solve(test_solution)
		

				

#  Some rules:
#	* there are 24 possible orientations
#	* After every move the claw needs to go to the home position
#		* This could be optimized to be one function
#	* A rotation is always counter clockwise to that face
#	* We should do an analyis; I am willing to bet that, for example, R
#	and R' moves may together be more common than R3, so the motors maybe
#	should be mounted like this: | (0) (home position)
#	                      (90) --+
#	                             | (180)
#
#	rather than like this:  | (90) (home position)
#	                  (0) --+-- (180)




								
def main():	
	pins = [12,11,10,9]
	positions = [0, 90, 180, 70, 10,
				 0, 90, 180, 95, 45]
	robot = arduino.Robot('/dev/ttyACM0', pins, positions)		
	robot.test()
	return 0

if __name__ == '__main__':
	main()

#
# Dear maintainer:
# 
# Once you are done trying to 'optimize' this routine,
# and have realized what a terrible mistake that was,
# please increment the following counter as a warning
# to the next guy:
# 
# total_hours_wasted_here = 16
