import unittest
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./")

f = open("report.html", 'wb')  # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
f.close()
