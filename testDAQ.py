from PyDAQmx import *
import numpy as np
import time


on = np.array([0,1,0,0,0,0,0,0], dtype=np.uint8)
otherOn = np.array([0,0,1,0,0,0,0,0], dtype=np.uint8)
off = np.array([0,0,0,0,0,0,0,0], dtype=np.uint8)

task = Task()
task.CreateDOChan("/cDAQ1Mod1/port0/line0:7","",DAQmx_Val_ChanForAllLines)
task.StartTask()

task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,on,None,None)
time.sleep(2)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,otherOn,None,None)
time.sleep(0.5)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,on,None,None)
time.sleep(0.2)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,otherOn,None,None)
time.sleep(0.2)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,on,None,None)
time.sleep(0.4)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,otherOn,None,None)
time.sleep(0.9)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,on,None,None)
time.sleep(0.4)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,otherOn,None,None)
time.sleep(0.1)
task.WriteDigitalLines(1,1,10.0,DAQmx_Val_GroupByChannel,off,None,None)
task.StopTask()
