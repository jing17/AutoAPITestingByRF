#-*-coding:utf-8-*-
import os
import robot
import MySQLdb
import MySQLdb.cursors
import random
import string
import md5
import json
import simplejson
import requests
import urllib
import time
from  datetime  import  *  
import time
import datetime
from urllib import quote
from urllib import unquote
from urllib import urlencode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from robot.libraries.BuiltIn import BuiltIn

try:
    from requests_ntlm import HttpNtlmAuth
except ImportError:
    pass

# 随机生成手机号码(大陆，香港，澳门)
def createPhone():
    prelist1=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","178","180","186","187","188"]
    Zone1='+86'
    phone1 =Zone1+"".join(random.choice(prelist1))+"".join(random.choice("0123456789") for i in range(8))
    #prelist2=["21","22","23","24","25","26","27","28","29","31","34","35","36","37","51","52","53","54","55","56","59","90","91","92","93","94","95","96","97","98"]
    #Zone2=random.choice(['+852','+853'])
    #phone2 =Zone2+"".join(random.choice(prelist2))+"".join(random.choice("0123456789") for i in range(6))
    #prelist3=["010","021","022","023","0335","0429","0571","0688","0701","0888","0943"]
    #Zone3='+86'
    #phone3 =Zone3+"".join(random.choice(prelist3))+"".join(random.choice("0123456789") for i in range(8))	
    return phone1
    
#随机生成客户名称
def createname():
    namelist1 = ['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨','朱','秦','尤','许','何','吕','施','张','孔','曹','严','华','金','魏','陶','姜','戚','谢','邹','喻','柏','水','窦','章','云','苏','潘','葛','奚','范','彭','郎','鲁','韦','昌','马','苗','凤','花','方','俞','任','袁','柳','酆','鲍','史','唐','费','廉','岑','薛','雷','贺','倪','汤','滕','殷','罗','毕','郝','邬','安','常','乐','于','时','傅','皮','卞','齐','康','伍','余','元','卜','顾','孟','平','黄','和','穆','萧','尹','姚','邵','湛','汪','祁','毛','禹','狄','米','贝','明','臧','计','伏','成','戴','谈','宋','茅','庞','熊','纪','舒','屈','项','祝','董','粱','杜','阮','蓝','闵','席','季','麻','强','贾','路','娄','危','江','童','颜','郭','梅','盛','林','刁','钟','徐','邱','骆','高','夏','蔡','田','樊','胡','凌','霍','虞','万','支','柯','昝','管','卢','莫','经','房','裘','缪','干','解','应','宗','丁','宣','贲','邓','郁','单','杭','洪','包','诸','左','石','崔','吉','钮','龚','程','嵇','邢','滑','裴','陆','荣','翁','荀','羊','於','惠','甄','麴','家','封','芮','羿','储','靳','汲','邴','糜','松','井','段','富','巫','乌','焦','巴','弓','牧','隗','山','谷','车','侯','宓','蓬','全','郗','班','仰','秋','仲','伊','宫','宁','仇','栾','暴','甘','钭','厉','戎','祖','武','符','刘','景','詹','束','龙','叶','幸','司','韶','郜','黎','蓟','薄','印','宿','白','怀','蒲','邰','从','鄂','索','咸','籍','赖','卓','蔺','屠','蒙','池','乔','阴','欎','胥','能','苍','双','闻','莘','党','翟','谭','贡','劳','逄','姬','申','扶','堵','冉','宰','郦','雍','舄','璩','桑','桂','濮','牛','寿','通','边','扈','燕','冀','郏','浦','尚','农','温','别','庄','晏','柴','瞿','阎','充','慕','连','茹','习','宦','艾','鱼','容','向','古','易','慎','戈','廖','庾','终','暨','居','衡','步','都','耿','满','弘','匡','国','文','寇','广','禄','阙','东','殴','殳','沃','利','蔚','越','夔','隆','师','巩','厍','聂','晁','勾','敖','融','冷','訾','辛','阚','那','简','饶','空','曾','毋','沙','乜','养','鞠','须','丰','巢','关','蒯','相','查','後','荆','红','游','竺','权','逯','盖','益','桓','公','万俟','司马','上官','欧阳','夏侯','诸葛','闻人','东方','赫连','皇甫','尉迟','公','澹台','公冶','宗政','濮阳','淳于','单于','太叔','申屠','公孙','仲孙','轩辕','令狐','钟离','宇文','长孙','慕容','鲜于','闾丘','司徒','司空','亓官','司寇','仉','督','子车','颛孙','端木','巫马','公西','漆雕','乐正','壤驷','公良','拓跋','夹谷','宰父','谷梁','晋','楚','闫','法','汝','鄢','涂','钦','段干','百里','东郭','南门','呼延','归','海','羊舌','微生','岳','帅','缑','亢','况','后','有','琴','梁丘','左丘','东门','西门','商','牟','佘','佴','伯','赏','南宫','墨','哈','谯','笪','年','爱','阳','佟','第五','言','福']
    namelist2 = ['梁','栋','维','启','克','伦','翔','旭','鹏','泽','晨','辰','士','以','建','家','致','树','炎','盛','雄','琛','钧','冠','策','腾','楠','榕','风','航','弘','义','兴','良','飞','彬','富','和','鸣','朋','斌','行','时','泰','博','磊','民','友','志','清','坚','庆','若','德','彪','伟','刚','勇','毅','俊','峰','强','军','平','保','东','文','辉','力','明','永','健','世','广','海','山','仁','波','宁','福','生','龙','元','全','国','胜','学','祥','才','发','武','新','利','顺','信','子','杰','涛','昌','成','康','星','光','天','达','安','岩','中','茂','进','林','有','诚','先','敬','震','振','壮','会','思','群','豪','心','邦','承','乐','绍','功','松','善','厚','裕','河','哲','江','超','浩','亮','政','谦','亨','奇','固','之','轮','翰','朗','伯','宏','言','蕊','薇','菁','梦','岚','苑','婕','馨','瑗','琰','韵','融','园','艺','咏','卿','聪','澜','纯','爽','琬','茗','羽','希','宁','欣','飘','育','滢','馥','筠','柔','竹','霭','凝','晓','欢','霄','伊','亚','宜','可','姬','舒','影','荔','枝','思','丽','芬','芳','燕','莺','媛','艳','珊','莎','蓉','眉','君','琴','毓','悦','昭','冰','枫','芸','菲','寒','锦','玲','秋','秀','娟','英','华','慧','巧','美','娜','静','淑','惠','珠','翠','雅','芝','玉','萍','红','月','彩','春','菊','兰','凤','洁','梅','琳','素','云','莲','真','环','雪','荣','爱','妹','霞','香','瑞','凡','佳','嘉','琼','勤','珍','贞','莉','桂','娣','叶','璧','璐','娅','琦','晶','妍','茜','黛','青','倩','婷','姣','婉','娴','瑾','颖','露','瑶','怡','婵','雁','蓓','纨','仪','荷','丹']
    name = random.choice(namelist1) + random.choice(namelist2)
    return name.decode('utf-8')

#随机生成客户性别
def createsex():
    #sexlist = ['先生','女士']
    sex = random.choice('12')
    return sex
    
#随机生成身份证号
def getdistrictcode(): 
    with open(r'D:\微云同步盘\493911445\同步盘\自动化测试\接口自动化\Resource\PublicLibrary\districtcode.txt'.decode('utf-8')) as file: 
        data = file.read() 
        districtlist = data.split('\n') 
    for node in districtlist: 
    #print node 
        if node[10:11] != ' ': 
            state = node[10:].strip() 
        if node[10:11]==' 'and node[12:13]!=' ': 
            city = node[12:].strip() 
        if node[10:11] == ' 'and node[12:13]==' ': 
            district = node[14:].strip() 
            code = node[0:6] 
            codelist.append({"state":state,"city":city,"district":district,"code":code})

def createIDcard(): 
    global codelist 
    codelist = [] 
    if not codelist:
        getdistrictcode()
    id = codelist[random.randint(0,len(codelist))]['code'] #地区项 
    id = id + str(random.randint(1930,2013)) #年份项 
    da = date.today()+timedelta(days=random.randint(1,366)) #月份和日期项 
    id = id + da.strftime('%m%d') 
    id = id+ str(random.randint(100,300))#，顺序号简单处理 
  
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项 
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射 
    for i in range(0,len(id)): 
        count = count +int(id[i])*weight[i] 
        id = id + checkcode[str(count%11)] #算出校验码 
        return id.decode('utf-8')
# print createPhone()
# print createname()
# print createsex()
#print createIDcard() 

#url编码String对象
def my_urlencode(str):
    reprStr = repr(str).replace(r'\x', '%')
    return reprStr[1:-1]

#MD5参数
def get_MD5_Value(string):
    mString = md5.new()
    mString.update(string)
    return mString.hexdigest()

#获取ak
def get_ak(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data') 
    AccessToken = dataStr.get("AccessToken") 
    return str(AccessToken)


#获取BrokerID
def get_BrokerID(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data') 
    BrokerID = dataStr.get("BrokerID") 
    return str(BrokerID)

#获取AdminID
def get_AdminID(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data') 
    CrmUserID = dataStr.get("CrmUserID") 
    return str(CrmUserID)

#获取message
def get_message(string):
    ret_dict = simplejson.loads(string)
    message = ret_dict.get('Message') 
    return str(message).decode('utf-8')
#获取带签名的URL
def get_relurl(string):
    if uri.find('?') != -1:
	uri = uri + '&' + "sign=" + sign.hexdigest()
    else:
        uri = uri + '?' + "sign=" + sign.hexdigest()
    return uri
	
#获取小区信息VillageCode
def get_VillageCode(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	VillageCode=dataStr[0].get('VillageCode')
	return str(VillageCode)
	
#获取城市名	
def get_CityName(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	CityName=dataStr[0].get('CityName')
	return str(CityName)
	
#获取小区信息	
def get_VillageName(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	VillageName=dataStr[0].get('VillageName')
	return str(VillageName).encode('utf-8')

def get_Code(string):
    ret_dict=simplejson.loads(string)
    dataStr=ret_dict.get('Code')
    return dataStr
	
def get_ItemCount(string):
    ret_dict=simplejson.loads(string)
    dataStr=ret_dict.get('Data')
    Count=dataStr.get('Count')
    return Count

def get_Address(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	Address=dataStr[0].get('Address')
	return str(Address).decode('utf-8')
	

def get_District(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	District=dataStr[0].get('AdminName')
	return str(District).decode('utf-8')
	
def get_BusinessName(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	BusinessName=dataStr[0].get('BusinessName')
	return str(BusinessName).decode('utf-8')
	
def get_Lat(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	Lat=dataStr[0].get('Lat')
	return str(Lat)

def get_Lng(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	Lng=dataStr[0].get('Lng')
	return str(Lng)

	
#获取楼幢信息	
def get_DongId(string):
    ret_dict=simplejson.loads(string)
    dataStr=ret_dict.get(u'Data')
    if dataStr==[]:
        return u'没有有效的楼幢单元'
    else:
        return dataStr[0].get(u'DongId')

def get_DongName():
    a=random.randint(1,50)
    b='幢'
    c=str(a)+str(b)
    return str(c).decode('utf-8')
	
def get_UnitName():
    a=random.randint(1,10)
    b=u'单元'
    c=str(a)+str(b)
    return str(c).decode('utf-8')
	

#def get_UnitName(string):
#    ret_dict=simplejson.loads(string)
#    dataStr=ret_dict.get('Data')
#    if dataStr==[]:
#        return "没有获取到楼幢信息"
#    else:
 #       return (dataStr[0].get('UnitName').split(',',1)[0])

#获取户型标签
def get_HouseType(string):
	ret_dict=simplejson.loads(string)
	dataStr=ret_dict.get('Data')
	LabelName=dataStr[0].get('LabelName')
	return LabelName
	
#获取房间全称
def get_RoomFullName(string,string1,string2,string3):
    RoomFullName=string+string1+str(string2)+u"层"+str(string3)+u"室"
	#print RoomFullName
    return RoomFullName
#获取随机房号	
def get_RoomNum	():
	a=random.choice('abcdefghijklmnopqrstuvwxyz')
	b=random.randint(0,999999)
	RoomNum=str(a)+str(b)
	return RoomNum
	
	

def get_Floor1():
    a=random.randint(1,25)
    b=random.randint(1,25)
    if a>=b:
        return b,a
    else:
        return a,b
		
def get_Floor():
	a=random.randint(1,10)
	return a
def get_TotalFloor():	
	b=random.randint(10,20)
	return b
#获取房源ID
def get_HouseID(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data') 
    HouseID = dataStr.get("Id") 
    return str(HouseID)
	
#获取客源ID
def get_CustomerID(string):
    ret_dict = simplejson.loads(string)
    CustomerID = ret_dict.get('Data')  
    return str(CustomerID)
	
#获取订单号
def get_OrderId(string):
	ret_dict=simplejson.loads(string)
	OrderId=ret_dict.get('Data')
	return str(OrderId)
	
#获取居室信息
def get_S():
    a=random.randint(1,6)
    return a

def get_T():
    a=random.randint(0,3)
    return a
	
def get_C():
    a=random.randint(0,2)
    return a
	
def get_W():
    a=random.randint(0,6)
    return a
def get_Y():
    a=random.randint(0,5)
    return a
	
def get_STCWY(str1,str2,str3,str4,str5):
	S=str1
	T=str2
	C=str3
	W=str4
	Y=str5
	STCWY=str(S)+'室'+str(T)+'厅'+str(C)+'厨'+str(W)+'卫'+str(Y)+'阳'
	return str(STCWY).decode('utf-8')
	
#获取价格
def get_SaleAmount():
    a=random.randint(60,1000)
    return a
	
def get_RentAmount():
    a=random.randint(1000,10000)
    return a
	
	
#获取面积
def get_Area():
    a=random.randint(10,500)
    b=random.randint(10,500)
    return (min(a,b),max(a,b))

#获取佣金
def get_commissionTotalPrice(a,b):
	hammerPrice=a
	commissionTotalPerc=b
	commissionTotalPrice="%.2f"%(a*b*100)
	return (commissionTotalPrice)
	
#评价满意度	
def get_Satisfaction():
    Satisfaction=random.randint(1,5)
    return Satisfaction
	
	
#获取房客源Id
#获取房客源Id
def get_HCId(string):
	#连接数据库
    conn= MySQLdb.connect(
        host='tops001rc.mysql.rds.aliyuncs.com',
        port = 3648,
        user='top_cjzs_dba',
        passwd='Upv5gZxZgnVmLg3K6xsD3heM6Zkkxu',
        db ='top_cjzs',
        charset='utf8',
        )
    cur = conn.cursor()
    #aa=cur.execute(" select * from cjzs_salematch where TradeState=0 and IsDeleted=0 and HouseId in (select Id from cjzs_salehouse where BrokerId=20627 ) and CustomerId in (select Id from cjzs_buycustomer where BrokerId=54112 ) Order by MatchTime Desc")
    aa=string
    data= cur.fetchmany(aa)
    cur.close()
    conn.commit()
    conn.close()
    key_list=[]
    for key in data:
        key_list.append(key)
    HCId=random.sample(key_list, 1)[0]
    HouseId=HCId[1]
    CustomerID=HCId[2]
    return (HouseId,CustomerID)

#获取房,客源ID
def Get_MID(tuple):
    aa=str(tuple)
    H_id1=aa.split(',),)',1)[0]
    H_id=H_id1.split('((',1)[1]
    return H_id

#获取小区名称
def get_HouseVillage():
    conn= MySQLdb.connect(
        host='tops001rc.mysql.rds.aliyuncs.com',
        port = 3648,
        user='commondata_dba',
        passwd='3hM7l3tBygb55QOEA3O4SXdzjy4R0o',
        db ='commondata',
        charset='utf8',
        )
    cur = conn.cursor()
    aa=cur.execute("select name from house_building where type=2 and city_id=112 and villageCode in (select VillageCode from  house_zhuang where VillageCode !=0) ")
    data= cur.fetchmany(aa)
    cur.close()
    conn.commit()
    conn.close()
    key_list=[]
    for key in data:
        key_list.append(key)
    VillageName1=random.sample(key_list, 1)[0]
    HouseVillage=VillageName1[0]
    return HouseVillage.decode("utf-8")
	

def get_LoginResult(string):
	a=string
	if string=='':
		return "FAILE"
	else:
		return "SUCCESS"
		
def get_AddResult(string):
	ret_dict=simplejson.loads(string)
	Code=ret_dict.get('Code')
	if Code==0:
		return "SUCCESS"
	else:
		return "FAILED"
#获取委托单ID
def get_EntrustId(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data')
    Item = dataStr.get("Items")
    EntrustId=Item[0].get('Id')
    return str(EntrustId)

#获取订单Id
def get_OrderIdFromTrade(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data')
    Item = dataStr.get("Items")
    OrderId=Item[0].get('Id')
    return str(EntrustId)

#获取取消合作理由
def get_CancelCooperateReason(string):
    ret_dict = simplejson.loads(string)
    dataStr = ret_dict.get('Data')
    Items=dataStr.get('Items')
    ReasonLs=Items[0].get('ReasonLs')
    ReasonName=ReasonLs[0].get('ReasonName')
    return ReasonName

#获取拒绝成交理由
def get_processRemark():
    processRemark=random.choice(['佣金比例不是约定比例','成交金额不对','成交房源不对','成交客户不对','其他'])
    return processRemark
'''
	VillageName=dataStr.get("VillageName")
	AdminCode=dataStr.get("AdminCode")
	AdminName=dataStr.get("AdminName")
	Address=dataStr.get("Address")
	Lat=dataStr.get("Lat")
	Lng=dataStr.get("Lng")
	id=dataStr.get("id")
	CityName=dataStr.get("CityName")

#解码
def urldecode(string)
	if type(string) is unicode:
        return string.encode('utf-8')

    if not type(data) is dict:
        return data

    utf8_data = {}
    for k, v in data.iteritems():
        utf8_data[k] = unicode(v).encode('utf-8')
    return urlencode(utf8_data
	
'''

	
#def urldecode(string):
#cityName=%E6%9D%AD%E5%B7%9E%E5%B8%82
#d = "cityName==%E6%9D%AD%E5%B7%9E%E5%B8%82"
	
#签名+MD5加密
def Ret(a, b, c):
    if a.get(b, c) != None:
        print(c)
        return c
    else:
        print(c)
        return

def Str_replace(string,str1,str2):
    #print str(string).replace(str1,"").replace(str2,"")
    if str2 == "null":
        return str(string).replace(str1,"")
    else:
        return str(string).replace(str1,"").replace(str2,"")

#Str_replace('http://oauth.test.tops001.com/Login.html?b2befd14199a4fbf986d7946c613ffaf/javascript:void(0)','http://oauth.test.tops001.com/Login.html?','/javascript:void(0)')

def Uk(bd):
    # bd='{"Code":0,"Message":"","Data":"http://oauthpt.test.tops001.com/index.html?uk=c6c5af7d-79e9-4e32-8a48-cc44533811c3&#/zone","ServerTime":"2015-12-29 18:54:58"}'
    s = json.loads(bd)
    return s["Data"].replace("http://oauthpt.test.tops001.com/index.html?uk=", "").replace("&#/zone", "")

def get_string(json1,key1,key2):
    json1 = json.loads(json1)
    if key2 != "null":
        return str(json1[key1][key2])
    else:
        return str(json1[key1])

#get_string('{"Code":0,"Message":"","Data":{"AccessToken":"57405137-b508-11e5-a5a0-6c92bf21d861","ExpirationTime":"2016-01-08 02:31:53","UserToken":"a2b0a5c9-773e-46ee-8534-ad09fb70c891","UserLastUpdated":"2015-07-13 01:11:50","LoginToken":"00000000-0000-0000-0000-000000000000","CrmUserID":"8459","BrokerID":"0","LoginType":1},"ServerTime":"2016-01-07 14:31:53"}',"Data","AccessToken")

def SetCookie(head):
    head = str(head)
    # bd="{'Content-Length': '157', 'Set-Cookie': 'sessionid=e886ebaff9774737b3f4d62223cffb66.49235106; domain=oauthpt.test.tops001.com; path=/; httponly', 'Expires': '-1', 'Server': 'TOPS001.COM', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'Date': 'Tue, 29 Dec 2015 12:52:22 GMT', 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json; charset=utf-8'}"
    print(head.split('sessionid=', 1)[1].split('; domain', 1)[0])


# SetCookie()
def timenow():
    #timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    timeStr = datetime.datetime.now()
    times = str(timeStr)
    #print times
    times = times.replace(" ", "").replace(":", "").replace("-", "").replace(".","")[:-3]
    #print times
    return times
#timenow()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).replace(" ", "").replace(":", "").replace("-", "")


def sign(string, data, time, sig):
    broker = "374fa3ab6b1fae595db5382afe415bce"
    admin = "80b131d757c90282b802e3f9840bfd71"
    test = "11021d8cfed50c14eeb3cca9aeb654f0"
    #print data
    if sig == "app_sales":
        sig = admin
    elif sig == "app_broker":
        sig = broker
    elif sig == "test":
        sig = test

    urlStr = str(string)
    if urlStr.find('?') > 0:
        urlStr = urlStr.split('?')[0]
    strTmp = urlStr.split('/')
    ApiName = urlStr.split('/')[len(strTmp) - 1]
    ApiName = ApiName.lower()
    #print ApiName

    # time = timenow()
    # print time
    paras = data.keys()
    #print ("paras:= {0}".format(paras))
    #dataTmp = "app=" + data.get("app") + "&" + "time=" + time + "&" + "agent=" + data.get("agent")
    dataTmp = "time=" + time
    #print dataTmp
    for i_p in paras:
        #print i_p
        #if i_p != "app" and i_p != "agent":
            #print ("第ddddddddddddddddddddd: {0}".format(data.get(i_p)))
        dataTmp = dataTmp + '&' +i_p.lower() + '=' + changge(data.get(i_p))
            #print dataTmp
   # print ("第一次:= {0}".format(dataTmp))

#   data = _utf8_urlencode(dataTmp)
    #print("data:= {0}".format(dataTmp))
    #dataTmp = urllib.unquote(dataTmp)
   #print("dataTmp:= {0}".format(dataTmp))
    #dataTmp = dataTmp.lower()
    #print("dataTmp:= {0}".format(dataTmp))
    dataTmp = dataTmp.split('&')
    #print("dataTmp:= {0}".format(dataTmp))
    dataList = sorted(dataTmp)
    #print("dataList:= {0}".format(dataList))
    QueryString = ""
    for i in dataList:
        if QueryString == "":
            QueryString = i
        else:
            QueryString = QueryString + '&' + i
    #print QueryString

    # 生成PlainText
    PlainText = ApiName + QueryString + sig
    #print PlainText

    # 生成MD5
    sign = md5.new()
    sign.update(PlainText)
    print "the sign value is "
    print sign.hexdigest()
    return sign.hexdigest()



def _utf8_urlencode(data):
    if type(data) is unicode:
        return data.encode('utf-8')

    if not type(data) is dict:
        return data

    utf8_data = {}
    for k, v in data.iteritems():
        utf8_data[k] = unicode(v).encode('utf-8')
    return urlencode(utf8_data)

def get_MD5_Value(string):
    mString = md5.new()
    mString.update(string)
    #print mString.hexdigest()
    return mString.hexdigest()
#get_MD5_Value("getvillageinfolistagent=ios&ak=ff175d5d-c0b8-11e5-a598-8038bc0b570d&app=app_broker&cityname=%E6%9D%AD%E5%B7%9E%E5%B8%82&time=20160122113454000&villagename=%E6%98%A5%E6%B1%9F%E8%8A%B1%E6%9C%88374fa3ab6b1fae595db5382afe415bce")
                                  # "agent=ios&ak=ff175d5d-c0b8-11e5-a598-8038bc0b570d&app=app_broker&cityName=%E6%9D%AD%E5%B7%9E%E5%B8%82&time=20160122113454000&villageName=%E6%98%A5%E6%B1%9F%E8%8A%B1%E6%9C%88

#print datetime.datetime.now()

def set_Dict_Value(dict, key, value):
    if dict.has_key(key):
        dict[key] = value
    else:
        return None
#a = "{u'agent': u'ios', u'ak': 'ff175d5d-c0b8-11e5-a598-8038bc0b570d', u'app': u'app_broker', u'cityName': u'\u676d\u5dde\u5e02', u'villageName': u''}"
#a = dict()
#sign('http://oauth.apitops.com/Authorization/getvillageinfolist?sign=d5f41c3cfd1b485d745b4244546eb68a', a,"20160122113454000","374fa3ab6b1fae595db5382afe415bce")

def add_Dict_Value(dict, key, value):
    if dict.has_key(key):
        return None
    else:
        dict[key] = value
        return dict

def changge(c):
    c= str(c)
    print quote(c)
    return quote(c)

#changge("啊啊")
#sign = md5.new()
#sign.update('unsafeloginagent=ios&appcode=test&loginname=top&password=123456&time=2016012112204752611021d8cfed50c14eeb3cca9aeb654f0')
#print "the sign value is "
#print sign.hexdigest()


	
	

"""
print changge("a=b&b=c")


#a='F_Title=%E8%92%8B%E5%B8%85%E9%94%8B&app=app_broker&BrokerKid=57034&pushBuildingKids=10&pushType=3&device_id=9cfced20-9458-3cd8-938d-071e48760f38&F_Phone=%2B8617767**8957&F_Sex=%E5%85%88%E7%94%9F&agent=android&ak=d956ff6c-b5a8-11e5-a598-8038bc0b570d&time=20160108154226477&strIsCancel=0&appVersion=3.0.7-debug&F_Remark=&F_Phone2=&F_Phone3=&isRefactor=1&strIsTimer=0'
dataTmp='F_Title=jsf&app=app_broker&BrokerKid=57034&pushBuildingKids=10&pushType=3&device_id=9cfced20-9458-3cd8-938d-071e48760f38&F_Phone=%2B8617767168957&F_Sex=%E5%85%88%E7%94%9F&agent=android&ak=d956ff6c-b5a8-11e5-a598-8038bc0b570d&time=20160108195504572&strIsCancel=0&appVersion=3.0.7-debug&F_Remark=&F_Phone2=&F_Phone3=&isRefactor=1&strIsTimer=0'

#dataTmp = _utf8_urlencode(dataTmp)
#dataTmp = urllib.unquote(dataTmp)
#print("dataTmp:= {0}".format(dataTmp))
dataTmp = dataTmp.lower()
print("dataTmp:= {0}".format(dataTmp))
dataTmp = dataTmp.split('&')
print("dataTmp:= {0}".format(dataTmp))
dataList = sorted(dataTmp)
print("dataList:= {0}".format(dataList))
QueryString = ""
for i in dataList:
    if QueryString == "":
        QueryString = i
    else:
        QueryString = QueryString + '&' + i
print QueryString
#addcustomerandpushv1agent=android&ak=d956ff6c-b5a8-11e5-a598-8038bc0b570d&app=app_broker&appversion=3.0.7-debug&brokerkid=57034&device_id=9cfced20-9458-3cd8-938d-071e48760f38&f_phone=%2b8617767168957&f_phone2=&f_phone3=&f_remark=&f_sex=%e5%85%88%e7%94%9f&f_title=jsf&isrefactor=1&pushbuildingkids=10&pushtype=3&striscancel=0&stristimer=0&time=20160108195504572374fa3ab6b1fae595db5382afe415bce

PlainText = "addcustomerandpushv1" + QueryString + "374fa3ab6b1fae595db5382afe415bce"
print PlainText
sign = md5.new()
sign.update(PlainText)
           # 'addcustomerandpushv1agent=android&ak=d956ff6c-b5a8-11e5-a598-8038bc0b570d&app=app_broker&appversion=3.0.7-debug&brokerkid=57034&device_id=9cfced20-9458-3cd8-938d-071e48760f38&f_phone2=&f_phone3=&f_phone=%2b8617767**8957&f_remark=&f_sex=%e5%85%88%e7%94%9f&f_title=%e8%92%8b%e5%b8%85%e9%94%8b&isrefactor=1&pushbuildingkids=10&pushtype=3&striscancel=0&stristimer=0&time=20160108154226477374fa3ab6b1fae595db5382afe415bce

print "the sign value is "
print sign.hexdigest()
print "ccf8d259af522ec08e1272a88e7505ea"
print urllib.unquote("%2B8617767168957")



print get_MD5_Value("addcustomerandpushv1agent=android&ak=d956ff6c-b5a8-11e5-a598-8038bc0b570d&app=app_broker&appversion=3.0.7-debug&brokerkid=57034&device_id=9cfced20-9458-3cd8-938d-071e48760f38&f_phone=%2b8617767168957&f_phone2=&f_phone3=&f_remark=&f_sex=%e5%85%88%e7%94%9f&f_title=jsf&isrefactor=1&pushbuildingkids=10&pushtype=3&striscancel=0&stristimer=0&time=20160108195504572374fa3ab6b1fae595db5382afe415bce")

"""


