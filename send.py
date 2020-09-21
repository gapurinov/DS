from threading import Thread
import sys, os
import socket


def send_file(name, addr, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a_socket:
        a_socket.connect((addr, port))
        temp1 = len(name).to_bytes(1, 'big')
        a_socket.sendall(temp1)
        temp2 = str(name).encode()
        a_socket.sendall(temp2)
        cur = os.path.getsize(name)
        cnt = 0
        with open(name, "rb") as fl:
            var = 1
            while var == 1:
                print((cnt / cur) * 100, "%")
                b = fl.read(1024)
                if not b:
                    break
                a_socket.sendall(b)
                cnt = cnt + len(b)
        print("DONE")


if __name__ == "__main__":
    file = sys.argv[1]
    addr = sys.argv[2]
    port = int(sys.argv[3])
    th = Thread(target=send_file, args=(file, addr, port))
    th.start()
    th.join()
    print("Exit")