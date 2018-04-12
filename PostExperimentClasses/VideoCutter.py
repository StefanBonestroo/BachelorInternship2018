import os

import cv2
import argparse

class VideoCutter:

    def __init__(self, image):

        self.image = image
        self.windowName = "Select your ROI"

    def selectROI(self):

        ROI = cv2.selectROI(self.windowName, self.image, False, False)
        cv2.destroyAllWindows()

        return ROI
