# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018

import sys,os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import qw_model_action_util, base_case, check_result

class testcase_Basic_Check_Setup_SKB_0001(base_case.BaseCase):
    """
    Excel:              Basic_Check_Setup_SKB.xlsx
    Pre-condition:      None
    Category:           SKB
    Test case:          1) HomeUI->Setup
                        2) Enter into System Settings / Device Name
                        3) verify the color key function
                        4) verify input function and save
    Expected Result:    color key work normally the input words can be saved
    """
    def setUp(self):
        print("Initialization Test Environment")
        # 1. 进入Setup界面
        # qw_model_action_util.go_setup()
        # # 2.确保resetting成功
        # qw_model_action_util.go_all_resetting()
        super(testcase_Basic_Check_Setup_SKB_0001, self).setUp()

    def tearDown(self):
        # 确保退出至HOME界面
        qw_model_action_util.send_key('BLUE')
        qw_model_action_util.send_key('RETURN')
        if check_result.check_pictures('Stop_Entry.png'):
            qw_model_action_util.send_key('LEFT')
            qw_model_action_util.send_key('ENTER')
        super(testcase_Basic_Check_Setup_SKB_0001, self).tearDown()

    def testcase_Basic_Check_Setup_SKB_0001(self):
        print ("Step1: Enter into Setup screen")
        qw_model_action_util.go_home()
        qw_model_action_util.go_setup()

        print ("Step2: Enter into System Settings / Device Name")
        qw_model_action_util.go_system_setting()
        qw_model_action_util.go_device_name()

        print ("Step3: Press The Yellow Key And Check The History")
        qw_model_action_util.send_key('YELLOW')
        self.assertTrue(check_result.check_pictures('History_Before.png'),
                        'The History is not clear')

        print ("Step4: Enter A Device Name And Check The Yellow Key")
        qw_model_action_util.send_key('BLUE')
        qw_model_action_util.enter_device_name()
        qw_model_action_util.save_device_name()
        qw_model_action_util.send_key('ENTER')
        qw_model_action_util.send_key('YELLOW')
        self.assertTrue(check_result.check_pictures('History_After.png'),
                        'The History is not displayed correctly')

        print ("Step5: Press The Blue Key And Check The History")
        qw_model_action_util.send_key('BLUE')
        self.assertTrue(check_result.check_pictures('History_Before.png'),
                        'The History is not clear')

        print ("Step6: Press The Red Key And Check The Language")
        qw_model_action_util.send_key('RED')
        self.assertTrue(check_result.check_pictures('Language_Yellow.png'),
                        'The language bar is not displayed correctly')
        qw_model_action_util.send_key("RETURN")

        print ("Step7: Press The Green Key And Check The Size Of The Input Mode")
        qw_model_action_util.send_key('GREEN')
        self.assertTrue(check_result.check_pictures('Input_Mode_Blue.png'),
                        'The Input Mode is not displayed correctly')
        qw_model_action_util.send_key('BLUE')

        print ("Step8: Enter A Device Name And Press Enter")
        qw_model_action_util.enter_device_name()
        qw_model_action_util.save_device_name()
        self.assertTrue(check_result.check_pictures('Device_Name.png'),
                        'The input word has not been saved')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_Setup_SKB_0001)
    runner.run(suite)