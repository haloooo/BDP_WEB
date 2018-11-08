# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import sys,os
import unittest
import xmlrunner
sys.path.insert(0, os.getcwd())
from BDP.config import constants
from BDP.common import qw_model_action_util, base_case, check_result

class testcase_Basic_Check_Setup_WiredWireless_0002(base_case.BaseCase):
    """
    Excel:              Basic_Check_Setup_WiredWireless.xlsx
    Category:           Wired & Wireless
    Test case:          1) Setup BDP Wired connection.
                        2) Retrive Internet Service List.
                        3) Play any network service (E.g: Youtube)

    Expected Result:    Confirm Local connection & Network access both OK.
                        Retrive Network Service List successful.
                        Playback OK.
    """
    def setUp(self):
        print("Initialization Test Environment")
        super(testcase_Basic_Check_Setup_WiredWireless_0002, self).setUp()

    def tearDown(self):
        super(testcase_Basic_Check_Setup_WiredWireless_0002, self).tearDown()

    def testcase_Basic_Check_Setup_WiredWireless_0002(self):
        print ("Step1: Enter Into Setup screen")
        qw_model_action_util.go_home()
        qw_model_action_util.go_setup()

        print ("Step2: Enter Into Network Setting")
        qw_model_action_util.go_network_setting()

        print ("Step3: Enter Into Internet Settings")
        qw_model_action_util.go_internet_settings()

        print ("Step4: Retrive Internet Service List")
        qw_model_action_util.set_wireless_setup()
        qw_model_action_util.go_right_wireless()
        qw_model_action_util.config_wireless_setup()

        # print ("Step5: Play any network service (E.g: Digital Concert Hall)")
        # qw_model_action_util.go_digital_concert_hall()
        # self.assertTrue(check_result.check_pictures('Digital_Concert.png'),
        #                 'Play network service Digital Concert Hall Failed')

if __name__ == '__main__':
    xmlpath = constants.log_dir
    runner = xmlrunner.XMLTestRunner(output=xmlpath, stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase_Basic_Check_Setup_WiredWireless_0002)
    runner.run(suite)