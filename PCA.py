#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

#Constants
nbPCAServo=16 

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[0, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
INC = [-2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

#Objects
pca = ServoKit(channels=16)

# function init 
def init():

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])


# function main 
def main():

    pcaScenario();


time.sleep(3)


# function pcaScenario 
def pcaScenario():
    """Scenario to test servo"""
    for i in [0,2,4,6,8]:
        for j in range(MIN_ANG[i],MAX_ANG[i],4*INC[i]):
            #print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-4*INC[i]):
            #print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
       # pca.servo[i].angle=None #disable channel
        time.sleep(0.1)
    
    for i in [8,6,4,2,0]:
        for j in range(MIN_ANG[i],MAX_ANG[i],4*INC[i]):
            #print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-4*INC[i]):
            #print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        #pca.servo[i].angle=None #disable channel
        time.sleep(0.1)

    for j in range(MIN_ANG[1],MAX_ANG[1],INC[1]):

        for i in [2,4,6,8]:

            pca.servo[i].angle = j

        pca.servo[0].angle = 180 - j
        time.sleep(0.01)

    for j in range(MAX_ANG[1],MIN_ANG[1],-INC[1]):

        for i in [2,4,6,8]:

            pca.servo[i].angle = j

        pca.servo[0].angle = 180 - j
        time.sleep(0.01)

    for i in [0,2,4,6,8]:
        pca.servo[i].angle=None #disable channel

    '''for i in [0,2,4,6,8]:

        pca.servo[i].angle = MAX_ANG[i]
        
    time.sleep(0.5)

    for i in [0,2,4,6,8]:

        pca.servo[i].angle = MIN_ANG[i]
        pca.servo[i].angle=None #disable channel

    '''    






if __name__ == '__main__':
    init()
    main()