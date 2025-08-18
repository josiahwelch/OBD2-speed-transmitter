#!/bin/python3 from pyobd.obd_io import OBDConnection

import os
import pyobd.modified_obd_io
PORT = 3

connection = OBDConnection(PORT, 'AUTO', 1000, 5, False)