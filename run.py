import unittest
import time
import sys
import os
import logging
import pickle
from HTMLTestReportCN import HTMLTestRunner
from mail.send_email import send_email
from test.suite.test_suites import *
from config.config import *


sys.path.append("../..")

base_dir=os.path.dirname(__file__)
test_case_path = os.path.join(base_dir,'test/cases/user')
suite=unittest.TestSuite()
# TODO
last_fails_file=os.path.join(base_dir,'test/cases/user')
testlist_file=os.path.join(base_dir,'test/cases/user')

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
        logging.error("The suit not exist")

def collect():
    suite=unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for test in tests:
                    _collect(test)
        else:
            suite.addTest(tests)
    _collect(discover())                                                                                        
    return suite

def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time()-t0))

def makesuite_by_testlist(testlist_file):
    with open(testlist_file) as f:
        testlist=f.readlines()
    testlist=[i.strip() for i in testlist if not i.startswith("#")]

    suite=unittest.TestSuite()
    all_cases=collect()
    for case in all_cases:
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite

def makesuite_by_tag(tag):
    suite+unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suite.addTest(case)
        return suite

def save_failures(result,file):
    suite=unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])
    with open(file) as f:
        pickle.dump(suite,f)
def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb')as f:
        suite=pickle.load(f)
    run(suite)

def main():
    if options.collect_only:    # 如果指定了--collect-only参数
        collect_only()
    elif options.rerun_fails:    # 如果指定了--rerun-fails参数
        rerun_fails()
    elif options.testlist:    # 如果指定了--testlist参数
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:  # 如果指定了--testsuite=***
        run_suite(options.testsuite)
    elif options.tag:  # 如果指定了--tag=***
        run(makesuite_by_tag(options.tag))
    else:   # 否则，运行所有用例
        run_all()

    
# 
# send_email('report.html')  # 发送邮件
if __name__ == '__main__':
    main()   # 调用main()
