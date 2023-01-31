
#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
import numpy as np

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




# function pcaScenario 
def pcaScenario():

    time.sleep(3)
    angles = np.linspace(0,3*np.pi,100)
    servo_index = [0,2,4,6,8] 
    phase = np.array([0,1,2,3,4])*np.pi /30

    """Scenario to test servo"""
    for alpha in angles:
        for i, ind in enumerate(servo_index):
            
            if i > 0:
                pca.servo[ind].angle = int(180*np.abs(np.sin(alpha+phase[i])))
            else:
                pca.servo[ind].angle = int(180-180*np.abs(np.sin(alpha+phase[i])))
        
        time.sleep(0.05)
    
    time.sleep(0.1)

    for i in [0,2,4,6,8]:
        pca.servo[i].angle=MIN_ANG[i] #disable channel

    for alpha in angles:
        for i, ind in enumerate(servo_index):
            
            if i > 0:
                pca.servo[ind].angle = int(180*np.abs(np.sin(alpha+phase[4-i])))
            else:
                pca.servo[ind].angle = int(180-180*np.abs(np.sin(alpha+phase[4-i])))
        
        time.sleep(0.05)

    time.sleep(0.1)

    for i in [0,2,4,6,8]:
        pca.servo[i].angle=MIN_ANG[i] #disable channel

    time.sleep(0.1)

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