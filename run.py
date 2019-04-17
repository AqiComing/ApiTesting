import unittest
from HTMLTestReportCN import HTMLTestRunner
from mail.send_email import send_email
from test.suite.test_suites import *
import sys
import os
import logging

sys.path.append("../..")

base_dir=os.path.dirname(__file__)
test_case_path = os.path.join(base_dir,'test/cases/user')
suite=unittest.TestSuite()

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)

def run(suite):
    logging.info("=========Testing start=======")
    with open("report.html", 'wb') as f:  # 改为with open 格式
        HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="Nick").run(suite)
    logging.info("=========Test compelted=======")

def run_all():
    run(discover())

def run_suite(suite_name):
    suite=get_suite(suite_name)
    if suite:
        run(suite)
    else:
        logging.error("There is no test case to run")
run_all()
send_email('report.html')  # 发送邮件
