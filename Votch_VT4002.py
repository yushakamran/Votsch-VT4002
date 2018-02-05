# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:35:25 2018

Below are functions for setting and getting the temperature
of the Votsch VT4002. These are assuming you are using serial
communication via RS232.

NOTE: The baud rate and the ID of the climate chamber will
most likely be different for your chamber.

@author: ekamyus
"""

import serial
#NOTE: baud rate is set inside the chamber's interface, default is 9600
cc = serial.Serial('COM1', 9600, timeout = 1)

def setTemp(temp):
    #Note 01 is the chamber's ID, can be anything from 0-31
    cc.write(b"$01E 00" + str(temp).encode() + b".0\r\n")

def getTemp():
    #Note 01 is the chamber's ID, can be anything from 0-31
    cc.write(b"$01I\r\n")
    temp = cc.readline().decode("utf-8").split(" ")[1]
    return float(temp)