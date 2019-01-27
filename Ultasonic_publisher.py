#!/usr/bin/env python

import rospy #The rospy library is very important and it must be included all when we right a python code for ROS
import serial # Serial library is used here to collect the data from the arduino through a serial port
import string # the arduino will send a string message we need to convert that message to floats
import math #used for conversion 
import sys

from geometry_msgs.msg import Twist # each topic carries a specific message, in our case, try in command line > rostopic info /husky_velocity_controller/cmd_vel then try > rosmsg show geometry_msgs/Twist to know more about the message

rospy.init_node("Follower_Sensor") #this function initilizes this file as a ROS node with the name Follower_sensor

velocity_publisher = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=1) #we need to publish commands to control the robot in the simulation thats why we send the command through this topic /husky_velocity_controller/cmd_vel
# message type is Twist
#We only care about the most recent command, i.e. queue_size=1

vel_cmdMsg = Twist() # sent a variable name for message with its type Twist

port='/dev/ttyUSB0' # select the right port to read the data from it

try: # try to open the port 
    ser = serial.Serial(port=port, baudrate=115200, timeout=1)
except serial.serialutil.SerialException:
    rospy.logerr("Arduino not found at port "+port + ". Did you specify the correct port?")
    #exit
    sys.exit(0)

rospy.sleep(2)  # just stop the code execution for a bit, to make sure the data are correct from the arduino.

sens1=0
sens2=0
sens3=0

while not rospy.is_shutdown(): # while ros is running 
    line = ser.readline()# read the line of the string
    words = string.split(line,",")    # Fields split
    sens1=float(words[0]) #put the values from the arduino to variables called sens1 sens2 ...
    sens2=float(words[1])
    sens3=float(words[2])
    if ((sens1>10 and sens1<20) and (sens3>10 and sens3<20)): #forward
	vel_cmdMsg.linear.x = 1
	vel_cmdMsg.angular.z = 0
    elif ((sens1>10 and sens1<20)): #right
	vel_cmdMsg.linear.x = 1
	vel_cmdMsg.angular.z = -1
    elif ((sens3>10 and sens3<20)): #left
	vel_cmdMsg.linear.x = 1
	vel_cmdMsg.angular.z = 1
    elif ((sens2>10 and sens2<20)): #backward
	vel_cmdMsg.linear.x = -1
	vel_cmdMsg.angular.z = 0
    else:
	vel_cmdMsg.linear.x = 0
	vel_cmdMsg.angular.z = 0
    
    # the rest of the message components are set to 0 	
    vel_cmdMsg.linear.y = 0
    vel_cmdMsg.linear.z = 0
    vel_cmdMsg.angular.x = 0
    vel_cmdMsg.angular.y = 0
    velocity_publisher.publish(vel_cmdMsg)# publish the message

ser.close #close the port






