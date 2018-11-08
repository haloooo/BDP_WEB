# -*- coding:utf-8 -*-
'''
# TargetMatch:
#   based on Python 2.7
'''
import os,time
import cv2
import numpy as np

MAX_MATCH_NUM = 3
class TargetMatch(object):
    '''
    TargetMatch is to get the location of the target image in the source.
    methodsPtn = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED,  # cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    '''
    def __init__(self, img_path, target_path, thre=0.3):
        """
        Init the paras of the images
        Args:
            img_path: the source picture.
            target_path: the target picture.
            thre: thre  is the resize ratio
        """
        if not checkfile(img_path, target_path):
            return

        for i in range(0,10):
            if(os.path.exists(img_path) == False):
                time.sleep(1)
            else:
                break
        self.back_ground = cv2.imread(img_path)
        self.target = cv2.imread(target_path)
        self.height, self.width, self.channel = self.target.shape
        assert self.height and self.width
        self.rect = thre * (self.height > self.width and self.height or self.width)

    def has_child_picture(self, target_score=0.8):
        """
        return if has the child picture of the source picture by target_score
        Args:
            target_score: if the score above the target_score,return True.
        """
        pos = self.get_target_pos()
        best_pos, score = self.get_best_target_pos(pos)
        if score != 1 and score != 0:
            score = score[0]
        if score < target_score:
            return False, ()
        else:
            return True, best_pos

    def get_target_pos(self, method=cv2.TM_SQDIFF_NORMED):
        '''
        Template to get the approximate pos of the target
        Args:
            method:method of opencv
        Return:
             matches
        '''
        result = cv2.matchTemplate(self.back_ground, self.target, method)
        # get the max/min value
        ret = np.reshape(result, result.shape[0] * result.shape[1])
        res = None
        # For the TM_SQDIFF and TM_SQDIFF_NORMED series the best match are the lowest values.For all the others, higher values represent better matches
        if method == cv2.TM_SQDIFF or method == cv2.TM_SQDIFF_NORMED:
            res = np.argsort(ret)
        else:
            res = np.argsort(-ret)
        num = len(res) > MAX_MATCH_NUM and MAX_MATCH_NUM or len(res)
        matches = []
        for idx, value in enumerate(res):
            if idx == num:
                break
            # get the target pos
            y_coor, x_coor = np.unravel_index(value, result.shape)
            top_left = (x_coor, y_coor)
            bottom_right = (top_left[0] + self.width, top_left[1] + self.height)
            matches.append([top_left, bottom_right])
        return matches

    def get_best_target_pos(self, matches):
        '''
        Get the approximatest pos of the target
        Args:
            matches:matches list
        Return:
            [top-left,bottom-right],similar score
        '''
        best_score = 0
        best_pose = []
        for pos in matches:
            score = self.calc_similar(pos, self.channel)
            if score >= best_score:
                best_score = score
                if len(best_pose) == 0 or best_pose[0][0] > pos[0][0] or best_pose[0][1] > pos[0][1]:
                    best_pose = pos
        return best_pose, best_score



    def calc_similar(self, pos, channel=3):
        '''
        Get the score of the pos
        Args:
             pos: pos of target
        Return:score
        '''
        def calc(src, dst):
            '''
            calculate the degree of the img
            Args:
                 src: the source picture
                 dst: the target picture
            Return:degree
            '''
            hist1 = cv2.calcHist([src], [0], None, [256], [0.0, 255.0])
            hist2 = cv2.calcHist([dst], [0], None, [256], [0.0, 255.0])
            degree = 0
            for index, value in enumerate(hist1):
                if value != hist2[index]:
                    degree = degree + (1 - abs(value - hist2[index]) / max(value, hist2[index]))
                else:
                    degree = degree + 1
            degree = degree / len(hist1)
            return degree
        def roi(base, pos):
            '''
            Get the info of the img
            Args:
                 base:info of img
                 pos: pos of target
            Return:base
            '''
            return base[pos[0][1] : pos[1][1], pos[0][0] : pos[1][0]]

        targ = cv2.split(self.target)
        src = cv2.split(roi(self.back_ground, pos))
        degree = 0
        for im1, im2 in zip(targ, src):
            degree += calc(im1, im2)
        degree = degree / channel
        return degree

def checkfile(img_path, target_path):
    '''
    checkfile
        Args:
            img_path:
            target_path:
        Return:
            bool
    '''
    if os.path.isfile(img_path) or os.path.isfile(target_path):
        return True
    else:
        return False

if __name__ == '__main__':
    IMG_PATH = r"D:\temp\64f5b14a-9adf-11e8-a071-b083fe7dfab7.png"
    TAR_PATH = r"D:\BDP\BDP\pictures\EasyDisplaySettings.png"
    # template match
    match = TargetMatch(IMG_PATH, TAR_PATH)
    # match = TargetMatch(TAR_PATH,IMG_PATH)
    # print match.height
    # print match.width
    a,b = match.has_child_picture(0.9)
    print(a,b)