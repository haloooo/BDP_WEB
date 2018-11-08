# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys, os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import jp_model_action_util, base_case, check_result

class testcase_HomeUI_BasicCheck_0002(base_case.BaseCase):
    """
    Excel:              HomeUI_BasicCheck.xlsx

    Pre-condition:      - Destination: US, Language: English.
                        - Complete All&Personal Settings resetting.
                        - Power is ON.

    Category:           Launch Apps

    Test case:          1) Insert a disc, then press [ENTER] key on disc icon.
                        2) Insert a USB, then press [ENTER] key on USB icon.
                        3) Press [ENTER] key on Media Server icon.
                        4) Press [ENTER] key on Screen mirroring icon.
                        5) Press [ENTER] key on a bivl app icon.


    Expected Result:    Disc icon display normal.
                        Can open disc play/list.
                        USB icon display normal.
                        Can open USB list.
                        Can open Media Server list.
                        Can open Screen mirroring screen.
                        Can open the bivl app.
    """
    def setUp(self):
        print("Initialization Test Environment")
        super(testcase_HomeUI_BasicCheck_0002, self).setUp()
        # # # 1. 进入Home UI界面
        # # jp_model_action_util.send_key('HOME')
        # # # 2. 进入Setup界面
        # # jp_model_action_util.go_setup()
        # # # 3.确保resetting成功
        # # jp_model_action_util.go_all_resetting()
        # # # 4. 进入Home UI界面
        # # jp_model_action_util.send_key('HOME')
        # # 5. Internet
        # # jp_model_action_util.go_setup()
        # # jp_model_action_util.go_network_setting()
        # # jp_model_action_util.go_internet_settings()
        # # jp_model_action_util.set_wireless_setup()
        # jp_model_action_util.go_right_wireless()
        # jp_model_action_util.config_wireless_setup()
        # # 4.确保图标居中
        # jp_model_action_util.init_focus_location()

    def tearDown(self):
        if (check_result.check_pictures('Connection_Status.png', type='JP')):
            jp_model_action_util.send_key("RIGHT")
            jp_model_action_util.send_key("ENTER")
            jp_model_action_util.send_key("UP")
        super(testcase_HomeUI_BasicCheck_0002, self).tearDown()

    def testcase_HomeUI_BasicCheck_0002(self):
        print ('Step1: Insert a disc,Disc icon display normal')
        jp_model_action_util.send_key('LEFT')
        self.assertTrue(check_result.check_pictures('disc_icon.png', type='JP'),
                        'Disc icon display unnormal')

        print ('Step2: Press [ENTER] key on disc icon')
        jp_model_action_util.send_key('ENTER', 2)

        print ('Step3: Can open disc play/list')
        jp_model_action_util.send_key('DISPLAY')
        self.assertTrue(check_result.check_pictures('Play_Back.png', type='JP'),
                        'Can not open disc play/list')
        jp_model_action_util.send_key('STOP', 2)

        print ('Step4: Insert a USB, USB icon display normal')
        jp_model_action_util.go_diff_icon('USB')
        self.assertTrue(check_result.check_pictures('USB_device.png', type='JP'),
                        'USB icon display unnormal')

        print ('Step5: Press [ENTER] key on USB icon')
        jp_model_action_util.send_key('ENTER', 2)

        print ('Step6: Can open USB list.')
        self.assertTrue(check_result.check_pictures('USB_device_appearance.png', type='JP'),
                        'Open USB list failed')
        jp_model_action_util.send_key('RETURN', 2)

        print ('Step7: Can open Media Server list')
        jp_model_action_util.send_key('RIGHT')
        jp_model_action_util.send_key('ENTER')
        self.assertTrue(check_result.check_pictures('Media_Server.png', type='JP'),
                        'Can not open Media Server list')
        jp_model_action_util.send_key('HOME')

        print ('Step10: Press [ENTER] key on a bivl app icon')
        jp_model_action_util.go_diff_icon('bivl app')

        print ('Step11: Can open the bivl app')
        self.assertTrue(check_result.check_pictures('bivl_app.png', type='JP'),
                        'Can not open the bivl app')
        jp_model_action_util.send_key('HOME')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_HomeUI_BasicCheck_0002)
    runner.run(suite)