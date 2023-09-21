import sys
import socket
from datetime import datetime
import concurrent.futures
import time

target = socket.gethostbyname("192.168.1.1")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


def check_port(port):
    # if str(port).startswith("80"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))
    if result == 0:
        return "Port {} is open".format(port)

    s.close()
    return port


before = time.time()

try:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ports = list(range(1, 65536))
        results = executor.map(check_port, ports, chunksize=15)
        for result in results:
            print(result)

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()

after = time.time()

print('Duration: {}s'.format(round(after - before, 2)))

# datetime.time(second=int(after - before))
