import serial
import list_ports

running = True

com = list_ports.serial_ports()
print(com)

'input port number'
port = input("Please enter port number(e.g COM8): ").upper()
'input bound rate'
bound_rate = int(input("Please enter bound rate(9600, 19200, 57600): "))
'input parity'
print("1. PARITY_NONE")
print("2. PARITY_EVEN")
print("3. PARITY_ODD")
num = int(input("Please select parity: "))
if num == 1: str = serial.PARITY_NONE
elif num == 2: str = serial.PARITY_EVEN
elif num == 3: str = serial.PARITY_ODD
else: str = serial.PARITY_NONE

ser = serial.Serial(port,bound_rate,parity=str,timeout=1)

while running:
    cmd = input("Please enter the command(or enter '0' to quit): ")
    if cmd == "0": break
    ser.write(cmd.encode())
    line = 0
    while True:
        res = ser.readline()
        print(res.decode())
        line +=1
        if len(res) == 0: break


print(line)
ser.close()







