#!/bin/python3

from obd.obd import OBD
from obd.commands import Commands

class OBD2SpeedGet:
	def __init__():
		obd = OBD()
		commands = Commands()

	def get_speed(self):
		speed = float(str(connection.query(commands.SPEED).value).split(' ')[0])
		return speed
