# Josiah Welch
# 8/18/2025
# OBD-ii speed getter for NU-ROVE

from obd.obd import OBD
from obd.commands import Commands

class OBD2SpeedGet:
	def __init__(self):
		obd = OBD()
		commands = Commands()

	def get_speed_str(self):
		speed = str(obd.query(commands.SPEED).value).split(' ')[0]
		return speed

	def get_speed(self):
		speed = float(self.get_speed_str())
		return speed
