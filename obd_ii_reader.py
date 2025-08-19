#!/bin/python3

from obd.obd import OBD
from obd.commands import Commands

class OBD2SpeedGet:
	def __init__(self):
		obd = OBD()
		commands = Commands()

	def get_speed_str(self):
		speed = str(connection.query(commands.SPEED).value).split(' ')[0]
		return speed

	def get_speed(self):
		speed = float(get_speed_str())
		return speed
