# -*- coding:utf-8 -*-
'''
# Hdmi
#   based on Python 2.7
'''

import threading
import time
import cv2

# from config import  constants
from BDP.config import constants


class HDMI(object):
    '''
    # HDMI:
    '''
    def __init__(self):
        """open the camera,and wait the command to record or capture the image
            Args:
                width: the width of picture.
                high: the hight of picture.
             """
        # self.cap = cv2.VideoCapture(int(constants.camera_id))
        self.cap = cv2.VideoCapture(0)
        if(constants.output_resolution == '1080p'):
            self.cap.set(3,1920)
            self.cap.set(4,1080)
        # self.cap.set(3, 1920)
        # self.cap.set(4, 1080)

        else:
            print('暂时只支持1080p')
            return

        self.imagename = None
        if not self.cap.isOpened():
            self.cap.open()
        thread = threading.Thread(target=self.open_camera, args=())
        # set false wait the threading to shutdown by itself
        thread.setDaemon(False)
        thread.start()


    def __del__(self):
        """Release everything if job is finished """
        self.cap.release()

    def open_camera(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                #frame = cv2.flip(frame, 3)
                if  self.imagename:
                    #print '%s' % self.imagename
                    cv2.imwrite('%s' % self.imagename, frame)
                    self.cap.release()

            else:
                break

    def capture(self, imagename):
        """start Record.
        Args:
            name: the name of the picture to capture.
        """
        self.imagename = imagename
        time.sleep(5)

if __name__ == '__main__':
    import os
    hdmi = HDMI()
    if (not os.path.exists(r"D:\temp")):
        os.makedirs(r"D:\temp")
    hdmi.capture(r"D:\temp\Media_Server.png")