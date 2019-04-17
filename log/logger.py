import logging
import json

logging.basicConfig(level=logging.INFO,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式

def log_case_info(case_name,url,data,expect_res,atc_res):
    if isinstance(data,dict):
        data=json.dumps(data,ensure_ascii=False)
    logging.info('TestCase:{}'.format(case_name))
    logging.info('Url :{}'.format(url))
    logging.info('Data ：'+ data)
    logging.info('Expect result :{}'.format(expect_res))
    logging.info('Actually result:{}'.format(atc_res))
    