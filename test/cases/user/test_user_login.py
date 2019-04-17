import unittest  # 导入unittest
import json
import requests
from data.read_excel import get_test_data,excel_to_lists
from log.logger import *
from test.test_base import TestBase

class TestUserLogin(TestBase): 

    def test_user_login_normal(self):  

        data=get_test_data(self.data_list,'test_user_login_normal')  
        res = self.send_request(data)
        self.assertIn(res.text,data['expect_res'],'The text should be 登陆成功')  
        
    def test_user_login_password_wrong(self):
        data=get_test_data(self.data_list,'test_user_login_password_wrong')
        res = self.send_request(data)
        self.assertIn(res.text,data['expect_res'],'The text should be 失败..')
        
if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别
