
"""
VideoWriter.py

This class holds the information for a writer object which cv2 libraries use to
write a video file.

created by: Stefan Bonestroo
date created: 07/02/2018
date last modified: 07/02/2018

"""

import cv2

class VideoWriter:

    def __init__(self, filename, frameWidth, frameHeight):

        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        self.filename = filename

    def writer(self):

        return cv2.VideoWriter(self.filename,\
                cv2.VideoWriter_fourcc('M','J','P','G'), 20,
                (self.frameWidth, self.frameHeight))
