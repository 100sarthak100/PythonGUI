import threading
import serial
port = "\\\\.\\COM32"
baud = 38400

connected = False

#serial_port = serial.Serial(port, baud, timeout=1)
serial_port = serial.Serial(port, baud, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0)

def handle_data(data):
    x=1
    print(data, end='')
    #print(data)

def read_from_port(ser):
    connected = False
    while not connected:
        #serin = ser.read()
        connected = True
        serial_port.write(b"dfsdgsfgfgsdg")

        record = {}
        lst = ['a', 'b', 'c']
        while True:
            k = serial_port.readline().decode()

            if k == '':
                break
            try:
                if k == "b'C":
                    pass
                else:
                    record[lst.pop(0)] = k.strip('\r\n')
            except IndexError:
                pass
            print(record)




thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()