## client.py

import socket
import argparse
import os

def run(host, port, filename):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

#        filename = "text.txt"
        s.sendall(filename.encode())

        print("filename = ", filename)

        data=s.recv(1024)
        print("size : ",len(data))

        f=open(filename,'w')
        f.write(data.decode())
        f.flush()
    
        
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host -f filename")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)
    parser.add_argument('-f', help="fail_name", required=True)

    args = parser.parse_args()
    run(host=args.i, port=int(args.p), filename=args.f)
