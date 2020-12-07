import socket
import select
HEADER_LENGTH = 10
IP="127.0.0.1"
PORT=1234
# AF = Address Family
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ALLOWS TO RE CONNECT
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((IP,PORT))
server_socket.listen()
socket_list = [server_socket]
