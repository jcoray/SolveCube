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
#
#	The claws are mounted like this: | (0) (home position)
#	                          (90) --+
#	                                 | (180)
	

from pyfirmata import Arduino, util
#  https://media.readthedocs.org/pdf/pyfirmata/latest/pyfirmata.pdf
import sys
import time

class Cube(object):
	def __init__(self):
		self.orient = {'D':'D', 'F':'F', 'R':'R', 'B':'B', 'L':'L', 'U':'U'} # TODO Does this really need to be it's own class?

class Claw(object):
	def __init__(self, arduino, wrist_pin, hand_pin, positions, hand_delay, quarter_turn_delay):
		#  Configure Arduino
		arduino.servo_config(wrist_pin, 1000, 2000, 90) #  (pin, min micro, max micro, center deg)
		arduino.servo_config(hand_pin, 1000, 2000, 90)
		self.wrist = arduino.digital[wrist_pin]
		self.hand = arduino.digital[hand_pin]
		#  Positions (degrees)
		self.home_turn_deg = positions[0]  
		self.quarter_turn_deg = positions[1]
		self.half_turn_deg = positions[2]
		self.open_hand_deg = positions[3]
		self.close_hand_deg = positions[4]
		#  Delays (seconds)
		self.quarter_turn_delay = quarter_turn_delay
		self.half_turn_delay = quarter_turn_delay * 2
		self.hand_delay = hand_delay
		#  Current Orientation 
		#self.wrist_position = o
	def home_turn(self):
		self.wrist.write(self.home_turn_deg)
		#  TODO the home turn could either be a half or quarter turn 
		#  It would be best to optimize it to know the delay
		time.sleep(self.half_turn_delay)
	def quarter_turn(self):
		self.wrist.write(self.quarter_turn_deg)
		time.sleep(self.quarter_turn_delay)
	def half_turn(self):
		self.wrist.write(self.half_turn_deg)
		time.sleep(self.half_turn_delay)

	def open_hand(self):
		self.hand.write(self.open_hand_deg)
		time.sleep(self.hand_delay)
		
	def close_hand(self):
		self.hand.write(self.close_hand_deg)
		time.sleep(self.hand_delay)
		
class Robot(object):
	def __init__(self, serial_port, pins, positions, hand_delay=.25, quarter_turn_delay=.5):
		sys.stdout.write("Connecting to Arduino... ") #  Print w/o \n
		#  On Linux machines the serial port will be similar 
		#  to '/dev/ttyACM'. Open up a terminal window and type:
		#      $_  ls /dev | grep ttyACM 
		#  to list devices. One of these should be your Arduino.
		arduino = Arduino(serial_port)
		print "Done."
		print "Configuring Arduino..."
		iterator = util.Iterator(arduino)
		iterator.start()
		sys.stdout.write("    Configuring down_claw... ") #  Print w/o \n
		self.claw_down = Claw(arduino, pins[0], pins[1], positions[0:5], hand_delay, quarter_turn_delay)
		print "Done."
		sys.stdout.write("    Configuring up_claw... ") #  Print w/o \n
		self.claw_right = Claw(arduino, pins[2], pins[3], positions[5:10], hand_delay, quarter_turn_delay)
		print "Done."
		print "Configured."
		self.cube = Cube()
		#  Open the claws and put them in the correct orientation without a delay
		self.claw_down.wrist.write(self.claw_down.home_turn_deg)
		self.claw_down.hand.write(self.claw_down.open_hand_deg)
		self.claw_right.wrist.write(self.claw_right.home_turn_deg)
		self.claw_right.hand.write(self.claw_right.open_hand_deg)
		
	def find_orient(self, face):
		face_orient = ''
		for orient in self.cube.orient.keys():
			if face is self.cube.orient[orient]:
				face_orient = orient
				break
		return face_orient
		
	def rotate_90(self, face): 
		face_orient = self.find_orient(face)
		print "90* turn of", face, "Face orientation", face_orient, '\n' #  TODO remove after debug
		buffer_orient = self.cube.orient
		if face_orient is 'D': 
			self.claw_down.quarter_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			#  Because the face is already in claw_down, the robot
			#  does not need rotate the cube to turn the face. 
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
			buffer_orient['D'] = self.cube.orient['D'] #  The face in the claw does not move
			buffer_orient['F'] = self.cube.orient['L']
			buffer_orient['R'] = self.cube.orient['F'] 
			buffer_orient['B'] = self.cube.orient['R']
			buffer_orient['L'] = self.cube.orient['B'] 
 			buffer_orient['U'] = self.cube.orient['U'] 
		elif face_orient is 'R':
			self.claw_right.quarter_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
			#  Because the face is already in claw_right, the robot
			#  does not need rotate the cube to turn the face. 
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
			buffer_orient['D'] = self.cube.orient['B'] 
			buffer_orient['F'] = self.cube.orient['D']
			buffer_orient['R'] = self.cube.orient['R'] #  The face in the claw does not move
			buffer_orient['B'] = self.cube.orient['U'] 
			buffer_orient['L'] = self.cube.orient['L'] 
 			buffer_orient['U'] = self.cube.orient['F'] 
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
			buffer_orient['D'] = self.cube.orient['D'] #  The face in the claw does not move
			buffer_orient['F'] = self.cube.orient['B'] 
			buffer_orient['R'] = self.cube.orient['L'] 
			buffer_orient['B'] = self.cube.orient['F'] 
			buffer_orient['L'] = self.cube.orient['R']
 			buffer_orient['U'] = self.cube.orient['U']
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
			buffer_orient['D'] = self.cube.orient['U'] #  The face in the claw does not move
			buffer_orient['F'] = self.cube.orient['B'] #  L -> F
			buffer_orient['R'] = self.cube.orient['R'] #  F -> R
			buffer_orient['B'] = self.cube.orient['F'] #  R -> B
			buffer_orient['L'] = self.cube.orient['L'] #  B -> L
 			buffer_orient['U'] = self.cube.orient['D']
		self.cube.orient = buffer_orient #  Update the orientation.
		return self.cube.orient 
		
	def rotate_180(self, face): 
		face_orient = self.find_orient(face)
		print "180* turn of", face, "Face orientation", face_orient, '\n' #  TODO remove after debug
		buffer_orient = self.cube.orient
		if face_orient is 'D': #  Face held in claw_down
			self.claw_down.half_turn()
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
			self.claw_right.half_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
			buffer_orient['D'] = self.cube.orient['D'] #  The face in the claw does not move
			buffer_orient['F'] = self.cube.orient['L']
			buffer_orient['R'] = self.cube.orient['F'] 
			buffer_orient['B'] = self.cube.orient['R']
			buffer_orient['L'] = self.cube.orient['B'] 
 			buffer_orient['U'] = self.cube.orient['U'] 
		elif face_orient is 'R': #  Face held in claw_right
			self.claw_right.half_turn()
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
			self.claw_down.half_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			buffer_orient['D'] = self.cube.orient['B'] 
			buffer_orient['F'] = self.cube.orient['D']
			buffer_orient['R'] = self.cube.orient['R'] #  The face in the claw does not move
			buffer_orient['B'] = self.cube.orient['U'] 
			buffer_orient['L'] = self.cube.orient['L'] 
 			buffer_orient['U'] = self.cube.orient['F'] 
		elif face_orient is 'L':
			self.claw_right.open_hand()
			self.claw_down.half_turn()
			self.claw_right.close_hand()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			self.claw_right.half_turn()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
			buffer_orient['D'] = self.cube.orient['D'] #  The face in the claw does not move
			buffer_orient['F'] = self.cube.orient['B'] 
			buffer_orient['R'] = self.cube.orient['L'] 
			buffer_orient['B'] = self.cube.orient['F'] 
			buffer_orient['L'] = self.cube.orient['R']
 			buffer_orient['U'] = self.cube.orient['U']
		elif face_orient is 'U':
			self.claw_down.open_hand()
			self.claw_right.half_turn()
			self.claw_down.close_hand()
			self.claw_right.open_hand()
			self.claw_right.home_turn()
			self.claw_right.close_hand()
			self.claw_down.half_turn()
			self.claw_down.open_hand()
			self.claw_down.home_turn()
			self.claw_down.close_hand()
			buffer_orient['D'] = self.cube.orient['U'] #  The face in the claw does not move
			buffer_orient['F'] = self.cube.orient['B'] #  L -> F
			buffer_orient['R'] = self.cube.orient['R'] #  F -> R
			buffer_orient['B'] = self.cube.orient['F'] #  R -> B
			buffer_orient['L'] = self.cube.orient['L'] #  B -> L
 			buffer_orient['U'] = self.cube.orient['D']
		self.cube.orient = buffer_orient #  Update the orientation.
		return self.cube.orient 

	def solve(self, solution):
		self.claw_right.hand.write(self.claw_right.close_hand_deg)
		self.claw_down.hand.write(self.claw_down.close_hand_deg)
		print "ready"
		time.sleep(2)
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
			print step
			rotations = step[0]
			face = step[1]
			if rotations is 1:
				print step, self.cube.orient
				self.rotate_90(face)
				print step, self.cube.orient
			elif rotations is 2:
				print step, self.cube.orient
				self.rotate_180(face)
				print step, self.cube.orient
			elif rotations is 3:
				print step, self.cube.orient
				self.rotate_180(face)
				print step, self.cube.orient
				self.rotate_90(face)
				print step, self.cube.orient
			print "SOLVED!"
		return 0
	
	def test(self):
		test_solution = 'L1L3'#" D1D3 U1U3 L1L3 R1R3 F1F3 B1B3"
		print "Testing robot. Test pattern:", test_solution
		self.solve(test_solution)

def main():	
	pins = [12,11,10,9]
	positions = [180, 96, 10, 70, 10,
				 180, 100, 25, 95, 45]
	robot = Robot('/dev/ttyACM5', pins, positions)		
	print "setup done"
	robot.test()
	return 0 #  TODO it does not exit (niether sys.exit(0) nor exit(0) work)

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
# total_hours_wasted_here = 22
