
"""
StimulusPlot.py

This class inherits from matplotlibs' FigureCanvasQTAgg and describes the
visualization of (sub)plot on the canvas, as well as the visualization of the
little bleep that displays where you are in the experiment.

created by: Stefan Bonestroo
date created: 08/02/2018
date last modified: 13/02/2018

"""

import time

from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class StimulusPlotCanvas(FigureCanvas):

    def __init__(self, parent = None, width = 8, height = 4, dpi = 100):

        # The figure and subplot to be viewed on the canvas will be initiated
        fig = Figure(figsize = (width, height), dpi = dpi)
        fig.subplots_adjust(left = 0, right = 1, bottom = 0.1 , top = 0.8)
        self.axes = fig.add_subplot(111)

#*******************************************************************************

        # Holds the info for the graph and for the little bleep
        self.x = [0]
        self.y = [0]

        self.xBleep = 0
        self.yBleep = 0

#*******************************************************************************

        # All values and conditions concerning the 'running' of an experiment are
        # stored here (including the timer and its connection to 'bleepShower')
        self.runningTime = 0
        self.running = False

        self.bleepInterval = 250
        self.intervalsPassed = 0
        self.counter = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.bleepShower)

#*******************************************************************************

        # Upon initiation, the stimulus plot will be created inside the canvas
        self.plotStimulus()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # It should fit nicely inside of the widget box
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

#*******************************************************************************

    """"
    This function handles the plotting and other visual aspects of the plot
    """"
    def plotStimulus(self):

        # Means the 'Run experiment' button was not pressed
        if not self.running:

            # The axes should be cleared everytime this is run
            self.axes.cla()

            # Looks good to only have the x-axis (seconds)
            self.axes.spines['top'].set_visible(False)
            self.axes.spines['right'].set_visible(False)
            self.axes.spines['left'].set_visible(False)
            self.axes.get_yaxis().set_ticks([])

            self.axes.plot(self.x, self.y, drawstyle="steps-post")
            self.axes.plot(self.xBleep, self.yBleep, 'ro')

        # Means the 'Run experiment' button was pressed
        if self.running:

            # The last value of the x list will be the total running time
            self.runningTime = self.x[len(self.x) - 1]
            self.startingTime = time.time()

            # The connection that the timer has will be executed every 'bleepInterval'
            # milliseconds. This means that 'bleepShower' is triggered every 'bleepInterval' ms
            self.timer.start(self.bleepInterval)

#*******************************************************************************

    """
    Re-plots the plot every 'bleepInterval' ms to update the location of the bleep,
    so that the user can see the course of the experiment.
    """
    def bleepShower(self):

        # The value of 'xBleep' is essentially the time passed in seconds (converted from ms)
        self.xBleep = self.intervalsPassed * self.bleepInterval / 1000

        # If the signal-value ('yBleep') has to change at a certain time,
        # the plot should read a new value from the y-list
        if self.xBleep >= (self.x[self.counter]):
            self.counter += 1
        self.yBleep = self.y[self.counter - 1]

        # The plot is cleared and re-plotted
        self.axes.cla()
        self.axes.plot(self.x, self.y, drawstyle = "steps-post", zorder = 0)
        self.axes.plot(self.xBleep, self.yBleep, 'ro', zorder = 1)
        self.draw()

        self.intervalsPassed += 1

        # When we have reached our total running time the triggering of this function
        # should cease, and all values concerning the run should be reset
        if self.xBleep == self.runningTime:

            self.timer.stop()
            self.resetStuff()
            return

#*******************************************************************************

    """
    This function resets a bunch of values concerning the running of an experiment.
    """
    def resetStuff(self):

        self.xBleep = 0
        self.yBleep = 0

        self.runningTime = 0
        self.running = False

        self.intervalsPassed = 0
        self.counter = 0
