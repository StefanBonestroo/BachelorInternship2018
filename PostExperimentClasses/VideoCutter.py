import cv2
import argparse

class VideoCutter:

    def __init__(self, image, height, width):

        self.image = image
        self.clone = image.copy()
        self.windowName = "Select your ROI"

        self.height = height
        self.width = width

        self.ROI = None


    def selectROI(self):

        self.ROI = cv2.selectROI(self.windowName, self.image, False, False)

        print(self.ROI)
