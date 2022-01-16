import bluetooth
import lighton
import json
from threading import Thread
from time import sleep

# end of message text
EOM = "\n"
EOL = "endloop"


def init():
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    sock.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)
    sock.bind(("", port))
    sock.listen(1)

    while True:
        openSock(sock)


def readData(client_sock):
    data = ""
    while EOM not in data and EOL not in data:
        data += client_sock.recv(1024)
    return data


current_action = ""
rainbow = "rainbow"
main = "main"
sizes_req = "sizes"
indexes_req = "index"


# setup client
def openSock(sock):
    client_sock, address = sock.accept()

    print (address)

    try:
        data = ""
        while EOL not in data:
            data = readData(client_sock)
            print (data)

            if sizes_req in data:
                sizes = str(lighton.LED_MATRIX_HEIGHT) + "," + str(lighton.LED_MATRIX_WIDTH) + EOM
                client_sock.send(sizes)
                print ("Data sent: " + sizes)
            elif indexes_req in data:
                cleared = ''.join(c for c in data if c.isdigit() or c is ' ')
                print("cleared " + cleared)
                indexes = list(map(int, cleared.strip(indexes_req).split()))
                print ("result", indexes)
                lighton.lightOn(indexes)
        print ("oops")
    except bluetooth.btcommon.BluetoothError, KeyboardInterrupt:
        print ("err")

    finally:
        close(sock, client_sock)
        print ("The end")


def close(sock, client_sock):
    client_sock.close()
    sock.close()
