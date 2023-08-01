#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

RMotor_1 = 29
RMotor_2 = 31
LMotor_1 = 33
LMotor_2 = 35

def setup():
    GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering mode to BCM
    GPIO.setup(RMotor_1, GPIO.OUT)
    GPIO.setup(RMotor_2, GPIO.OUT)
    GPIO.setup(LMotor_1, GPIO.OUT)
    GPIO.setup(LMotor_2, GPIO.OUT)

def move_forward():
    #Your code for moving the motors forward here
    GPIO.output(RMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(LMotor_2, GPIO.HIGH)
    pass

def move_left():
    #Your code for moving the motors left here
    GPIO.output(RMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(LMotor_2, GPIO.LOW)
    pass

def move_right():
    #Your code for moving the motors right here
    GPIO.output(RMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(LMotor_2, GPIO.HIGH)
    pass

def move_stop():
    #Your code for stopping the motors here
    GPIO.output(RMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(LMotor_2, GPIO.LOW)
    pass

def move_motors_callback(data):
    #Process the received LDR signal and move the motors accordingly
    cmd = data.data
    rospy.loginfo("Received message: %s", cmd)
    if cmd == 'F':
        move_forward()
    elif cmd == 'S':
        move_stop()
    elif cmd == 'L':
        move_left()
    elif cmd == 'R':
        move_right()

def ldr_subscriber():
    rospy.init_node('ldr_subscriber_node', anonymous=True)
    rospy.Subscriber('ldr', String, move_motors_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        setup()
        ldr_subscriber()
    except rospy.ROSInterruptException:
        pass
