#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Solution.py
#  
<<<<<<< HEAD
#  Copyright 2015 Gabriel Norris <
=======
#  Copyright 2015 Gabriel Norris  <>
>>>>>>> 0cf5fd808f484f6a0763b55ed556a1b3474a467c
#                 Jakob Coray <jakob2016@gmail.com>
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
		self.orient = ['D', 'F', 'R', 'B', 'L', 'T',]
	def rotate_90(self,):
		#  always rotates clockwise
		if self.holds_face = 'D':
			
		if self.holds_face = 'R': # TODO correct this one
			buffer_orient[0] = self.cube.orient[0] #  The face in the claw does not move
			buffer_orient[1] = self.cube.orient[4] #  L -> F
			buffer_orient[2] = self.cube.orient[1] #  F -> R
			buffer_orient[3] = self.cube.orient[2] #  R -> B
			buffer_orient[4] = self.cube.orient[3] #  B -> L
			buffer_orient[5] = self.cube.orient[5] #  Top does not move

class Claw(object):
	def __init__(self, arduino, wrist_pin, hand_pin, positions, delays):
		arduino.servo_config(wrist_pin, 1000, 2000, 90) 
		arduino.servo_config(hand_pin, 1000, 2000, 90)
		self.wrist = arduino.digital[wrist_pin]
		self.hand = arduino.digital[hand_pin]
		
		self.home_turn_deg = positions[0]
		self.quarter_turn_deg = positions[1]
		self.half_turn_deg = positions[2]
		self.open_hand_deg = positions[3]
		self.close_hand_deg = positions[4]
		
		self.quarter_turn_delay = delays[0]
		self.half_turn_delay = delays[0] * 2
		self.hand_delay = delays[1] 
		
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
	def __init__(self, serial_port, pins, positions):
		sys.stdout.write("Connecting to Arduino...")
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
		self.claw_down = Claw(arduino, pins[0], pins[1], positions[0:4], delay[0:1])
		print "Done."
		sys.stdout.write("    Configuring up_claw... ") #  Print w/o \n
		self.claw_down = Claw(arduino, pins[2], pins[3], positions[5:9], delay[2:3])
		print "Done."
		print "Configured."

		OS1 = 70 #  Degrees
		CS1 = 40 # max 10 Degrees
		OS2 = 95 #  Degrees
		CS2 = 65 # max 10 Degrees
		RS1 = 0 #  Degrees
		ARS1 = 180 #  Degrees
		RS2 = 0 #  Degrees
		ARS2 = 180 #  Degrees
		OCDelay = .25 #  Seconds
		RDelay = .5 #  Seconds
	def rotate_90(face):
		buffer_orient = []
		#                                 C1   #    C2   #    #    #
		for orient, iiface in enumerate():
			if face = iiface:
				face_orient = orient
		
		if face_orient is 0: #  Face held in claw_down
			self.claw_down.wrist.write(self.claw_down.quarter_turn)
			time.sleep(self.quarter_turn_delay)
			self.claw_down.hand.write(self.claw_down.open_hand)
			time.sleep(self.hand_delay)
			self.claw_down.wrist.write(self.claw_down.home_turn)
			time.sleep(self.quarter_turn_delay)
			self.claw_down.hand.write(self.claw_down.close_hand)
			time.sleep(self.hand_delay)
			
			buffer_orient[0] = self.cube.orient[0] #  The face in the claw does not move
			buffer_orient[1] = self.cube.orient[4] #  L -> F
			buffer_orient[2] = self.cube.orient[1] #  F -> R
			buffer_orient[3] = self.cube.orient[2] #  R -> B
			buffer_orient[4] = self.cube.orient[3] #  B -> L
			buffer_orient[5] = self.cube.orient[5] #  Top does not move
		elif face_orient is 1: 
			rotate claw2
		elif face_orient is 2:
		elif face_orient is 3:
		elif face_orient is 4:
		elif face_orient is 5:
		
		#  Update the orientation. 
		for ii_orient, ii_face in enumerate(buffer_orient);
			self.cube.orient[ii_orient] = ii_face
		return self.cube.orient

	def U1(self, ):
		
		#  Rotate so that this face is in one of the claws
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#  close servo
		#  rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#  Return side to original position
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def U2():
		#Rotate so that this face is in one of the claws
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def U3():
		#Rotate so that this face is in one of the claws
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #3
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def F1():
		#Rotate so that this face is in one of the claws
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1) ; time.sleep(RDelay)
		OCServo1.write(CS1) ; time.sleep(OCDelay)
		#rotate side prescribed number of times
		RServo2.write(RS1) ; time.sleep(RDelay) #1
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#Return side to original position
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
	def F2():
		#Rotate so that this face is in one of the claws
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		#rotate side prescribed number of times
		RServo2.write(RS1) ; time.sleep(RDelay) #1
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		RServo2.write(RS1) ; time.sleep(RDelay) #2
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#Return side to original position
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1) ; time.sleep(RDelay)
		OCServo1.write(CS1) ; time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1) ; time.sleep(RDelay)
		OCServo1.write(CS1) ; time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1) ; time.sleep(RDelay)
		OCServo1.write(CS1) ; time.sleep(OCDelay)
	def F3():
		#Rotate so that this face is in one of the claws
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		#rotate side prescribed number of times
		RServo2.write(RS1) ; time.sleep(RDelay) #1
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		RServo2.write(RS1) ; time.sleep(RDelay) #2
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		RServo2.write(RS1) ; time.sleep(RDelay) #3
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#Return side to original position?
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1) ; time.sleep(RDelay)
		OCServo1.write(CS1) ; time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1); time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1) ; time.sleep(RDelay)
		OCServo1.write(CS1) ; time.sleep(OCDelay)
	def R1():
		#rotate side prescribed number of times
		RServo2.write(RS1) ; time.sleep(RDelay) #1
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def R2():
		#Rotate so that this face is in one of the claws
		#close servo
		#rotate side prescribed number of times
		RServo2.write(RS1) ; time.sleep(RDelay) #1
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		RServo2.write(RS1) ; time.sleep(RDelay) #2
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#Return side to original position?
	def R3():
		#rotate side prescribed number of times
		RServo2.write(RS1) ; time.sleep(RDelay) #1
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		RServo2.write(RS1) ; time.sleep(RDelay) #2
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		RServo2.write(RS1) ; time.sleep(RDelay) #3
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS1); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#Return side to original position?
	def B1():
		#Rotate so that this face is in one of the claws
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position?
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def B2():
		#Rotate so that this face is in one of the claws
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def B3():
		#Rotate so that this face is in one of the claws
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #3
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo2.write(RS2) ; time.sleep(RDelay)
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo2.write(ARS2); time.sleep(RDelay) #
		OCServo2.write(CS2); time.sleep(OCDelay)
	def L1():
		#Rotate so that this face is in one of the claws
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
	def L2():
		#Rotate so that this face is in one of the claws
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
	def L3():
		#Rotate so that this face is in one of the claws
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #3
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		OCServo2.write(OS2); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay)
		OCServo2.write(CS2); time.sleep(OCDelay)
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
	def D1():
		#Rotate so that this face is in one of the claws
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position?
	def D2():
		#Rotate so that this face is in one of the claws
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position?
	def D3():
		#Rotate so that this face is in one of the claws
		#close servo
		#rotate side prescribed number of times
		RServo1.write(RS1) ; time.sleep(RDelay) #1
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #2
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		RServo1.write(RS1) ; time.sleep(RDelay) #3
		OCServo1.write(OS1); time.sleep(OCDelay)
		RServo1.write(ARS1); time.sleep(RDelay) #
		OCServo1.write(CS1); time.sleep(OCDelay)
		#Return side to original position?



#  Some rules:
#	* there are 24 possible orientations
#	* After every move the claw needs to go to the home position
#		* This could be optimized to be one function
#	* A rotation is always counter clockwise to that face
#	* We should do an analyis; I am willing to bet that, for example, R
#	and R moves may together be more common than R3, so the motors maybe
#	should be mounted like this: | (0) (home position)
#	                      (90) --+
#	                             | (180)
#
#	rather than like this:  | (90) (home position)
#	                  (0) --+-- (180)


def test():
	print 'U1'
	U1()	
	print "U2"
	U2()
	print "U3"
	U3()
	print "F1"
	F1()
	print "F2"
	F2()
	print "F3"
	F3()
	print "R1"
	R1()
	print "R2"
	R2()
	print "R3"
	R3()
	print "B1"
	B1()
	print "B2"
	B2()
	print "B3"
	B3()
	print "L1"
	L1()
	print "L2"
	L2()
	print "L3"
	L3()
	print "D1"
	D1()
	print "D2"
	D2()
	print "D3"
	D3()

def solve(solution):	
	prev = 0
	moves = []
	error_count = 0
	for i in solution:
		if i.isdigit():
			moves.append(str(prev) + str(i))
		else:
			prev = i
	for i in moves:
		#Identify the move in question
		#TODO Find less stupid way? (polymorphism)
		if i == "U1": 
			U1()		
		elif i == "U2":
			U2()
		elif i == "U3":
			U3()
		elif i == "F1":
			F1()
		elif i == "F2":
			F2()
		elif i == "F3":
			F3()
		elif i == "R1":
			R1()
		elif i == "R2":
			R2()
		elif i == "R3":
			R3()
		elif i == "B1":
			B1()
		elif i == "B2":
			B2()
		elif i == "B3":
			B3()
		elif i == "L1":
			L1()
		elif i == "L2":
			L2()
		elif i == "L3":
			L3()
		elif i == "D1":
			D1()
		elif i == "D2":
			D2()
		elif i == "D3":
			D3()
		else: 
			print "Error:", i, "is not a valid move."		
			error_count += 1		
	return error_count
								
def main():			
	while True:
		test()
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
# total_hours_wasted_here = 6
# 
