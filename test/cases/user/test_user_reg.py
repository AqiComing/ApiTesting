import unittest
import requests
from db import *
from test.test_base import TestBase
import json

# 数据准备
NOT_EXIST_USER = '范冰冰'
EXIST_USER = '张三'


class TestUserReg(TestBase):
    def test_user_reg_normal(self):
        case_data=self.get_case_data('test_user_reg_normal')
        name=json.load(case_data['args']).get('name')
        # 环境检查
        if check_user(name):
            del_user(name)

        # 发送请求
        res=self.send_request(case_data)

        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        except_res = {
            "code": "100000",
            "msg": "成功",
            "data": {
                "name": NOT_EXIST_USER,
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        }

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), except_res)

        # 数据库断言
        self.assertTrue(check_user(NOT_EXIST_USER))

        # 环境清理（由于注册接口向数据库写入了用户信息）
        del_user(NOT_EXIST_USER)

    def test_user_reg_exist(self):
        case_data=self.get_case_data('test_user_reg_exist')
        name=json.load(case_data['args']).get('name')
        # 环境检查
        if not check_user(EXIST_USER):
            add_user(EXIST_USER, '123456')

        # 发送请求
        res = self.send_request(case_data)

        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        except_res = {
            "code": "100001",
            "msg": "失败，用户已存在",
            "data": {
                "name": EXIST_USER,
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        }

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), except_res)

        # 数据库断言(没有注册成功，数据库没有添加新用户)

        # 环境清理（无需清理）


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # 运行所有用例
    t = TestUserReg()
    t.test_user_reg_normal()