# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys, os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import jp_model_action_util, base_case, check_result

class testcase_ContentList_BasicCheck_0001(base_case.BaseCase):
    """
    Excel:              ContentList_BasicCheck.xlsx
    Category:           Video/Music/Photo List
    Test case:          1) On ""BDP Home"" screen, press [ENTER] key on Dis/USB/MediaServer icon.
                        #  For USB/MediaServer, continue to select a device."
                        2) On Video/Music/Photo list screen, press arrow keys and [ENTER] key.
                        3) On Video/Music/Photo list screen, press [ENTER] key on a Video/Music/Photo file.

    Expected Result:    Default is Video category.
                        Video list screen display normal.
                        Focus move normal, can enter to next layer.
                        Can open video playback.
    """
    def setUp(self):
        print("Initialization Test Environment")
        self.assertTrue(jp_model_action_util.check_USB('JP'),
                        'please Insert the USB correctly.')
        super(testcase_ContentList_BasicCheck_0001, self).setUp()
        # 1. 进入Home UI界面
        jp_model_action_util.send_key('HOME')
        # 2. 进入Setup界面
        jp_model_action_util.go_setup()
        # 3.确保resetting成功
        jp_model_action_util.go_all_resetting()
        jp_model_action_util.send_key('HOME')

    def tearDown(self):
        super(testcase_ContentList_BasicCheck_0001, self).tearDown()

    def testcase_ContentList_BasicCheck_0001(self):
        # 1. Video List
        print ("Step1: Enter Into USB device")
        jp_model_action_util.go_usb_device()

        print ("Step2: On Video list screen, press [ENTER] key on a video file")
        jp_model_action_util.play_source('video')

        print ("Step3: Can open video playback")
        jp_model_action_util.send_key('DISPLAY')
        self.assertTrue(check_result.check_pictures('Play_Back.png',type='JP'),
                        'Open video playback failed')
        jp_model_action_util.quit_play_back('video')

        # 2. Music List
        print ("Step4: Change catetory to Music")
        jp_model_action_util.change_catetory()

        print ('Step5: On Music list screen, Press [ENTER] key on a music file')
        jp_model_action_util.play_source('music')

        print ("Step6: Can open video playback")
        self.assertTrue(check_result.check_pictures('Play_Back.png',type='JP'),
                        'Open music playback failed')
        jp_model_action_util.quit_play_back('music')

        # 3 Photo List
        print ("Step7: Change catetory to Photo")
        jp_model_action_util.change_catetory()

        print ("Step8: On Photo list screen, Press [ENTER] key on a photo file")
        jp_model_action_util.play_source('photo')

        print ("Step9: Can open photo playback")
        self.assertTrue(check_result.check_pictures('Photo.png',True,type='JP'),
                        'Open photo playback failed')
        jp_model_action_util.quit_play_back('photo')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_ContentList_BasicCheck_0001)
    runner.run(suite)