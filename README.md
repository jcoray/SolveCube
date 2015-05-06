# SolveCube
A fast Raspberry Pi and Arduino based Rubik's Cube solving robot.

Created by Jakob Coray and Gabriel Norris.
#### Software
- arduino.py - Controls the robotics
- cubecompo.cpp - Solves the cube
- cube.py - Serves as the glue between the various programs
- gui.py - Interface for entering the cube 

#### Hardware
- Arduino Uno R3
- Raspberry Pi 2 Model B
- Standerd Servos (4)
- 3 Amp power supply 
- Claws (2) Designed by Kas of the Arduino forums <http://forum.arduino.cc/index.php?topic=271827.0>

## Installation Instructions
1. Download repository
2. Compile cubecompo.cpp: ```$_ g++ cubecompo.cpp -o cubecompo```
3. Run cube.py: ```$_ ./cube.py```
