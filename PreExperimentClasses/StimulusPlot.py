
"""
StimulusPlot.py

This class inherits from matplotlibs' FigureCanvasQTAgg and describes the
visualization of (sub)plot on the canvas, as well as the visualization of the
little bleep that displays where you are in the experiment.

created by: Stefan Bonestroo
date created: 08/02/2018
date last modified: 21/02/2018

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

        self.conditionLabels = []

#*******************************************************************************

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # It should fit nicely inside of the widget box
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)


#*******************************************************************************

        # Holds the info for the graph and for the little bleep
        self.x = [0]
        self.y = [0]

        self.xBleep = 0
        self.yBleep = 0

#*******************************************************************************

        # All values and conditions concerning the 'running' of an experiment are
        # stored here
        self.runningTime = 0

        self.bleepInterval = 200    # Needs to be multiplicable to a 1000
        self.intervalsPassed = 0
        self.counter = 0

        self.oneSecond = 1000 # ms

#*******************************************************************************

    def plotStimulus(self):

        """
        This function handles the plotting and other visual aspects of the plot
        """

        # The axes should be cleared everytime this is run
        self.axes.cla()

        # Looks good to only have the x-axis (seconds)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.get_yaxis().set_ticks([])

        self.axes.plot(self.x, self.y, drawstyle="steps-post")
        self.axes.plot(self.xBleep, self.yBleep, 'ro')

        self.placeLabels()

#*******************************************************************************

    def bleepShower(self):

        """
        Re-plots the plot every 'bleepInterval' ms to update the location of the bleep,
        so that the user can see the course of the experiment.
        """

        # When we have reached our total running time the triggering of this function
        # should cease, and all values concerning the run should be reset
        if self.xBleep == self.runningTime:
            return 

        # The value of 'xBleep' is essentially the time passed in seconds (converted from ms)
        self.xBleep = self.intervalsPassed * self.bleepInterval / self.oneSecond

        # If the signal-value ('yBleep') has to change at a certain time,
        # the plot should read a new value from the y-list
        if self.xBleep >= (self.x[self.counter]):
            self.counter += 1

        self.yBleep = self.y[self.counter - 1]

        # The plot is cleared and re-plotted
        self.axes.cla()
        self.axes.plot(self.x, self.y, drawstyle = "steps-post", zorder = 0)
        self.axes.plot(self.xBleep, self.yBleep, 'ro', zorder = 1)

        self.placeLabels()

        # Draw the plot
        self.draw()

        self.intervalsPassed += 1

#*******************************************************************************

    def placeLabels(self):

        """
        This function places the labels above the stimuli and will change the color of
        the label of the active stimulus.
        """

        # Every uneven index number is stimulus activation point
        stimPoint = 1

        # Place the conditions above the stimulus position, one by one
        for label in self.conditionLabels:

            # The x where of where the centre of the label should go is the average
            # between the activation point and deactivation point
            x = (self.x[stimPoint] +  self.x[stimPoint + 1]) / 2
            y = 1.2

            # The stimulus label will light up when on
            if self.xBleep >= self.x[stimPoint] and self.xBleep < self.x[stimPoint + 1]:
                color = 'red'
            else:
                color = 'white'

            self.axes.text(x, y , label, \
                            bbox = dict(facecolor = color, alpha = 0.3), \
                            horizontalalignment='center', verticalalignment='center')

            stimPoint += 2

#*******************************************************************************

    def resetStuff(self):

        """
        This function resets a bunch of values concerning the running of an experiment.
        """

        self.xBleep = 0
        self.yBleep = 0

        self.runningTime = 0

        self.intervalsPassed = 0
        self.counter = 0
