# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys,os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import qw_model_action_util, base_case, check_result

class testcase_Basic_Check_for_System_Team_0002(base_case.BaseCase):
    """
    Excel:              Basic Check for System Team.xlsx
    Category:           Demo Mode
    Test case:          1) Set is in HomeUI
                        2) Press STOP + RETURN + PAUSE + SUBTITLE in remote key
                        3) Demo Mode will be enable

    Expected Result:    - ""Demo Mode"" pop up message is appear
                        - Confirm Eject key is disabled
    """
    def setUp(self):
        print("Initialization Test Environment")
        super(testcase_Basic_Check_for_System_Team_0002, self).setUp()

    def tearDown(self):
        super(testcase_Basic_Check_for_System_Team_0002, self).tearDown()

    def testcase_Basic_Check_for_System_Team_0002(self):
        print ("Step1: Enter Into HomeUI")
        qw_model_action_util.go_home()

        print ("Step2: Press STOP + RETURN + PAUSE + SUBTITLE in remote key")
        qw_model_action_util.set_different_mode("Demo Mode")

        print ("Step3: \"Demo Mode\" pop up message is appear")
        self.assertTrue(check_result.check_pictures('Demo_Mode_Pop_Up.png', False, 0.8),
                        '"Demo Mode" pop up message is not appear')

        print ("Step4: Confirm Eject key is disabled")
        qw_model_action_util.send('OPEN')
        self.assertTrue(check_result.check_pictures('Demo_Mode_Eject_Key.png', False, 0.8),
                        'Eject key is not disabled')

        print ("Step5: Cancel The Demo Mode")
        qw_model_action_util.set_different_mode("Demo Mode")

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_for_System_Team_0002)
    runner.run(suite)