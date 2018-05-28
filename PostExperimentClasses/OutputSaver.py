import os

import GUIFiles.enterInfoGUI as enterInfoGUI
from PostExperimentClasses.DataProcessor import getPower, getMovement, dataCutter

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets

class OutputSaver(QtWidgets.QMainWindow, enterInfoGUI.Ui_enterInfoWindow):

    def __init__(self, parent = None):

        super(OutputSaver, self).__init__(parent)
        self.setupUi(self)

        screen = self.frameGeometry()
        centre = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(centre)
        self.move(screen.topLeft())

        self.conditionOne = [self.conOneLineEdit, self.conOneLineLabel,
                            self.conOneFamilyEdit, self.conOneFamilyLabel,
                            self.conOneAgeLabel, self.conOneAgeSpinBox,
                            self.conOneAgeSpinBox]

        self.conditionTwo = [self.conTwoLineEdit, self.conTwoLineLabel,
                            self.conTwoFamilyEdit, self.conTwoFamilyLabel,
                            self.conTwoAgeLabel, self.conTwoAgeSpinBox,
                            self.conTwoAgeSpinBox]

        self.conditionThree = [self.conThreeLineEdit, self.conThreeLineLabel,
                            self.conThreeFamilyEdit, self.conThreeFamilyLabel,
                            self.conThreeAgeLabel, self.conThreeAgeSpinBox,
                            self.conThreeAgeSpinBox]

        self.conditionFour = [self.conFourLineEdit, self.conFourLineLabel,
                            self.conFourFamilyEdit, self.conFourFamilyLabel,
                            self.conFourAgeLabel, self.conFourAgeSpinBox,
                            self.conFourAgeSpinBox]

#******************************************************************************

        self.conOneRadioButton.clicked.connect(self.makeConditionAvailable)
        self.conTwoRadioButton.clicked.connect(self.makeConditionAvailable)
        self.conThreeRadioButton.clicked.connect(self.makeConditionAvailable)
        self.conFourRadioButton.clicked.connect(self.makeConditionAvailable)

#******************************************************************************

        self.data = None

#******************************************************************************

        self.rawDataDirectory = None
        self.outputDataDirectory = None

        self.setRawDataDirectoryButton.clicked.connect(self.setInputDirectory)
        self.setOutputDataDirectoryButton.clicked.connect(self.setOutputDirectory)

#******************************************************************************

        self.saveOutputButton.clicked.connect(self.saveOutput)

#******************************************************************************

    def makeConditionAvailable(self):

        states = [self.conOneRadioButton.isChecked(),
                    self.conTwoRadioButton.isChecked(),
                    self.conThreeRadioButton.isChecked(),
                    self.conFourRadioButton.isChecked()]

        conditions = [self.conditionOne, self.conditionTwo,
                        self.conditionThree, self.conditionFour]

        x = 0

        for condition in conditions:

            for option in condition:
                option.setEnabled(states[x])

            x += 1

#******************************************************************************

    def setInputDirectory(self):

        """
        This function lets the user pick a directory and will present all relevant
        files inside a QListWidget (csv files in our case).
        """

        # The list is cleared
        self.rawDataList.clear()

        # A directory picker is opened
        self.rawDataDirectory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose your directory")

        # If a directory has been chosen, iterate over all files en add all videofiles to the list
        if self.rawDataDirectory:

            for file in os.listdir(self.rawDataDirectory):

                if file.endswith(".csv"):

                    self.rawDataList.addItem(file)

#******************************************************************************

    def setOutputDirectory(self):

        """
        This function lets the user pick a directory and will present all relevant
        files inside a QListWidget (csv files in our case).
        """

        # The list is cleared
        self.outputDataList.clear()

        # A directory picker is opened
        self.outputDataDirectory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose your directory")

        # If a directory has been chosen, iterate over all files en add all videofiles to the list
        if self.outputDataDirectory:

            for file in os.listdir(self.outputDataDirectory):

                if file.endswith(".csv"):

                    self.outputDataList.addItem(file)

#******************************************************************************

    def readInput(self):

        item = self.rawDataList.currentItem()

        if item == None:
            return

        path = self.rawDataDirectory + "/" + item.text()

        file = open(path, 'r')
        table = file.readlines()
        header = table.pop(0)

        data = [list() for i in range(2)]

        for row in table:

            datapoint = row.split(';')
            x = float(datapoint[0])
            y = float(datapoint[1])

            data[0].append(x)
            data[1].append(y)

        return data

#******************************************************************************

    def saveOutput(self):

        data = self.readInput()

        stimulusLength = self.stimulusLengthSpinBox.value()
        preStimulus = self.preExperimentSpinBox.value()
        interval = self.intervalLengthSpinBox.value()
        timeframe = self.timeFrameSpinBox.value()

        stimuli = [self.conOneEdit.text(), self.conTwoEdit.text(), \
                    self.conThreeEdit.text(), self.conFourEdit.text()]

        median = []
        mean = []
        low = []
        mid = []
        high = []
        sums = []

        for n in range(0,4):

            start = preStimulus + (n * (stimulusLength + interval))
            pre, post = dataCutter(data, start, stimulusLength, timeframe)
            powers = getPower(pre, post)

            print("\n---------STIMULUS-", stimuli[n], "------START-", start, "-S----------------")
            median.append(powers[0])
            print("Median: ", powers[0])
            mean.append(powers[1])
            print("Mean: ", powers[1])
            low.append(powers[2])
            print("Low: ", powers[2])
            mid.append(powers[3])
            print("Mid: ", powers[3])
            high.append(powers[4])
            print("High: ", powers[4])

            sum = getMovement(pre, post)

            sums.append(sum)
            print("Sum: ", sum)
            print("----------------------------------------------------------\n")

        self.writeOutput(stimuli, median, mean, low, mid, high, sums)

#******************************************************************************

    def writeOutput(self, stimuli, median, mean, low, mid, high, sums):

        item = self.outputDataList.currentItem()

        if item == None:
            return

        path = self.outputDataDirectory.replace(' ', '\ ')

        path = path + "/" + item.text()

        file = open(path, 'r')
        contents = file.readlines()
        file.close()

        header = "Moth_nr;Moth_family;Moth_line;Moth_age;Date;EXP_time;Chamber"\
                + ";Habituation_setup;Habituation_light;Humid;Temp;Flow"\
                + ";Stimulus;Stimulus_nr;Stimulus_family;Stimulus_line;Stimulus_age"\
                + ";Median_power;Mean_power;Low_bandpower;Mid_bandpower;High_bandpower"\
                + ";Sum_movement;Notes" + "\n"

        day = str(self.experimentDaySpinBox.value())
        month = str(self.experimentMonthSpinBox.value())

        hour = str(self.experimentHourSpinBox.value())
        minute = str(self.experimentMinutesSpinBox.value())

        if len(day) == 1:
            day = "0" + day

        if len(month) == 1:
            month = "0" + month

        if len(hour) == 1:
            hour = "0" + hour

        if len(minute) == 1:
            minute = "0" + minute

        time = hour + ":" + minute + ":00"
        date = day + "-" + month

        families = [self.conOneFamilyEdit.text(), self.conTwoFamilyEdit.text(),\
                    self.conThreeFamilyEdit.text(), self.conFourFamilyEdit.text()]

        lines = [self.conOneLineEdit.text(), self.conTwoLineEdit.text(),\
                    self.conThreeLineEdit.text(), self.conFourLineEdit.text()]

        ages = []

        if self.conOneRadioButton.isChecked():
            ages.append(str(self.conOneAgeSpinBox.value()))
        else:
            ages.append("")

        if self.conTwoRadioButton.isChecked():
            ages.append(str(self.conTwoAgeSpinBox.value()))
        else:
            ages.append("")

        if self.conThreeRadioButton.isChecked():
            ages.append(str(self.conThreeAgeSpinBox.value()))
        else:
            ages.append("")

        if self.conFourRadioButton.isChecked():
            ages.append(str(self.conFourAgeSpinBox.value()))
        else:
            ages.append("")

        if len(contents) == 0:

            file = open(path,'w')
            file.write(header)
            mothNumber = 1

        else:

            file = open(path,'a')

            try:
                lastLine = contents[len(contents) - 2]
                line = lastLine.split(';')
                mothNumber = int(line[0]) + 1
            except:
                lastLine = contents[len(contents) - 3]
                line = lastLine.split(';')
                mothNumber = int(line[0]) + 1

        for n in range(0,4):

            row = str(mothNumber) + ";" + self.familyNameEdit.text() + ";"\
                + self.lineNameEdit.text() + ";" + str(self.ageSpinBox.value()) + ";"\
                + date + ";" + time + ";" + str(self.chamberNumberSpinBox.value()) + ";"\
                + str(self.habituationSetUpSpinBox.value()) + ";"\
                + str(self.habituationLightsSpinBox.value()) + ";"\
                + str(self.humiditySpinBox.value()) + ";" + str(self.temperatureSpinBox.value())\
                + ";" + str(self.flowSpinBox.value()) + ";" + stimuli[n] + ";"\
                + str(n + 1) + ";" + families[n] + ";" + lines[n] + ";" + ages[n] + ";"\
                + str(median[n]) + ";" + str(mean[n]) + ";" + str(low[n]) + ";" + str(mid[n]) + ";"\
                + str(high[n]) + ";" + str(sums[n]) + ";" + self.notesTextEdit.toPlainText() + "\n"

            file.write(row)
