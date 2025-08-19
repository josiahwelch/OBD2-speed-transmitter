#!/bin/python3

import pyserial

class OBD2SpeedTransmitter:
	__init__(com_port, baudrate=9600, timeout=0.5):
        self.ser = Serial(port=com_port, baudrate, timeout)
