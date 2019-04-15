import unittest
from HTMLTestReportCN import HTMLTestRunner
from mail.email_config import send_email

# suite = unittest.defaultTestLoader.discover("./")

# f = open("report.html", 'wb')  # 二进制写格式打开要生成的报告文件
# HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
# f.close()
suite = unittest.defaultTestLoader.discover("./")
with open("report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
send_email('report.html')  # 发送邮件
