# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys, os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import jp_model_action_util, base_case, check_result, jp_model_action_util


class testcase_Basic_Check_Setup_0001(base_case.BaseCase):
    """
    Excel:              Basic_Check_Setup.xlsx
    Pre-condition:      None
    Category:           EasySetup
    Test case:          1) Factory Resetting/All Resetting
                        2) Power Off -> Power On
    Expected Result:    Display EasySetup Step
    """
    def setUp(self):
        print("Initialization Test Environment")
        super(testcase_Basic_Check_Setup_0001, self).setUp()
        # jp_model_action_util.init_focus_location()

    def tearDown(self):
        super(testcase_Basic_Check_Setup_0001, self).tearDown()

    def testcase_Basic_Check_Setup_0001(self):
        # print ("Step1: Enter into Setup screen")
        # jp_model_action_util.go_setup(False)
        #
        # print ("Step2: Factory Resetting/All Resetting")
        # jp_model_action_util.go_all_resetting()
        #
        # print ("Step3: Power Off")
        # jp_model_action_util.go_power_off()
        #
        # print ("Step4: Power On")
        # jp_model_action_util.go_power_on()

        print ("Step5: Display EasySetup Step")
        self.assertTrue(check_result.check_pictures('EasyDisplaySettings.png',type='JP'),
                        'EasySetup Step Not Displayed')

        # print ("Step6: Finish EasySetup Step")
        # jp_model_action_util.go_finish_easySetup_step()
        #
        # print ("Step7: Select Setup Button")
        # jp_model_action_util.go_setup()
        #
        # print ("Step8: Display Setup List Items")
        # self.assertTrue(check_result.check_pictures('Setup.png',type='JP'),
        #                 'Setup List Items Not Displayed')
        #
        # print ("Step9: Choose One Setting Item And "
        #        "Change The Option Value To Another(not default)")
        # jp_model_action_util.change_HDR_output()
        # self.assertTrue(check_result.check_pictures('HDR_Output_Off.png',type='JP'),
        #                 'Change The Option Value To Another(not default) Failed')
        #
        # print ("Step10: Enter Into Resettings To Do All Resetting")
        # jp_model_action_util.go_home()
        # jp_model_action_util.go_setup()
        # jp_model_action_util.go_all_resetting()
        #
        # print ("Step11: Return To This Setting Item")
        # jp_model_action_util.go_home()
        # jp_model_action_util.go_setup()
        # jp_model_action_util.go_HDR_output()
        #
        # print ("Step12: The Value Change To Default")
        # self.assertTrue(check_result.check_pictures('HDR_Output_Auto.png',type='JP'),
        #                 'The Value Not Change To Default')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_Setup_0001)
    runner.run(suite)