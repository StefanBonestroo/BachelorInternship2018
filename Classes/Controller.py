import os
import sys
import random
import time
import threading

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

        task = Task()

    def run(self):



        self.runStimulusProtocol()

    def runStimulusProtocol(self):
