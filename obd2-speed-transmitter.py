#!/bin/python3

import pyserial
import time
from obd-ii-reader import OBD2SpeedGet

class OBD2SpeedTransmitter:
	__init__(com_port, baudrate=9600, timeout=0.5):
        self.ser = Serial(port=com_port, baudrate, timeout)
        self.obd2_speed_get = OBD2SpeedGet()

    def send_speed():
        self.ser.write(self.get_speed_str() + '\n')

def __main__:
    transmitter = OBD2SpeedTransmitter("/dev/ttyUSB0")
    while True:
        transmitter.send_speed();
        sleep(0.1);

if __name__ == "__main__":
    __main__()
