import requests,datetime,pandas as pd,time
from sys import stderr
from logging import *
from settings import *
### 日志
logger = getLogger(f'天眼查_{datetime.datetime.now()}')
logger.setLevel(INFO)
rf_handler = StreamHandler(stderr)  # 默认是sys.stderr
rf_handler.setLevel(DEBUG)
f2_handler = FileHandler(f'logs/天眼查.log')
f2_handler.setLevel(INFO)
f2_handler.setFormatter(Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
f3_handler = FileHandler(f'logs/天眼查.error.log')
f3_handler.setLevel(ERROR)
f3_handler.setFormatter(Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
logger.addHandler(rf_handler)
logger.addHandler(f2_handler)
logger.addHandler(f3_handler)
def sreach_detailed(name:str)->dict:
    '''
    可用企业名称、统一社会信用代码查询
    异步大批量返回会反爬
    目前采用同步爬取
    10000次请求
    '''
    AUTHORIZATION = '0###oo34J0VKzLlpdvf8kgFkMlfU_IPY###1642087379312###22494f3155c2e5a4be76e503837fa439'
    """ 请求token """
    X_AUTH_TOKEN = "eyJkaXN0aW5jdF9pZCI6IjE3ZDFjNWVhMzZjNGY2LTA5ZjU2NWUwNWViNTZjLTFjMzA2ODUxLTIwNzM2MDAtMTdkMWM1ZWEzNmRiMzYiLCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS4xNS4yNCJ9LCJwcm9wZXJ0aWVzIjp7IiR0aW1lem9uZV9vZmZzZXQiOi00ODAsIiRzY3JlZW5faGVpZ2h0IjoxMDgwLCIkc2NyZWVuX3dpZHRoIjoxOTIwLCIkbGliIjoianMiLCIkbGliX3ZlcnNpb24iOiIxLjE1LjI0IiwiJGxhdGVzdF90cmFmZmljX3NvdXJjZV90eXBlIjoi6Ieq54S25pCc57Si5rWB6YePIiwiJGxhdGVzdF9zZWFyY2hfa2V5d29yZCI6IuacquWPluWIsOWAvCIsIiRsYXRlc3RfcmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsImN1cnJlbnRfdXJsIjoiaHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vc2VhcmNoP2tleT0lRTYlOUQlQUQlRTUlQjclOUUlRTYlOTklQUUlRTUlODUlQjQlRTQlQkMlODElRTQlQjglOUElRTclQUUlQTElRTclOTAlODYlRTUlOTAlODglRTQlQkMlOTklRTQlQkMlODElRTQlQjglOUEiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LnRpYW55YW5jaGEuY29tL3NlYXJjaD9rZXk9JUU2JTlEJUFEJUU1JUI3JTlFJUU2JTk5JUFFJUU1JTg1JUI0JUU0JUJDJTgxJUU0JUI4JTlBJUU3JUFFJUExJUU3JTkwJTg2JUU1JTkwJTg4JUU0JUJDJTk5JUU0JUJDJTgxJUU0JUI4JTlBIiwidHljaWQiOiI0MmMxZTY1MDQ0ZjYxMWVjYmIxZDY3ZmJiYzEwN2U3NSIsIm5hbWUiOiLmna3lt57mma7lhbTkvIHkuJrnrqHnkIblkIjkvJnkvIHkuJoiLCJtb2R1bGUiOiLkvJjotKjlrp7lkI3orqTor4EiLCIkaXNfZmlyc3RfZGF5IjpmYWxzZX0sImFub255bW91c19pZCI6IjE3ZDFjNWVhMzZjNGY2LTA5ZjU2NWUwNWViNTZjLTFjMzA2ODUxLTIwNzM2MDAtMTdkMWM1ZWEzNmRiMzYiLCJ0eXBlIjoidHJhY2siLCJldmVudCI6InNlYXJjaF9yZXN1bHRfZXhwdXJlIiwiX3RyYWNrX2lkIjo3MjUyNDM3Mjd9"
    headers={
     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "version": "TYC-XCX-WX",
    "Host": "api9.tianyancha.com",
    "Authorization": AUTHORIZATION,
    'x-auth-token': X_AUTH_TOKEN
    }
    #天眼查搜索api接口url
    url=f'https://api9.tianyancha.com/services/v3/search/sNorV3/{name}'
    #获取json字符串
    response=requests.get(url,headers=headers)
    try:
        data=response.json()['data']['companyList'][0]
        response.close()
    except IndexError:
        raise IndexError()
    except:
        raise Exception(response.text)
    return data
if __name__ == '__main__':
    ### 字段名
    columns=columns_tyc
    Result=pd.DataFrame(columns=columns)
    ### 是否从错误处继续
    index_in_error_file=True
    index=0
    
    if index_in_error_file:
        try:
            with open('logs/tyc_index.txt','r') as f:
                content=f.read()
                if content:
                    index=int(content)
            Result=pd.read_excel('output/天眼查.xlsx')
        except:
            index=0
    if skip_index:
        index+=1
    ### 读取文件并去重
    df=pd.read_excel(file_name).drop_duplicates()
    ### 查询列表
    key_list=df[key_name].values.tolist()
    length=len(key_list)
    logger.info(f'读取到{length}条数据，天眼查爬虫开始！')
    ### 初始化需要获取的字段
    try:
        for key in key_list[index:]:
            ### 初始化结果
            res={
                'firm_code':key,
                'firm_name_tyc':None,
                'ope_scope_tyc':None,
                'ind_econ_code_tyc':None,
                'ind_econ_name_tyc':None
            }
            logger.info(f'{key}开始爬取-{index+1}/{length}')
            try:
                data=sreach_detailed(key)
                logger.info(f'{key}爬取成功-{data.get("name")}')
                ### 填充需要获取的字段
                res['firm_name_tyc']=data.get('name')
                res['ope_scope_tyc']=data.get('businessScope')
                res['ind_econ_code_tyc']=data.get('categoryCodeStd')
                res['ind_econ_name_tyc']=data.get('categoryStr')
                index+=1
                Result=Result.append([res])
                Result.to_excel('output/天眼查.xlsx',index=False) 
            except IndexError:
                ### 未查询的到的数据
                logger.warning(f'{key}爬取失败-{index+1}/{length}-error:未查询到数据')
                index+=1
                Result=Result.append([res])
                Result.to_excel('output/天眼查.xlsx',index=False) 
            except Exception as e:
                ### 未知错误，可能被反爬
                logger.error(f'{key}爬取失败-{index+1}/{length}-error:{e}')
                raise e    
            finally:
                with open('logs/tyc_index.txt','w') as f:
                    f.write(str(index))
                time.sleep(timesleep) 
    except:
        pass
    logger.info(f'爬取到{index}条数据，保存成功！')
        
    logger.info(f'爬取完毕-{length}条数据')
    