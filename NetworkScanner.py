import sys
import socket
import threading
import time

usg1 = "python NetworkScanner.py <TARGET> <START_PORT> <END_PORT>"  # scan_1
usg2 = "python NetworkScanner.py <TARGET> <PORT>"  # scan_2
usg3 = "python NetworkScanner.py <TARGET>"  # scan_3


def scanPortINRange():  # scanning in range,given by the user
    start_time = time.time()

    if len(sys.argv) != 4:
        print(usg1)
        sys.exit()

    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Error")
        sys.exit()

    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    print("Target: {}".format(target))

    print("scanning process is started...")

    # scanning port
    def scan_port_1(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        con = s.connect_ex((target, port))
        if not con:
            print("[#] Port is open {}".format(port))
        s.close()

    for Port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port_1, args=(Port,))
        t.start()
    end_time = time.time()
    print("Time Taken: ", end_time - start_time)

    sys.exit()

def ScanAllPorts():
    print("hi")
