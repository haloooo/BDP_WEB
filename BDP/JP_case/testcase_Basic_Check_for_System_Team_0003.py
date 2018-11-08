# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys, os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import jp_model_action_util, base_case, check_result

class testcase_Basic_Check_for_System_Team_0003(base_case.BaseCase):
    """
    Excel:              Basic Check for System Team.xlsx
    Category:           Service Mode
    Test case:          1) Set is in HomeUI
                        2) Press STOP + DISPLAY + PAUSE + UP in remote key
                        3) Set will reboot into Service Mode

    Expected Result:    Confirm Service mode can be enter successfully

    """
    def setUp(self):
        print("Initialization Test Environment")
        constants.flag = True
        super(testcase_Basic_Check_for_System_Team_0003, self).setUp()

    def tearDown(self):
        if constants.flag:
            jp_model_action_util.restart_power()
            jp_model_action_util.go_finish_easySetup_step()
        else:
            jp_model_action_util.go_finish_easySetup_step()
        super(testcase_Basic_Check_for_System_Team_0003, self).tearDown()

    def testcase_Basic_Check_for_System_Team_0003(self):
        print ("Step1: Enter Into HomeUI")
        jp_model_action_util.go_home()

        print ("Step2: Press STOP + DISPLAY + PAUSE + UP in remote key")
        jp_model_action_util.set_different_mode("Services Mode")

        print ("Step3: Set will reboot into Service Mode")
        self.assertTrue(check_result.check_picture_with_timeout('Service_Mode.png',type='JP'),
                        'Service Mode cannot be enter successfully')

        print ("Step4: Restart the power supply")
        jp_model_action_util.restart_power()
        constants.flag = False

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_for_System_Team_0003)
    runner.run(suite)