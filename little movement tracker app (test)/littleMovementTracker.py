#
#   Stefan Bonestroo - 09/02/2018
#
#   This little, live movement tracker uses your webcam to record your movements.
#   It will plot the amount of movement over time by obtaining the absolute
#   difference between two frames, and using the amount of pixels that are different
#   (above a certain threshold).
#
#   The code is heavily based on:
#
#   The tutorial made by 'Avinab Saha' for 'Learn Open CV' -
#   https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
#
#   And, the tutorial made by 'Adrian RoseBrock' for 'PyImageSearch' -
#   https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

from videoWriter import VideoWriter

import time
import cv2
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

# Total amount of frames to be plotted
framesToBeCaptured = 100

# Create a VideoCapture object
capture = cv2.VideoCapture(0)

if (capture.isOpened() == False):
  print("Unable to read camera feed")

# Screen resolutions are obtained
frameWidth = int(capture.get(3))
frameHeight = int(capture.get(4))

# Creates a VideoWriter object
writer = VideoWriter("hello.avi", frameWidth, frameHeight)
output = writer.writer()

x = []
y = []

# The reference frame will be the previous frame
referenceFrame = None

# Makes sure plot window is overwritten
plot.ion()

figure = plot.figure()
view = figure.add_subplot(1,1,1)

# Counter for x data
start = time.time()

# # A certain amount of frames is captured and analyzed
# for i in range(0,framesToBeCaptured):
while (True):

    succesfullyGrabbed, frame = capture.read()

    if succesfullyGrabbed:

        # A frame will converted to a grayscale image
        currentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # A Gaussian blur will be applied to that frame to cancel out noise
        currentFrame = cv2.GaussianBlur(currentFrame, (21, 21), 0)

        # Makes sure the first screen is black
        if referenceFrame is None:
            referenceFrame = currentFrame
            continue

        # Max a black and white view of the absolute difference between the
        # current frame and the reference frame
        frameDelta = cv2.absdiff(referenceFrame, currentFrame)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Data to plotted is appended
        x.append(time.time() - start)
        y.append(np.sum(thresh == 255))

        view.clear()
        view.plot(x, y)

        cv2.imshow("Move it!", thresh)
        cv2.waitKey(2)
        plot.show()

        # I get a image/frame size error that a lot of people seem to have
        # output.write(thresh)

        # After the frame is displayed, make that frame reference for next iteration
        referenceFrame = currentFrame

    # # Break the loop
    # else:
    #     break

# When everything done, release the video capture and video write objects
capture.release()
output.release()

plot.savefig("frequencyData.jpg")

# Closes all the frames
cv2.destroyAllWindows()
