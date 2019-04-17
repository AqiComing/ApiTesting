import unittest
import sys
sys.path.append("../..")
from test.cases.user.test_user_login import TestUserLogin
from test.cases.user.test_user_reg import TestUserReg

smoke_suite=unittest.TestSuite()
smoke_suite.addTests([TestUserLogin('test_user_login_normal'),TestUserReg('test_user_reg_normal')])
def get_suite(suite_name):
    return globals().get(suite_name)
