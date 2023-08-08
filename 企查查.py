# note：企查查批量查询接口，可以获取多条企业信息，且速度较快
import json
import re
import hmac
import time
import hashlib
import requests,datetime,pandas as pd
from sys import stderr
from logging import *
### 日志
logger = getLogger(f'企查查_{datetime.datetime.now()}')
logger.setLevel(INFO)
rf_handler = StreamHandler(stderr)  # 默认是sys.stderr
rf_handler.setLevel(DEBUG)
f2_handler = FileHandler(f'logs/企查查.log')
f2_handler.setLevel(INFO)
f2_handler.setFormatter(Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
f3_handler = FileHandler(f'logs/企查查.error.log')
f3_handler.setLevel(ERROR)
f3_handler.setFormatter(Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
logger.addHandler(rf_handler)
logger.addHandler(f2_handler)
logger.addHandler(f3_handler)

def get_pid_tid():
    url = 'https://www.qcc.com/web/search/advance?hasState=true'

    headers = {
        'accept-encoding': 'gzip, deflate, br'
        ,'accept-language': 'zh-CN,zh;q=0.9'
        ,'cache-control': 'max-age=0'
        ,'cookie': cookie
        ,'referer': 'https://www.qcc.com/'
        ,'sec-fetch-dest': 'document'
        ,'sec-fetch-mode': 'navigate'
        ,'sec-fetch-site': 'same-origin'
        ,'sec-fetch-user': '?1'
        ,'upgrade-insecure-requests': '1'
        ,'user-agent': useragent
    }

    res = requests.get(url, headers=headers).text
    try:
        pid = re.findall("pid='(.*?)'", res)[0]
        tid = re.findall("tid='(.*?)'", res)[0]
    except:
        pid = ''
        tid = ''

    return pid, tid

def seeds_generator(s):
    seeds = {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
    seeds_n = 20

    if not s:
        s = "/"
    s = s.lower()
    s = s + s

    res = ''
    for i in s:
        res += seeds[str(ord(i) % seeds_n)]
    return res

def a_default(url: str = '/', data: object = {}):
    url = url.lower()
    dataJson = json.dumps(data, ensure_ascii=False, separators=(',', ':')).lower()

    hash = hmac.new(
        bytes(seeds_generator(url), encoding='utf-8'),
        bytes(url + dataJson, encoding='utf-8'),
        hashlib.sha512
    ).hexdigest()
    return hash.lower()[8:28]

def r_default(url: str = '/', data: object = {}, tid: str = ''):
    url = url.lower()
    dataJson = json.dumps(data, ensure_ascii=False, separators=(',', ':')).lower()

    payload = url + 'pathString' + dataJson + tid
    key = seeds_generator(url)

    hash = hmac.new(
        bytes(key, encoding='utf-8'),
        bytes(payload, encoding='utf-8'),
        hashlib.sha512
    ).hexdigest()
    return hash.lower()
def qccspider(name:str):
    '''
    企查查
    公司名字或统一社会信用代码查询企业详细数据
    一个号500
    '''
    url = 'https://www.qcc.com/api/search/searchMulti'
    data = {'searchKey':name,'pageIndex':1,'pageSize':1}
    pid, tid = get_pid_tid()
    headers = {
        'accept': 'application/json, text/plain, */*'
        ,'accept-encoding': 'gzip, deflate, br'
        ,'accept-language': 'zh-CN,zh;q=0.9'
        ,'content-length': '141'
        ,'content-type': 'application/json'
        ,'cookie': cookie
        ,'origin': 'https://www.qcc.com'
        ,'referer': 'https://www.qcc.com/web/search/advance?hasState=true'
        ,'sec-fetch-dest': 'empty'
        ,'sec-fetch-mode': 'cors'
        ,'sec-fetch-site': 'same-origin'
        ,'user-agent': useragent
        ,'x-requested-with': 'XMLHttpRequest'
    }

    headers['x-pid'] = pid
    req_url = '/api/search/searchMulti'
    key = a_default(req_url, data)
    val = r_default(req_url, data, tid)
    headers[key] = val
    response = requests.post(url=url, headers=headers, json=data)
    try:
        res=response.json().get('Result')[0]
    except Exception as e:
        raise Exception(response.text)
    response.close()
    return res

if __name__ == '__main__':
    # user_cookie
    # 用户cookie，填写自己的用户cookie,useragent
    cookie = 'QCCSESSID=0dc43bac634c1da2146863b6a0; qcc_did=28fbb9c7-9dff-4aa5-ad18-b0acb3aa5dc3; UM_distinctid=189ab2a377a1a9-07e28810505d32-26031c51-1fa400-189ab2a377b16d3; acw_tc=3d808d2516913942121652333eab003c37d4bb2abfa64710822ec96190; CNZZDATA1254842228=825759271-1690793169-https%253A%252F%252Fwww.baidu.com%252F%7C1691393956'
    useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36' 
    ### 文件信用代码的字段名
    key_name='firm_code'
    ### 字段名
    columns=[key_name,'firm_name_qcc','ope_scope_qcc','ind_econ_code_qcc','ind_econ_name_qcc']
    Result=pd.DataFrame(columns=columns)
    ### 是否从错误处继续
    index_in_error_file=True
    ### 是否跳过错误
    skip_error=False
    index=0
    
    if index_in_error_file:
        try:
            with open('logs/qcc_index.txt','r') as f:
                content=f.read()
                if content:
                    index=int(content)
            Result=pd.read_excel('output/企查查.xlsx')
        except:
            index=0
    if skip_error:
        index+=1
    ### 读取文件并去重
    df=pd.read_excel('input/名单匹配.xlsx').drop_duplicates()
    
    ### 查询列表
    key_list=df[key_name].values.tolist()
    length=len(key_list)
    logger.info(f'读取到{length}条数据，企查查爬虫开始！')
    ### 初始化需要获取的字段
    try:
        for key in key_list[index:]:
            ### 初始化结果
            res={
                'firm_code':key,
                'firm_name_qcc':None,
                'ope_scope_qcc':None,
                'ind_econ_code_qcc':None,
                'ind_econ_name_qcc':None
            }
            logger.info(f'{key}开始爬取-{index+1}/{length}')
            try:
                data=qccspider(key)
                logger.info(f'{key}爬取成功-{data.get("Name")}')
                ### 填充需要获取的字段
                res['firm_name_qcc']=data.get('Name')
                res['ope_scope_qcc']=data.get('Scope')
                res['ind_econ_code_qcc']=data.get('Industry',{}).get('IndustryCode')
                res['ind_econ_name_qcc']=data.get('Industry',{}).get('Industry')
                index+=1
                Result=Result.append([res])
                Result.to_excel('output/企查查.xlsx',index=False) 
            except IndexError:
                ### 未查询的到的数据
                logger.warning(f'{key}爬取失败-{index+1}/{length}-error:未查询到数据')
                index+=1
                Result=Result.append([res])
                Result.to_excel('output/企查查.xlsx',index=False) 
            except Exception as e:
                ### 未知错误，可能被反爬
                logger.error(f'{key}爬取失败-{index+1}/{length}-error:{e}')
                raise e  
            finally:
                with open('logs/qcc_index.txt','w') as f:
                    f.write(str(index))
                time.sleep(10)  
    except:
        pass
    logger.info(f'爬取到{index}条数据，保存成功！')
    logger.info(f'爬取完毕-{length}条数据')