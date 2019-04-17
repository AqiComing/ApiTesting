import logging
import json

logging.basicConfig(level=logging.INFO,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.log',  # 日志输出文件
                    filemode='a')  # 追加模式

def log_case_info(case_name,url,args,expect_res,atc_res):
    if isinstance(args,dict):
        args=json.dumps(args,ensure_ascii=False)
    a='Expect result :{}'.format(expect_res)
    b='Args: {}'.format(args)
    logging.info(a)
    logging.info(b)
    logging.info('Actually result:{}'.format(atc_res))
    logging.info('TestCase:{}'.format(case_name))
    logging.info('Url :{}'.format(url))
    # logging.info('Args: {}'.format(args))
    
    