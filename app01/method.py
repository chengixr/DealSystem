import re

schedule_list = []
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 判断是否为闰年
def determin_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return 1
    else:
        return 0


# 判断每月多少天
def get_month_days(month, year):
    if month == 2 and determin_leap_year(year) == 1:
        return 29
    else:
        return month_days[month]


# 日期加或减n天
def change_day(date, days=1):
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
    day += days
    while day > get_month_days(month, year):
        day -= get_month_days(month, year)
        month += 1
        if month > 12:
            year += 1
            month = 1
    while day < 1:
        month -= 1
        if month < 1:
            year -= 1
            month = 12
        day += get_month_days(month, year)
    return str(year) + '-' + str(month) + '-' + str(day)


# 计算两个日期相差多少天
def calc_days(vdate, mdate):
    days = 0
    vyear, myear = int(vdate[:4]), int(mdate[:4])
    vmonth, mmonth = int(vdate[5:7]), int(mdate[5:7])
    vday, mday = int(vdate[8:]), int(mdate[8:])
    # 计算月份累计天数
    vmonth -= 1
    while vmonth > 0:
        days -= get_month_days(vmonth, vyear)
        vmonth -= 1
    days -= vday
    mmonth -= 1
    while mmonth > 0:
        days += get_month_days(mmonth, myear)
        mmonth -= 1
    days += mday
    # 计算起始年份到终止年份天数（不包括终止年份）
    while vyear < myear:
        days += 366 if determin_leap_year(vyear) == 1 else 365
        vyear += 1
    return days


def calc_schedule(vdate, mdate, paycycle, payrule, schecalrule, holidays):
    if re.match(r'\d{4}-\d{1,2}-\d{1,2}', vdate) is None or re.match(r'\d{4}-\d{1,2}-\d{1,2}', mdate) is None:
        return False
    days = calc_days(vdate, mdate)
    if days <= 0:
        return False
    if days <= 30:
        ipayday = mdate
        while ipayday in holidays:
            ipayday = change_day(ipayday)
        return schedule_list.append([vdate, mdate, ipayday, days])



