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


# 计算资金支付日
def calc_pay_date(mdate, payrule, holidays):
    if payrule == 'unchanged':
        return mdate

    change_rule = {'next': 1, 'last': -1, 'unchanged': 0, 'adjust': 'adjust'}
    ipayday = mdate
    while ipayday in holidays:
        if payrule == 'adjust' and ipayday == get_month_days(int(mdate[5:7]), int(mdate[:4])):
            ipayday = mdate
            while ipayday in holidays:
                ipayday = change_day(ipayday, -1)
        ipayday = change_day(ipayday, change_rule[payrule])
    return ipayday


# 根据日期向前或向后推算月份
def calc_date(date, key=1, value=1):
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
    if value == 12:
        year += key
    else:
        month += key
    if day > get_month_days(month, year):
        day = get_month_days(month, year)
    return str(year) + '-' + str(month) + '-' + str(day)


# 计算起息日和到期日的付息计划
def calc_schedule(vdate, mdate, paycycle, payrule, schecalrule, holidays, firstpaydate=None):
    if re.match(r'\d{4}-\d{1,2}-\d{1,2}', vdate) is None or re.match(r'\d{4}-\d{1,2}-\d{1,2}', mdate) is None:
        return False
    days = calc_days(vdate, mdate)
    if days <= 0:
        return False

    # 如果起息日和到期日相差小于一个月或者付息周期为利随本清，直接放到表中
    if days <= get_month_days(int(vdate[5:7]), int(vdate[:4])) or paycycle == 'DSD':
        return schedule_list.append([vdate, mdate, calc_pay_date(mdate, payrule, holidays), days])

    paycycle_days = {'M': 1, 'Q': 3, 'S': 6, 'Y': 12}
    if schecalrule == 'VF':
        mdate_current = calc_date(vdate, 1, paycycle_days[paycycle])
        days = calc_days(vdate, mdate_current)
        schedule_list.append([vdate, mdate_current, calc_pay_date(mdate_current, payrule, holidays), days])
        calc_schedule(mdate_current, mdate, paycycle, payrule, schecalrule, holidays)
    elif schecalrule == 'MB':
        vdate_current = calc_date(mdate, -1, paycycle_days[paycycle])
        days = calc_days(vdate_current, mdate)
        schedule_list.append([vdate_current, mdate, calc_pay_date(mdate, payrule, holidays), days])
        schedule_list.append([vdate, mdate, calc_pay_date(mdate, payrule, holidays), days])
        calc_schedule(vdate, vdate_current, paycycle, payrule, schecalrule, holidays)
    elif firstpaydate is not None:
        days = calc_days(vdate, firstpaydate)
        schedule_list.append([vdate, firstpaydate, calc_pay_date(firstpaydate, payrule, holidays), days])
        calc_schedule(firstpaydate, mdate, paycycle, payrule, schecalrule, holidays)




