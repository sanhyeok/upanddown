## server.py

import socket
import argparse


def run_server(port):
    host = '' ## 172.30.1.6 Loopback
  
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:##try finaly를 시용하면 문제가생겨도 close()가 된다!, family,type은 기본으로 설정 
        s.bind((host, port))##bind를 하기위해선 호스트와 포트번호가 필요하다
        s.listen(1) ## max 1 client 말그대로 접속시도를 알아채는것

        conn, addr = s.accept()##접속의 개시
        msg = conn.recv(1024)##소켓으로부터 데이터 받기
        print(msg.decode()) ## msg is a binary data, so we need to decode it

        poot = msg.decode()
        poot = poot[::-1]
        msg = poot.encode()

        conn.sendall(msg)##다시 메세지 보냄
        conn.close()##소켓 닫


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port")#인자 받기!
    parser.add_argument('-p', help="port_number", required=True)#p=portnumber

    args = parser.parse_args()
    run_server(port=int(args.p))

'''
try:
    s=socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    print("소켓 생성")
except socket.error as err:
    print("에러발생:%s"%(err))

host=''
port=9090
s.bind((host,port))
s.listen(1)
print("%d포트에서 연결 대기중"%(port))
while True:
    c, addr = s.accept()
    print(addr,"에서 사용자 접속")
    c.send(msg)
    c.close()'''
