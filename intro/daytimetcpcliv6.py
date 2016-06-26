#!/usr/bin/python
import sys
import socket 

def main():
    """Queries an NTP server and gets the time from it

    """
    if len(sys.argv) != 2:
        sys.exit("usage: daytimetcpcli.py  <IPaddress>")

    try:
        sockfd  = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    except Exception as exc:
        sys.exit("socket error %s" % exc)

    try:
        sockfd.connect((sys.argv[1], 13))
    except Exception as exc:
        sys.exit("connection error %s" % exc)

   
    lines = []
    while True:
        line = sockfd.recv(1024)
        if not line:
            break
        lines.append(line)
    recvline = ''.join(lines).strip()

    if len(recvline) > 0:
        print (recvline)
    else:
        sys.exit("read error")
if __name__ == "__main__":
    
    main()

