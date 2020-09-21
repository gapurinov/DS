import socket
import sys, os
from threading import Thread

def rename(name):
    if not os.path.exists(name):
        return name
    else:
        j = 1
        changed_name = name
        while os.path.exists(changed_name):
            cnt = str(j)
            if "." not in name:
                changed_name = temp + "_" + cnt
            else:
                temp = "".join(name.split(".")[:-1])
                e = name.split(".")[-1]
                changed_name = temp + "_" + cnt + "." + e
            j += 1
        return changed_name

def download_fl(con, addr):
    with con:
        print("From ", addr)
        sz = int.from_bytes(con.recv(1), 'big')
        name = rename((con.recv(sz)).decode())
        with open(name, "wb") as fl:
            var = 1
            while var == 1:
                x = con.recv(1024)
                if not x:
                    break
                fl.write(x)
        print(name, " was downloaded")

host = ""

if __name__ == "__main__":
    port_num = int(sys.argv[1])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a_socket:
        a_socket.bind((host, port_num))
        while True:
            a_socket.listen(1)
            con, addr = a_socket.accept()
            thread = Thread(target=download_fl, args=(con, addr))
            thread.start()