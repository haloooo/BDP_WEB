# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys, os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import jp_model_action_util, base_case, check_result

class testcase_Basic_Check_for_System_Team_0001(base_case.BaseCase):
    """
    Excel:              Basic Check for System Team.xlsx
    Category:           Child Lock
    Test case:          1) Set is in HomeUI
                        2) Press STOP + HOME + TOP MENU in remote key
                        3) Child Lock mode will be enable

    Expected Result:    Child Lock Mode On"" pop up message is appear
                        Confirm Eject key is disabled"
    """
    def setUp(self):
        print("Initialization Test Environment")
        # super(testcase_Basic_Check_for_System_Team_0001, self).setUp()
        # # 1. 进入Home UI界面
        # jp_model_action_util.send_key('HOME')
        # # 2. 进入Setup界面
        # jp_model_action_util.go_setup()
        # # 3.确保resetting成功
        # jp_model_action_util.go_all_resetting()
        # jp_model_action_util.send_key('HOME')

    def tearDown(self):
        super(testcase_Basic_Check_for_System_Team_0001, self).tearDown()

    def testcase_Basic_Check_for_System_Team_0001(self):
        print ("Step1: Enter Into HomeUI")
        jp_model_action_util.go_home()

        print ("Step2: Press STOP + HOME + TOP MENU in remote key")
        jp_model_action_util.set_different_mode("Child Lock")

        print ("Step3: \"Child Lock Mode On\" pop up message is appear")
        self.assertTrue(check_result.check_pictures('Child_Lock_Pop_Up.png', False, 0.8 ,type='JP'),
                        '"Child Lock Mode On" pop up message is not appear')

        print ("Step4: Confirm Eject key is disabled")
        jp_model_action_util.send('OPEN')
        self.assertTrue(check_result.check_pictures('Child_Lock_Eject_Key.png', False, 0.8,type='JP'),
                        'Eject key is not disabled')

        print ("Step5: Cancel The Child Look Mode")
        jp_model_action_util.set_different_mode("Child Lock")

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_for_System_Team_0001)
    runner.run(suite)