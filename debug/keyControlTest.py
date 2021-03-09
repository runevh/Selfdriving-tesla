import serial
import pygame
from pygame.locals import *

class CTRLTest(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_mode(500, 500)
        self.ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        self.send_inst = True
        self.steer()

    def steer(self):

        while self.send_inst:
            for e in pygame.event.get():
                if e.type == KEYDOWN:
                    input = pygame.key.get_pressed()

                    if input[pygame.K_UP]:
                        print("forward")

                    elif input[pygame.K_DOWN]:
                        print("backwards")

                    elif input[pygame.K_RIGHT]:
                        print("right")

                    elif input[pygame.K_LEFT]:
                        print("left")

                elif e.type == pygame.KEYUP:
                    print("up")


if __name__ == '__main__':
    CTRLTest()