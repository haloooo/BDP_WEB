# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018

import os, uuid, datetime, time, sys
sys.path.insert(0, os.getcwd())
from BDP.service.IR_hdmi_capture.hdmi import HDMI
from BDP.service.IR_image_location.target_match import TargetMatch
from BDP.config import constants
from BDP.common import qw_model_action_util

# 对比图片是否匹配
def check_pictures(tar_pic, display=False,ratio=constants.ratio, type='QW'):
    hdmi = HDMI()
    IMG_PATH = os.path.join(constants.temp_dir, str(uuid.uuid1()) + '.png')
    if(type == 'QW'):
        TAR_PATH = os.path.join(os.path.join(constants.tar_path, 'QW_model'), tar_pic)
    if (type == 'JP'):
        TAR_PATH = os.path.join(os.path.join(constants.tar_path, 'JP_model'), tar_pic)
    if (type == 'CN'):
        TAR_PATH = os.path.join(os.path.join(constants.tar_path, 'CN_model'), tar_pic)
    if(not os.path.exists(constants.temp_dir)):
        os.makedirs(constants.temp_dir)
    if display:
        qw_model_action_util.send_key('DISPLAY', 0)
    hdmi.capture(IMG_PATH)
    match = TargetMatch(IMG_PATH, TAR_PATH)
    flag, location = match.has_child_picture(ratio)
    return flag

def check_picture_with_timeout(tar_pic, display=False ,type='QW'):
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).\
        strftime("%Y-%m-%d %H:%M:%S")
    while start_time < end_time:
        if check_pictures(tar_pic, display, type=type):
            return True
        time.sleep(10)
        start_time = (datetime.datetime.now() + datetime.timedelta(seconds=10)).\
            strftime("%Y-%m-%d %H:%M:%S")
    return False

