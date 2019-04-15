import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.header import Header
from log.logger import *

def send_email(report_file):
    msg=MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))
    msg['From']='317401018@qq.com'
    msg['To'] = '317401018@qq.com' 
    msg['Subject'] = Header('接口测试报告', 'utf-8')
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)
    try:
        smtp = smtplib.SMTP_SSL('smtp.qq.com')  # smtp服务器地址 使用SSL模式
        smtp.login('317401018@qq.com', 'iptzeudeujtxbjhc')  #User name and smtp password
        smtp.sendmail("317401018@qq.com", "317401018@qq.com", msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
