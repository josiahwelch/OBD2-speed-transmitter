#!/bin/python3

# Josiah Welch
# 8/18/2025
# OBD-ii speed transmitter for NU-ROVE

from serial import Serial
from time import sleep
from obd_ii_reader import OBD2SpeedGet

class OBD2SpeedTransmitter:
    def __init__(self, com_port, baudrate=9600, timeout=0.5):
        self.ser = Serial(port=str(com_port), baudrate=baudrate, timeout=timeout)
        self.obd2_speed_get = OBD2SpeedGet()

    def send_speed(self):
        self.ser.write((self.obd2_speed_get.get_speed_str() + '\n').encode())

def __main__():
    transmitter = OBD2SpeedTransmitter("/dev/ttyUSB0")
    while True:
        transmitter.send_speed();
        sleep(0.1);

if __name__ == "__main__":
    __main__()
