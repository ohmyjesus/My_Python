#DS18B20的GPIOPIN为4（BCM编码）   物理引脚为7
import pymysql
import time
import re

# 连接数据库
way='/sys/bus/w1/devices/28-01193893fef4/w1_slave'
print("system start , start connect mysql")
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="other") #连接数据库
cursor=conn.cursor()
print("connect mysql succeed")

#向pi表中插入数据 
def order(values):
    global cursor,conn
    value=str(values)
    print(value)
    itime=str(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(itime)
    iorder="insert into pi(time,temperature) values('"+itime+"','"+value+"');"
    cursor.execute(iorder)
    conn.commit()
try:  #看能不能打开文件
    file=open(way,'r')
except Exception as result:
    print("%s" % result)
    order('-404')
    conn.close()
    try:
        file.close()
    except Exception as result:
        pass
    exit()
    
try: #将温度值写入表中的temperature
    temperature=file.read()
    crc=re.compile('crc=.*?(.*?)\n').findall(temperature)[0]
    t=re.compile('t=(.*?)\n').findall(temperature)[0]
    t=str(float(t)/1000.0)
    order(t)
except Exception as result: #不能写入则temperature值为-510
    print("%s" % result)
    order('-510')
finally:
    file.close()
    conn.close()
    