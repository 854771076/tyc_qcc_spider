# 企查查用户cookie，填写自己的用户cookie,useragent,一对可访问500次
cookie = 'QCCSESSID=0dc43bac634c1da2146863b6a0; qcc_did=28fbb9c7-9dff-4aa5-ad18-b0acb3aa5dc3; UM_distinctid=189ab2a377a1a9-07e28810505d32-26031c51-1fa400-189ab2a377b16d3; acw_tc=3d808d2516913942121652333eab003c37d4bb2abfa64710822ec96190; CNZZDATA1254842228=825759271-1690793169-https%253A%252F%252Fwww.baidu.com%252F%7C1691393956'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36' 
#爬取速率
timesleep=5
### 是否跳过初始index
skip_index=False
### input文件中信用代码或企业名称的字段名
key_name='firm_code'
#天眼查字段名
columns_tyc=[key_name,'firm_name_tyc','ope_scope_tyc','ind_econ_code_tyc','ind_econ_name_tyc']
columns_qcc=[key_name,'firm_name_qcc','ope_scope_qcc','ind_econ_code_qcc','ind_econ_name_qcc']
#读取文件名
file_name='input/名单匹配.xlsx'