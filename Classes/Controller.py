import os
import sys
import random
import time
import threading
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyDAQmx import *

class DeviceController(threading.Thread):

    def __init__(self, x, y, channels, conditions, fixedOrder):

        threading.Thread.__init__(self)

        self.x = x
        self.y = y

        self.channels = channels
        self.conditions = conditions
        self.fixedOrder = fixedOrder

        self.task = Task()
        self.task.CreateDOChan("/cDAQ1Mod1/port0/line0:7","",DAQmx_Val_ChanForAllLines)

    def run(self):

        task = self.task
        A = np.array([0,0,0,0,0,0,0,0], dtype=np.uint8)
        B = np.array([0,1,0,0,0,0,0,0], dtype=np.uint8)
        C = np.array([1,0,0,0,0,0,0,0], dtype=np.uint8)
        D = np.array([1,0,1,0,0,0,0,0], dtype=np.uint8)

        task.StartTask()

        task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,A,None,None)
        time.sleep(4)
        task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,B,None,None)
        time.sleep(4)
        task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,C,None,None)
        time.sleep(4)
        task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,D,None,None)
        time.sleep(4)
        task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,A,None,None)
        task.StopTask()
