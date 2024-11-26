# script to test for buffer overflows using random characters, you can change it to use a single character too
import socket
import random
import string

size = 1

def gen_payload():
    global size
    chars = string.ascii_letters + string.digits + "!@#$%¨&*()-_+=<>,.:;?çÇ/\|'[{]}"    # group of symbols that will be used
    rnd = random.SystemRandom()	# module to use the SO to generate a random choice
    payload = (''.join(rnd.choice(chars) for i in range(size)))
    size += 100
    return payload

def attack_socket(payload, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.recv(1024)
    s.send(f"{payload}\r\n")
    s.recv(1024)

while size < 1000:
    p = gen_payload()
    print(f"Testing payload (size={len(p)}) -> {p}")
    attack_socket(p, "192.168.0.1", 80)

