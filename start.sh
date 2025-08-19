#!/bin/sh
echo "OBD-ii transmitter starting...\n\n\n"
sleep 3
exec /home/pi/git/OBD2-speed-transmitter/obd2_speed_transmitter.py
