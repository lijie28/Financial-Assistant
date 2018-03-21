import time,os
from datetime import datetime, timezone

#余利宝
ylb = 10000.0
#余额宝
yeb = 10000.0
#零钱通
lqt = 1000.0 
#花呗
# hb = 7000.0
hb_used = 1000.0
#京东白条
jdbt_used = 8000.0

total = [{
    'name':'nil',#具体种类
    'type':0,#1是日结、可日取，2是定期，3是欠的（花呗，白条）
    'amount':0.0, #具体金额
    'rate':0 ,#年化 
    'date':'datestring' #到期日
},]



filepath = 'date.info'

nowtimestamp = time.time()


def fileos (filepath,old_str=''):
    if os.path.exists(filepath):#存在的话只改写
            f = open(filepath, "r") 
            lines = f.readlines() #读取所有行
    else:
        file_object = open(filepath, 'w')
        file_object.writelines(old_str)
        file_object.close()


def gettime(timestamp,type = 1):
    format = "%Y-%m-%d %H:%M:%S"
    if type ==2 :
        format = "%Y-%m-%d"
    structtime = time.localtime(timestamp)
    return time.strftime(format, structtime) 


def gettimestamp(strtime,type=1):

    format = "%Y-%m-%d %H:%M:%S"
    if type ==2 :
        format = "%Y-%m-%d"
    #转换成时间数组
    timeArray = time.strptime(strtime, format)
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp 


