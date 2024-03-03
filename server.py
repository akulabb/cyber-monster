import socket
import json
import time
import pygame


SERVER = 'localhost'
PORT = 1602
ACTIVATION_PASSWORD = 'oni rezut'
IMAGE_PATH = 'CyberMonster.png'

pygame.init()
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((SERVER, PORT))
socket.listen()

def activate_monster():
    status = True
    screen = pygame.display.set_mode((512, 512))
    image = pygame.image.load(IMAGE_PATH)
    image = pygame.transform.scale(image, (512, 512))
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
                print('задача выполнена')
    pygame.quit()




while True:
    user_socket, address = socket.accept()
    try:
        raw_password = user_socket.recv(1024)
        str_password = raw_password.decode()
        if str_password == ACTIVATION_PASSWORD:
            response = 'пароль верный' 
        else:
            response = 'пароль неверный'
        try:
            byte_response = response.encode()
            user_socket.send(byte_response)
        except Exception as err:
            pass
        print(response) 
        if response == 'пароль верный':
            activate_monster()
            user_socket.close()
            break
        else:
            user_socket.close()
    except Exception as err:
        time.sleep(1)





