import serial
import time
import os
serial_port = '/dev/ttyUSB0'
baud_rate = 9600
write_to_file_path = "output.txt"
output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
count = 0
while True:
	line = ser.readline()
	line = line.decode("utf-8")
	print(line)
	output_file = open(write_to_file_path, "a")
	output_file.write(line)
	output_file.close()
	


