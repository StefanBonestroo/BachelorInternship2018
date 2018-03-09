import threading

from goprocam import GoProCamera
from goprocam import constants

class GoPro(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)

        self.cam = GoProCamera.GoPro()

        self.runningTime = 0


    def run(self):

        self.cam.shoot_video(self.runningTime)
        return
