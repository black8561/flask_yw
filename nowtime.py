import datetime
import time


def nowtime():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return nowtime


def weekcycletime():
    nowtime = int(datetime.datetime.now().strftime('%Y%m%d'))
    today = int(time.strftime("%w"))
    weekminday = str(nowtime - today + 1)
    weekmaxday = str(int(weekminday) + 6)
    return weekmaxday,weekminday
    #[0]为该星期最大天数，[1]为该星期最小天数

def monthcycletime():
    nowtime = datetime.datetime.now().strftime('%Y%m')
    monthminday=nowtime+'01'
    monthmaxday = nowtime + '31'
    return monthmaxday,monthminday


def nowday():
    nowday = datetime.datetime.now().strftime('%Y%m%d')
    return nowday

def nowdaystr():
    nowday = datetime.datetime.now().strftime('%Y%m%d')
    nowdaystr=nowday[:4]+'年'+nowday[4:6]+'月'+nowday[6:8]+'日'
    return nowdaystr

print(monthcycletime())


