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
        self.mouseCoordinates = []
        self.currentlyCropping = False


    def selectROI(self):

        cv2.namedWindow(self.windowName)
        cv2.setMouseCallback(self.windowName, self.clickAndCrop)

        while(True):

            cv2.imshow(self.windowName, self.image)
            key = cv2.waitKey(0) & 0xFF


            # If the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                print(key)
                self.image = self.clone.copy()

            # If the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                print(key)
                break

        if len(self.mouseCoordinates) == 2:
            roi = clone[self.mouseCoordinates[0][1]:self.mouseCoordinates[1][1],\
                        self.mouseCoordinates[0][0]:self.mouseCoordinates[1][0]]

            cv2.imshow("ROI", roi)
            cv2.waitKey(0)

        cv2.destroyAllWindows()


    def clickAndCrop(self, event, x, y, flags, paramaters):

        if event == cv2.EVENT_LBUTTONDOWN:
        	self.mouseCoordinates = [(x, y)]
        	self.currentlyCropping = True

        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
        	# record the ending (x, y) coordinates and indicate that
        	# the cropping operation is finished
        	self.mouseCoordinates.append((x, y))
        	self.currentlyCropping = False

        	# draw a rectangle around the region of interest
        	cv2.rectangle(self.image, self.mouseCoordinates[0], self.mouseCoordinates[1], (0, 255, 0), 2)
        	cv2.imshow(self.windowName, self.image)
