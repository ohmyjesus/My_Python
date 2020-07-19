# 物理引脚下
# 激光 jiguang=7
# 人体红外传感器 GPIO_IN=31;  左vcc=4 ;GND=39
import pymysql
import RPi.GPIO as GPIO
import sys
import time

jiguang = 4
GPIO_IN = 22  # 人体红外传感器输入 GPIO22
# 初始化引脚

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_IN, GPIO.IN)
    GPIO.setwarnings(False)
    GPIO.setup(jiguang, GPIO.OUT, initial=GPIO.LOW)


# 连接数据库
print("开始连接数据库")
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="other")  # 连接数据库
cursor = conn.cursor()
print("数据库连接成功")


def open():
    GPIO.output(jiguang.GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(jiguang.GPIO.LOW)
    time.sleep(0.5)

# 向pi表中插入数据
def order(values):
    global cursor, conn
    value = str(values)
    print(value)
    itime = str(time.strftime('%Y-%m-%d %H:%M:%S'))
    iorder = "insert into pi(closetime,duration) values('" + itime + "','" + value + "');"
    cursor.execute(iorder)
    conn.commit()

try:
    init()
    while True:
        if GPIO.input(22) == True:
            t1 = time.time()
            print("someone is closing...")
            open()
            if GPIO.input(22) == 0:
                t2 = time.time()
                print("nobody")
                t = t2-t1
                order(t)

except Exception as result:
    print("%s" % result)
finally:
    cursor.close()
    conn.close()
