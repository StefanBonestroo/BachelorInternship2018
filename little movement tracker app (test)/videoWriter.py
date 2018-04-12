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
