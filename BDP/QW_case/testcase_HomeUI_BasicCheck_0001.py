# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys,os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import qw_model_action_util, base_case, check_result

class testcase_HomeUI_BasicCheck_0001(base_case.BaseCase):
    """
    Excel:              HomeUI_BasicCheck.xlsx

    Pre-condition:      - Destination: US, Language: English.
                        - Complete All&Personal Settings resetting.
                        - Power is ON.

    Category:           Favorite Key

    Test case:          1) On All Apps screen, press [OPTION] key on an app, select "Register as Favorite".
                        2) On BDP Home screen, press [FAVORITE] key.

    Expected Result:    Register favorite app works normal.
                        Launch favorite app works normal.
    """
    def setUp(self):
        print("Initialization Test Environment")
        super(testcase_HomeUI_BasicCheck_0001, self).setUp()
        qw_model_action_util.init_focus_location()

    def tearDown(self):
        super(testcase_HomeUI_BasicCheck_0001, self).tearDown()

    def testcase_HomeUI_BasicCheck_0001(self):
        print ('Step1: On All Apps screen, press [OPTION] key on an app, select "Register as Favorite"')
        qw_model_action_util.register_as_favorite()
        # self.assertTrue(check_result.check_pictures('Register_as_Favorite.png'),
        #                 'select "Register as Favorite" Failed')

        print ('Step2: On BDP Home screen, press [FAVORITE] key')
        qw_model_action_util.pressKey()

        print ('Step3: Launch favorite app works normal')
        # self.assertTrue(check_result.check_pictures('Open_Favorite.png'),
        #                 'Launch favorite app works abnormal')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_HomeUI_BasicCheck_0001)
    runner.run(suite)