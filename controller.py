import pygame
import time
import socket

s = socket.socket()
port = 1080;
s.connect(('172.24.1.1', port))



pygame.init()
size = width,height = (100,100)
screen = pygame.display.set_mode(size);
screen.fill((255,255,255));

running = True;
speed = 1500;
agle = 90;
onoff = '00'

init = '{0}/{1}/{2} '.format(onoff, speed, agle)
def up():
    for j in [1500, 1400, 1500, 1400]:
        speed = j
        init = '{0}/{1}/{2}'.format(onoff, speed, agle)
        s = socket.socket()
        s.connect(('172.24.1.1', port))
        s.send(init.encode())
        s.close()
def down():
    speed = 1600
def napravo(agle):
    # if agle==110:
    #     agle = 90
    # elif agle==90:
    #     agle=70
    if 70 <= agle - 8 <= 110:
        agle -= 8
def nalevo(agle):
        # if agle==70:
        #     agle = 90
        # elif agle==90:
        #     agle=110
    if 70 <= agle + 8 <= 110:  # Поправил код, теперь корректнее, не должен падать.
        agle += 8
def automove(agle=90):
    for j in range(4):
        up()
        socketsend()
        time.sleep(1)
        nalevo(agle)
        socketsend()
        time.sleep(1)
        napravo(agle)
        socketsend()
        time.sleep(1)
def socketsend():
    init = '{0}/{1}/{2}'.format(onoff, speed, agle)
    s = socket.socket()
    s.connect(('172.24.1.1', port))
    s.send(init.encode())
    s.close()

sprange = range(1200, 1700)
aglerange = range(0,180)
#init
s.send(init.encode())
time.sleep(1)
s.close()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    screen.fill((255, 255, 255));
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # if agle==110:
            #     agle = 90
            # elif agle==90:
            #     agle=70
            if 70<=agle-8<=110:
                agle -= 8
        if event.key == pygame.K_LEFT:
            # if agle==70:
            #     agle = 90
            # elif agle==90:
            #     agle=110
            if 70 <= agle+8 <= 110:#Поправил код, те перь корректнее, не должен падать.
                agle += 8
        if event.key == pygame.K_1:
            agle = 90
            speed = 1500
        if event.key == pygame.K_UP:
            # flag = 0
            #
            # if speed==1600 or speed==1400:
            #     speed=1500;
            # else:
            for j in [1500, 1400, 1500, 1400]:
                speed = j
                init = '{0}/{1}/{2}'.format(onoff, speed, agle)
                s = socket.socket()
                s.connect(('172.24.1.1', port))
                s.send(init.encode())
                s.close()
        if event.key == pygame.K_2:
            agle = 110
        if event.key == pygame.K_3:
            agle = 70


        if event.key == pygame.K_DOWN:
            speed=1600
        if event.key == pygame.K_9:
            automove(agle=90)
        #if event.key == pygame.K_SPACE:

        if event.key == pygame.K_SPACE:
            speed = 1500;
            agle = 90;
            onoff = '11';
            #break;

        init = '{0}/{1}/{2}'.format(onoff, speed, agle)
        s = socket.socket()
        s.connect(('172.24.1.1', port))
        s.send(init.encode())
        s.close()
    pygame.display.flip();

s.close();
pygame.quit();