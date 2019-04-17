import unittest
from HTMLTestReportCN import HTMLTestRunner
from mail.send_email import send_email
import sys
import os

sys.path.append("../..")

base_dir=os.path.dirname(__file__)
test_case_path = os.path.join(base_dir,'test/cases/user')

suite = unittest.defaultTestLoader.discover(test_case_path)
with open("report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="Nick").run(suite)
send_email('report.html')  # 发送邮件
