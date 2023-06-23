import serial

baud = 115200
ser = serial.Serial('/dev/ttyACM0', baud)

ser.close()
ser.open()

while True:
    try:
        data = ser.readline().decode().strip()
        print(data)
    except KeyboardInterrupt:
        break    
    
    
# Close the serial port    
ser.close()