import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostbyname(socket.gethostname()))
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(conn,addr):
     pass
def start():
       
print(" [STARTING] server is starting...")
start ( )