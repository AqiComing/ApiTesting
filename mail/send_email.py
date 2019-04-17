import smtplib
import yaml
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.header import Header
from log.logger import *

base_dir = os.path.dirname(os.path.dirname(__file__))
email_config_path=os.path.join(base_dir,'mail\emai_config.yaml')

def send_email(report_file):
    with open(email_config_path,'r',encoding='utf-8')as file:
        email_datas=yaml.safe_load(file)

    msg=MIMEMultipart()
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))
    msg['From']=email_datas['From']
    msg['To'] = email_datas['To'] 
    msg['Subject'] = Header(email_datas['Subject'], 'utf-8')
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)
    try:
        smtp = smtplib.SMTP_SSL('smtp.qq.com')  # smtp服务器地址 使用SSL模式
        smtp.login(email_datas['From'], 'iptzeudeujtxbjhc')  #User name and smtp password
        smtp.sendmail(email_datas['From'], email_datas['To'] , msg.as_string())
        logging.info("Email send successed!")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
