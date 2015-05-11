# SolveCube
A fast Raspberry Pi and Arduino based Rubik's Cube solving robot.

Created by Gabriel Norris and Jakob Coray, with advisement from Clint Gibson
#### Software
- arduino.py - Controls the robotics
- cubecompo.cpp - Solves the cube
- cube.py - Serves as the glue between the various programs
- gui.py - Interface for entering the cube 

##### Dependencies
- Python 2.7.6
- Tkinter
- Pyfirmata '''pip install py
- Ardiuno IDE (tested on versions 1.0.5, 1.6.1, 1.6.3)

#### Hardware
- Arduino Uno R3
- Raspberry Pi 2 Model B
- Standard Servos (4)
- 3 Amp power supply 
- Claws (2) Designed by Kas of the Arduino forums <http://forum.arduino.cc/index.php?topic=271827.0>

## Installation Instructions
1. Download repository
2. Compile cubecompo.cpp: ```g++ cubecompo.cpp -o cubecompo```
3. Install tkinter ```sudo apt-get install python-tk```
4. Install pip ```sudo apt-get install python-pip```
5. Install pyfirmata ```sudo pip install pyfirmata```
6. Connect the Arduino via USB. See comments in arduino.py for details on setting the serial port.
7. Open the Arduino IDE and upload ServoFirmata.ino (File/Examples/Firmata/ServoFirmata). 
8. Run cube.py: ```./cube.py```
