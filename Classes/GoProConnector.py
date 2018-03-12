"""
GoProController.py

This class is inherits from threading.Thread, and will when started send commands
to a paired GoPro (shoot a X seconds video in this case). Upon intiation the GoPro
will be paired.

The API used is KonradIT's 'Unofficial GoPro API Library for Python':
https://github.com/KonradIT/gopro-py-api

created by: Stefan Bonestroo
date created: 09/03/2018
date last modified: 12/02/2018
"""

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
