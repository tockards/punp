#!/usr/bin/python
import sys
import socket 
import time 

def main():
    """a  blocking iterative NTP server 
    """
    
    try:
        listenfd  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as exc:
        sys.exit("socket error %s" % exc)

    try:
        listenfd.bind(("0.0.0.0", 13))
    except Exception as exc:
        sys.exit("bind  error %s" % exc)

    listenfd.listen(1)
    
    while True:
        conn, addr = listenfd.accept()
        data = "{}".format(time.ctime())
        conn.sendall(data)
        conn.close()
if __name__ == "__main__":
    
    main()

