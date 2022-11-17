import sys
import socket
import threading
import time

usg1 = "python NetworkScanner.py <TARGET> <START_PORT> <END_PORT>"  # scan_1
usg2 = "python NetworkScanner.py <TARGET> <PORT>"  # scan_2
usg3 = "python NetworkScanner.py <TARGET>"  # scan_3

print(" ██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗██╗   ██╗    ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗███╗   ██╗ ██████╗   ")
print(" ██╔══██╗██║   ██║████╗  ██║████╗  ██║╚██╗ ██╔╝    ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║████╗  ██║██╔════╝   ")
print(" ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║ ╚████╔╝     ██║███████╗    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║██║██╔██╗ ██║██║  ███╗  ")
print(" ██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║  ╚██╔╝      ██║╚════██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██║██║╚██╗██║██║   ██║  ")
print(" ██████╔╝╚██████╔╝██║ ╚████║██║ ╚████║   ██║       ██║███████║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║██║ ╚████║╚██████╔╝  ")
print(" ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝       ╚═╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝   ")


def ScanPortInRange():  # scanning in range,given by the user
    start_time = time.time()

    if len(sys.argv) != 4:
        print(usg1)
        sys.exit()

    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Error Occurred")
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


def ScanAllPorts():  # all ports are scanned
    start_time = time.time()

    if len(sys.argv) != 2:
        print(usg3)
        sys.exit()

    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Error Occurred")
        sys.exit()

    start_port = 1
    end_port = 65535

    print("Target: {}".format(target))

    print("scanning process is started...")

    def scan_port_2(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        con = s.connect_ex((target, port))
        if not con:
            print("[#] Port is open {}".format(port))
        s.close()

    for Port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port_2, args=(Port,))
        t.start()
    end_time = time.time()
    print("Time Taken: ", end_time - start_time)

    sys.exit()


def ScanOnePort():
    start_time = time.time()

    if len(sys.argv) != 3:
        print(usg2)
        sys.exit()

    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Error Occurred")
        sys.exit()

    print("Target: {}".format(target))

    print("scanning process is started...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.5)
    con = s.connect_ex((target, int(sys.argv[2])))
    if not con:
        print("[#] Port is open {}".format(sys.argv[2]))
    else:
        print("[#] Port is closed".format(sys.argv[2]))
    s.close()

    end_time = time.time()
    print("Time Taken: ", end_time - start_time)

    sys.exit()


while True:
    if len(sys.argv) == 4:
        ScanPortInRange()
    elif len(sys.argv) == 2:
        ScanAllPorts()
    elif len(sys.argv) == 3:
        ScanOnePort()
    else:
        print("Format: " + usg1)
        print("Format: " + usg2)
        print("Format: " + usg3)
        break
