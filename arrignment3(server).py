## server.py

import socket
import argparse
import os


def run_server(port):
    host = 'localhost'
  
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s: 
        s.bind((host, port))
        s.listen(1)   
        conn, addr = s.accept()

        print("client connected ...",addr)

        filename=conn.recv(1024).decode()
        print(filename)

        filesize = os.path.getsize(filename)
        print(filesize)

        f=open(filename,'rb')
        data = f.read()
        f.flush()

        conn.sendall(data)


        conn.close()

#def serch(directory,filename):
#    filenames = os.listdir(directory)
#    for i in filenames: 
#        if i == filename :
#            want_filename = os.path.join(directory,filename)
#            print("filename : ", want_filename)

run_server(1004)

