import bluetooth

bd_addr = "00:14:03:05:59:38"  
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

print("Connected to Bluetooth module!")

while True:
    cmd = input("Enter command (F/B/L/R/S): ").upper()  
    if cmd in ["F", "B", "L", "R", "S"]:
        sock.send(cmd)
    elif cmd == "Q":
        print("Exiting...")
        break

sock.close()

