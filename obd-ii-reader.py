#!/bin/python3

from obd.obd import OBD
from obd.commands import Commands

connection = OBD()
commands = Commands()

while True:
	print(connection.query(commands.SPEED.decode))
