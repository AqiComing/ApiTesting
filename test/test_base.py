import unittest
import sys
import requests
from data.read_excel import *
from log.logger import*

sys.path.append("../..")

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.__name__!='TestBase':
            cls.data_list=excel_to_lists(cls.__name__)

    def get_case_data(self,case_name):
        return get_test_data(self.data_list,case_name)
        
    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        if method.upper() == 'GET':   # GET类型请求
            log_case_info(case_name, url, json.dumps(args), expect_res, res.text)
            res = requests.get(url=url, params=json.loads(args))
        elif data_type.upper() == 'FORM':   # 表单格式请求
            res = requests.post(url=url, data=json.loads(args), headers=json.loads(headers))
            log_case_info(case_name, url, args, expect_res, res.text)
        else:
            log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))   # JSON格式请求
            
        return res
