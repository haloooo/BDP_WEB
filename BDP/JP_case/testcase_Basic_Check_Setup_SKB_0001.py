# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys, os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import jp_model_action_util, base_case, check_result

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
        jp_model_action_util.go_setup()
        # 2.确保resetting成功
        jp_model_action_util.go_all_resetting()
        super(testcase_Basic_Check_Setup_SKB_0001, self).setUp()

    def tearDown(self):
        # 确保退出至HOME界面
        jp_model_action_util.send_key('RETURN')
        super(testcase_Basic_Check_Setup_SKB_0001, self).tearDown()

    def testcase_Basic_Check_Setup_SKB_0001(self):
        print ("Step1: Enter into Setup screen")
        jp_model_action_util.go_home()
        jp_model_action_util.go_setup()

        print ("Step2: Enter into System Settings / Device Name")
        jp_model_action_util.go_system_setting()
        jp_model_action_util.go_device_name()

        print ("Step3: Enter A Device Name And Press Enter")
        jp_model_action_util.enter_device_name()
        jp_model_action_util.save_device_name()
        self.assertTrue(check_result.check_pictures('Device_Name.png',type='JP'),
                        'The input word has not been saved')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_Setup_SKB_0001)
    runner.run(suite)