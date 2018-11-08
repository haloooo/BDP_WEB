# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018

import sys,os
import unittest
sys.path.insert(0, os.getcwd())
from BDP.common import qw_model_action_util


class BaseCase (unittest.TestCase):
    # 运行初始时检查
    def setUp(self):
        pass

    # 运行结束时检查
    def tearDown(self):
        qw_model_action_util.send_key('HOME')

    def assertResult(self,responselist,errormsg):
        pass

if __name__ == "__main__":
    unittest.main()
