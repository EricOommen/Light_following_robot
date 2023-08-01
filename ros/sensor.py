#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

LDR_RIGHT_PIN = 16
LDR_LEFT_PIN = 18

def read_ldr_values():
    ldr_right_value = GPIO.input(LDR_RIGHT_PIN)
    ldr_left_value = GPIO.input(LDR_LEFT_PIN)

    return ldr_right_value, ldr_left_value

def ldr_publisher():
    rospy.init_node('ldr_publisher_node', anonymous=True)
    ldr_pub = rospy.Publisher('ldr', String, queue_size=10)
    rate = rospy.Rate(1)  # Set loop frequency to 1 Hz
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LDR_RIGHT_PIN, GPIO.IN)
    GPIO.setup(LDR_LEFT_PIN, GPIO.IN)
    while not rospy.is_shutdown():
        # Read LDR values
        ldr_right_value, ldr_left_value = read_ldr_values()

        # Determine the character to publish based on LDR values
        if ldr_right_value == 0 and ldr_left_value == 0:
            ldr_msg = "F"
        elif ldr_right_value == 1 and ldr_left_value == 1:
            ldr_msg = "S"
        elif ldr_right_value == 0 and ldr_left_value == 1:
            ldr_msg = "R"
        elif ldr_right_value == 1 and ldr_left_value == 0:
            ldr_msg = "L"
        else:
            # Default to 'S' if none of the conditions match
            ldr_msg = "S"
            
        # Publish LDR value as ROS topic
        rospy.loginfo("Publishing message: %s", ldr_msg)
        ldr_pub.publish(ldr_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        ldr_publisher()
    except rospy.ROSInterruptException:
        pass