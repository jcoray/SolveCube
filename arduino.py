#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Solution.py
#  
#  Copyright 2015 Gabriel Norris  <>
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

print "Connecting to Arduino..."
arduino = Arduino('/dev/ttyACM0')
print "Connection extablished."


iter8 = util.Iterator(arduino)
iter8.start()

print "Setting up servos..."
arduino.servo_config(12, 1000, 2000, 90)
arduino.servo_config(11, 1000, 2000, 90)
arduino.servo_config(10, 1000, 2000, 90)
arduino.servo_config(9,  1000, 2000, 90)
arduino.digital[12].mode = SERVO
arduino.digital[11].mode = SERVO
arduino.digital[10].mode = SERVO
arduino.digital[9].mode = SERVO
OCServo1 = arduino.digital[12]
RServo1 = arduino.digital[11]
OCServo2 = arduino.digital[10]
RServo2 = arduino.digital[9]
print "Ready to solve."

OS1 = 70
CS1 = 10
OS2 = 95
CS2 = 10
RS1 = 0
ARS1 = 180
RS2 = 0
ARS2 = 180

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

	
def U1():
	#  Rotate so that this face is in one of the claws
	OCServo1.write(OS1)
	time.sleep(.5)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	#  close servo
	#  rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#  Return side to original position
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
def U2():
	#Rotate so that this face is in one of the claws
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
def U3():
	#Rotate so that this face is in one of the claws
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #3
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
def F1():
	#Rotate so that this face is in one of the claws
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	#rotate side prescribed number of times
	RServo2.write(RS1) #1
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	#Return side to original position
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
def F2():
	#Rotate so that this face is in one of the claws
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	#rotate side prescribed number of times
	RServo2.write(RS1) #1
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	RServo2.write(RS1) #2
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	#Return side to original position
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
def F3():
	#Rotate so that this face is in one of the claws
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	#rotate side prescribed number of times
	RServo2.write(RS1) #1
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	RServo2.write(RS1) #2
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	RServo2.write(RS1) #3
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	#Return side to original position?
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo.write(ARS1)
	OCServo.write(CS1)
def R1():
	#rotate side prescribed number of times
	RServo2.write(RS1) #1
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
def R2():
	#Rotate so that this face is in one of the claws
	#close servo
	#rotate side prescribed number of times
	RServo2.write(RS1) #1
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	RServo2.write(RS1) #2
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	#Return side to original position?
def R3():
	#rotate side prescribed number of times
	RServo2.write(RS1) #1
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	RServo2.write(RS1) #2
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	RServo2.write(RS1) #3
	OCServo2.write(OS1)
	RServo2.write(ARS1)
	OCServo2.write(CS1)
	#Return side to original position?
def B1():
	#Rotate so that this face is in one of the claws
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position?
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
def B2():
	#Rotate so that this face is in one of the claws
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
def B3():
	#Rotate so that this face is in one of the claws
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #3
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo2.write(RS2)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo2.write(ARS2)
	OCServo2.write(CS2)
def L1():
	#Rotate so that this face is in one of the claws
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
def L2():
	#Rotate so that this face is in one of the claws
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
def L3():
	#Rotate so that this face is in one of the claws
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #3
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	OCServo2.write(OS2)
	RServo1.write(RS1)
	OCServo2.write(CS2)
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
def D1():
	#Rotate so that this face is in one of the claws
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position?
def D2():
	#Rotate so that this face is in one of the claws
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position?
def D3():
	#Rotate so that this face is in one of the claws
	#close servo
	#rotate side prescribed number of times
	RServo1.write(RS1) #1
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #2
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	RServo1.write(RS1) #3
	OCServo1.write(OS1)
	RServo1.write(ARS1)
	OCServo1.write(CS1)
	#Return side to original position?
	
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
# total_hours_wasted_here = 5
# 
