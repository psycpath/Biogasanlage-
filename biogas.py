import serial

ser = serial.Serial('COM5')  # open serial port

ser.write(b'hello')     # write a strin

ser.close()             #close port