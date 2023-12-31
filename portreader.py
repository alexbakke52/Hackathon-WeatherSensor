import serial
import time


def get_data():    
    baud = 115200
    ser = serial.Serial('COM5', baud)

    timeout = time.time() + 10 #10 seconds into the future

    ser.close()

    temp_list = []

    ser.open()



    while True:
        try:
            data = ser.readline().decode().strip()
            temp_list.append(data)
        except KeyboardInterrupt:
            break    
        if time.time() > timeout:
            break
        
        
    # Close the serial port    
    ser.close()

    print(temp_list[:])

    return temp_list