import socket
import json
import time


SERVER = 'localhost'
PORT = 1602


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

password = input('Введите пароль : \n')
server.connect((SERVER, PORT))



try:
    str_password = str(password)
    byte_password = str_password.encode()
    server.send(byte_password)
    time.sleep(1)
except Exception as err:
    print('connection error : ', err)
try:
    response = server.recv(1024)
    str_response = response.decode()
    print(str_response)
except Exception as err:
    print('connection error : ', err)
    

