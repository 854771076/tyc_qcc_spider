## 天眼查企查查爬虫

> v1.0.0

#### 使用介绍

1. 将需要爬取的企业名称或企业信用代码写入`input/`路径下的`名单匹配.xlsx`文件中
2. 在`天眼查.py或企查查.py`文件中解析需要获取的数据（data变量是返回数据的字典）

```python
#企查查
{'KeyNo': 'be50b64d3c9c6b005d2fee9dd22342b2',
 'Name': '惠州市金驰包装科技有限公司',
 'Type': 0,
 'No': '',
 'CreditCode': '<em>91441322MA54PAMH2C</em>',
 'OperName': '罗长云',
 'Status': '在营（开业）企业',
 'StartDate': 1589990400000,
 'Address': '博罗县石湾镇源头乡茹卢村',
 'RegistCapi': '200万元人民币',
 'ContactNumber': '15119045398',
 'Email': '1064825743@qq.com',
 'ImageUrl': 'https://image.qcc.com/auto/be50b64d3c9c6b005d2fee9dd22342b2.jpg?x-oss-process=style/logo_200&shortName=%E9%87%91%E9%A9%B0%E5%8C%85%E8%A3%85&color=E5BF72',
 'TelList': '[]',
 'IsAuth': False,
 'OperInfo': '{"k":"pr11ae3d8fd890e08feaf47a286bf8f7","o":2,"t":1,"h":false}',
 'TagsInfo': None,
 'Flag': '3\tAC\tCR\tE\tensh.22\tensh.22.6\tensh.22.6.2\tEPE\tFBT\tGT\tMN\tP\tPT\tRS\tRSRK\tRY_2020\tRY_2021\tRY_2022\tSCALE_3\tSME\tT\tTP_FXTP\tTP_GLF\tTP_GQCT\tTP_GQFB\tTP_GQJG\tTP_GXTP\tTP_QYTP\tTP_SYGD\tVMN\tVT',
 'Tag': '包装\t传统行业\t轻工制造',
 'EmailList': [],
 'AuthLevel': -1,
 'IsHide': False,
 'AreaCode': '4413\t441322',
 'QccCode': '',
 'GW': '',
 'CountInfo': [{'k': '5', 'v': '[{"k":"15119045398","v":"1"}]'},
  {'k': '7', 'v': '80'},
  {'k': '9',
   'v': '[{"k":"pr11ae3d8fd890e08feaf47a286bf8f7","n":"罗长云","o":2,"j":"执行董事,经理,财务负责人","bp":1}]'},
  {'k': '10',
   'v': '{"OperType":1,"OperList":[{"k":"pr11ae3d8fd890e08feaf47a286bf8f7","n":"罗长云","o":2,"h":false}]}'},
  {'k': '13', 'v': '23'},
  {'k': '28', 'v': '{"A":"QCC03","B":"QCC0307,QCC030702,QCC03070211"}'},
  {'k': '30', 'v': '001001001,001001001001,002006'},
  {'k': '32', 'v': '小型企业'},
  {'k': '35', 'v': '{"TermStart":1589990400,"TermEnd":0}'},
  {'k': '10013', 'v': '23'}],
 'Industry': {'IndustryCode': 'M',
  'Industry': '科学研究和技术服务业',
  'SubIndustryCode': '74',
  'SubIndustry': '专业技术服务业',
  'MiddleCategoryCode': '749',
  'MiddleCategory': '工业与专业设计及其他专业技术服务'},
 'EconKind': '有限责任公司（自然人独资）',
 'QccIndustry': {'Ac': 'QCC03',
  'An': '工业',
  'Bc': 'QCC0307',
  'Bn': '商贸服务',
  'Cc': 'QCC030702',
  'Cn': '商业服务与用品',
  'Dc': 'QCC03070211',
  'Dn': '其他商业服务'},
 'TagsInfoV2': [{'Type': 505,
   'Name': '小微企业',
   'ShortName': '',
   'DataExtend': ''}],
 'ShortStatus': '在业',
 'Introduction': '',
 'IsIndividual': False,
 'HitReason': {'Field': '统一社会信用代码', 'Value': '<em>91441322MA54PAMH2C</em>'},
 'HitReasons': [{'Field': '统一社会信用代码', 'Value': '<em>91441322MA54PAMH2C</em>'},
  {'Field': '纳税人识别号', 'Value': '<em>91441322MA54PAMH2C</em>'}],
 'Scale': '小型企业',
 'TermStart': 1589990400,
 'TermEnd': 0,
 'Area': {'Province': '',
  'CityCode': '4413',
  'City': '惠州市',
  'CountyCode': '441322',
  'County': '博罗县'},
 'X': 23.158265572497825,
 'Y': 113.95700486671622}
```

```python
#天眼查
{'id': 3439661956,
 'name': '惠州市金驰包装科技有限公司',
 'type': 1,
 'matchType': '信用代码匹配',
 'base': '广东',
 'legalPersonName': '罗长云',
 'estiblishTime': '2020-05-21 00:00:00.0',
 'regCapital': '200万人民币',
 'regStatus': '存续',
 'score': '61',
 'orginalScore': '6150',
 'bonusScore': '0',
 'companyScore': '61',
 'historyNames': '',
 'categoryCode': '',
 'industry': None,
 'humanNames': '罗长云\t:#0\t;\t廖金桥\t:#0\t;\t罗 长云\t:#1\t;\t',
 'trademarks': None,
 'tmList': None,
 'productList': None,
 'usedBondName': None,
 'bondName': None,
 'bondNum': None,
 'bondType': None,
 'newtestName': None,
 'regNumber': '441322000330103',
 'orgNumber': 'MA54PAMH-2',
 'creditCode': '91441322MA54PAMH2C',
 'businessScope': '研发;生产;销售;包装制品;包装材料;纸塑设备及配件',
 'regLocation': '博罗县石湾镇源头乡茹卢村',
 'phone': '15119045398',
 'phoneList': ['15119045398'],
 'phoneInfoList': [{'number': '15119045398',
   'type': '1',
   'source': None,
   'comment': '号码可正常联系'}],
 'businessItemList': None,
 'phoneNum': '15119045398',
 'logo': '',
 'city': '惠州市',
 'district': '博 罗县',
 'emails': '1064825743@qq.com',
 'emailList': ['1064825743@qq.com'],
 'websites': '',
 'hiddenPhones': None,
 'abbr': '',
 'tagList': None,
 'companyType': 1,
 'companyOrgType': '有限责任公司\t;\t有限责任公司(自 然人独资)',
 'labelList': None,
 'matchField': {'field': '信用代码', 'content': '<em>91441322MA54PAMH2C</em>'},
 'latitude': None,
 'longitude': None,
 'legalPersonId': '2115107679',
 'legalPersonType': '1',
 'distance': None,
 'categoryStr': '造纸和纸制品业',
 'isClaimed': 0,
 'claimPkgType': None,
 'realClaimPkgType': None,
 'baiduUrl': None,
 'isBranch': 0,
 'alias': '金驰包装',
 'claimInfo': None,
 'hidden': 0,
 'legalPersonShowStr': '法定代表人',
 'regCapitalShowStr': '注册资本',
 'estiblishTimeShowStr': '成立日期',
 'multiMatchField': [{'field': '信用代码',
   'content': '<em>91441322MA54PAMH2C</em>'}],
 'labelListV2': ['小微企业'],
 'labelJsonList': ['{"type":1,"value":"小微企业"}'],
 'taxCode': '91441322MA54PAMH2C',
 'socialSecurityStaff_num': '1',
 'categoryCodeStd': '223',
 'hasMorePhone': None,
 'hasVideo': None,
 'videoId': None,
 'isRecommend': None,
 'englishName': None,
 'firstPositionShowStr': '法定代表人',
 'secondPositionShowStr': '注册资本',
 'firstPositionValue': '罗长云',
 'secondPositionValue': '200万人民币',
 'contantMap': {'recallSrc': 'ES',
  'param_reg_capital': '200.0',
  'establish_time_long': '1589990400000'}}
```

3. 天眼查每天上线10000次访问，企查查每个cookie上线500次访问
