"""
Controller.py

This class inherits from threading.Thread, so that it can be run parallel to the
visualizations in the GUI. Running this thread means the connected hardware (NI-9172) will be run.

created by: Stefan Bonestroo
date created: 24/02/2018
date last modified: 07/02/2018
"""

import time
import threading
import numpy as np

from PyDAQmx import *

class DeviceController(threading.Thread):

    def __init__(self, x, y, conditions, runningTime, fixedOrder):

        threading.Thread.__init__(self)

        self.x = x
        self.y = y

#*******************************************************************************

        self.conditions = conditions
        self.fixedOrder = fixedOrder
        self.runningTime = runningTime

#*******************************************************************************

        # The hardware is configured and made ready to receive signals
        self.task = Task()
        self.task.CreateDOChan("/cDAQ1Mod1/port0/line0:7","",DAQmx_Val_ChanForAllLines)

        self.channels = [[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0], [1,0,1,0,0,0,0,0]]
        self.triggerTree = {}

#*******************************************************************************

        self.counter = 0

        # A dictionary is made containing all the stimulus names + their channels
        for condition in conditions:
            self.triggerTree["{0}".format(condition)] = np.array(self.channels[self.counter],\
                                                        dtype = np.uint8)
            self.counter += 1


        self.allOff = np.array([0,0,0,0,0,0,0,0], dtype = np.uint8)

#*******************************************************************************

    def run(self):

        """
        This inherited function will run the thread and run the stimulus protocol on it.
        """

        self.counter = 0
        currentCondition = 0

        # For every on and off state, the loop is run (the last index is not used)
        for y in self.y[:-1]:

            # If it needs to be on, activate the channels to fit the next condition
            if y == 1:

                channelActivity = self.triggerTree[self.conditions[currentCondition]]
                self.task.WriteDigitalLines(1, 1, 10.0, DAQmx_Val_GroupByChannel, \
                                                channelActivity, None, None)
                self.conditions[currentCondition]
                currentCondition += 1

            # Else set to the default channel
            else:
                self.task.WriteDigitalLines(1, 1, 10.0, DAQmx_Val_GroupByChannel, \
                                                self.allOff, None, None)

            # Wait for an interval amount of seconds (as given by the user in the
            # stimulus protocol)
            time.sleep(self.x[self.counter + 1] - self.x[self.counter])
            self.counter += 1

        # Return to default state and stop the task
        self.task.WriteDigitalLines(1, 1, 10.0, DAQmx_Val_GroupByChannel, self.allOff, None, None)
        self.task.StopTask()
