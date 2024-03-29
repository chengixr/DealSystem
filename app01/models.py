import time

from django.db import models
from django_comment_migrate import *


# Create your models here.
class SysUsers(models.Model):
    USERID = models.CharField(help_text='用户代码', max_length=64, primary_key=True, unique=True)
    ORGID = models.CharField(help_text='机构编号', max_length=20)
    USERNAME = models.CharField(help_text='用户名称', max_length=10)
    USERCLASS = models.CharField(help_text='用户类别 01前台 02中台 03后台 04管理员', max_length=4)
    SEX = models.CharField(help_text='用户性别', max_length=1, blank=True, null=True)
    IDCARD = models.CharField(help_text='身份证号', max_length=20)
    PASSWOED = models.CharField(help_text='用户密码', max_length=64)
    EMAIL = models.CharField(help_text='用户邮箱', max_length=50, blank=True, null=True)
    STATUS = models.CharField(help_text='启用状态 1启用 0禁用', max_length=1)
    ADMINFLAG = models.CharField(help_text='管理员标识 Y是 N不是', max_length=1)
    TELNO = models.CharField(help_text='联系方式', max_length=20, blank=True, null=True)
    CREATDATE = models.DateTimeField(help_text='创建时间', blank=True, null=True)
    LSTMNDATE = models.DateTimeField(help_text='更新时间', blank=True, null=True)
    LSTMNUSER = models.CharField(help_text='更新人员', max_length=64, blank=True, null=True)
    EFFECTFLAG = models.CharField(help_text='有效标识', max_length=1)

    class Meta:
        db_table = "SYS_USERS"
        verbose_name = '用户信息表'


class SecInfo(models.Model):
    SEQNO = models.AutoField(help_text="序号", primary_key=True)
    SECID = models.CharField(max_length=20, help_text="债券代码")
    SECNAME = models.CharField(max_length=100, help_text="债券简称")
    PRODUCT = models.CharField(max_length=6, default='SECUR', help_text="债券产品类型代码")
    PRODTYPE = models.CharField(max_length=2, default='FI', help_text="债券交易类型代码")
    ACCTNGTYPE = models.CharField(max_length=10, null=True, blank=True, help_text="债券账户类型代码")
    ISSUESUBJECT1 = models.CharField(max_length=40, help_text="发行债券一级分类")
    ISSUESUBJECT2 = models.CharField(max_length=6, help_text="发行债券二级分类")
    INTCALRULE = models.CharField(max_length=10, help_text="计息方式")
    VDATE = models.DateTimeField(help_text="起息日")
    MDATE = models.DateTimeField(help_text="到期日")
    TERM = models.IntegerField(help_text="债券期限", null=True, blank=True)
    TERMUNIT = models.IntegerField(help_text="债券期限单位", null=True, blank=True)
    ISSUEPRICE = models.DecimalField(max_digits=12, decimal_places=6, default=100, help_text="发行价格")
    DENOM = models.IntegerField(default=100, help_text="债券计息单位")
    CCY = models.CharField(max_length=8, default="CNY", help_text="币种")
    PARVALUE = models.DecimalField(max_digits=26, decimal_places=4, default=100, help_text="债券面额")
    RETURNTYPE = models.CharField(max_length=10, help_text="还本方式")
    SECSUBTYPE = models.CharField(max_length=10, null=True, blank=True, help_text="")
    SETTCCY = models.CharField(max_length=50, default='CCY', null=True, blank=True, help_text="")
    BASIS = models.CharField(max_length=6, help_text="计息基础")
    ADJUSTRULE = models.CharField(max_length=10, help_text="推算方法")
    PAYCYCLE = models.CharField(max_length=3, help_text="付息周期")
    SCHECALRULE = models.CharField(max_length=2, help_text="推算方法")
    FIRSTPAYDATE = models.CharField(max_length=12, null=True, blank=True, help_text="首次付息日")
    INTTYPE = models.CharField(max_length=2, help_text="利率类型")
    PAPERIP = models.DecimalField(max_digits=12, decimal_places=6, help_text="票面利率")
    RATECODE = models.CharField(max_length=20, null=True, blank=True, help_text="基准利率")
    FACTOR = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True, help_text="因子 固定利率")
    SPREADRATE = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True, help_text="利差 固定利率")
    TOPRATEFLAG = models.CharField(max_length=1, null=True, blank=True, help_text="是否有上限利率 Y是 N否")
    TOPRATE = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True, help_text="上限利率")
    BOTTOMRATEFLAG = models.CharField(max_length=1, null=True, blank=True, help_text="是否有下限利率 Y是 N否")
    BOTTOMRATE = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True, help_text="下限利率")
    RATEVALUETYPE = models.CharField(max_length=1, null=True, blank=True)
    RATEVALUEPERIOD = models.CharField(max_length=1, null=True, blank=True)
    RATEVALUEDAYS = models.IntegerField(null=True, blank=True)
    PAYRULE = models.CharField(max_length=10, null=True, blank=True, help_text="营业日准则")
    INTPAYRULE = models.CharField(max_length=10, null=True, blank=True, help_text="利息分配方式")
    PLANISSUEAMT = models.DecimalField(max_digits=26, decimal_places=4, default=0, help_text="计划发行总额")
    ISSUEAMT = models.DecimalField(max_digits=26, decimal_places=4, help_text="发行总额")
    EXERCISEFLAG = models.CharField(max_length=1, default='N', help_text="是否含权")
    VIRTUALFLAG = models.CharField(max_length=1, null=True, blank=True, help_text="是否虚拟债 1是 0否")
    CONVERTFLAG = models.CharField(max_length=1, null=True, blank=True, help_text="是否可转债 Y是 N否")
    PRINBACKFLAG = models.CharField(max_length=1, null=True, blank=True, help_text="是否中间还本 Y是 N否")
    CREATEDATE = models.DateTimeField(null=True, blank=True, help_text="创建时间")
    EFFECTFLAG = models.CharField(max_length=1, help_text="有效标识")
    LSTMNTDATE = models.DateTimeField(help_text="更新时间")
    LSTMNTUSER = models.CharField(max_length=64, help_text="更新用户")
    FULLNAME = models.CharField(max_length=150, help_text="债券全称")
    SRCSECID = models.CharField(max_length=20, null=True, blank=True, help_text="原债券代码")
    RETURNSUBTYPE = models.CharField(max_length=10, null=True, blank=True, help_text="还本类型 SUBP减持仓 SUBV减面值")
    RTRANUSER = models.CharField(max_length=64, null=True, blank=True, help_text="业务柜员号")
    RTRANNAME = models.CharField(max_length=20, null=True, blank=True, help_text="业务员姓名")
    ORGID = models.CharField(max_length=20, null=True, blank=True, help_text="机构号")
    ORGNAME = models.CharField(max_length=100, null=True, blank=True, help_text="机构名称")
    SECMARKETID = models.CharField(max_length=40, help_text="债券市场代码")

    class Meta:
        db_table = 'TGT_SECINFO'
        verbose_name = "债券信息表"


class SecSchedule(models.Model):
    SCHNO = models.AutoField(primary_key=True, help_text='付息流水号')
    SEQNO = models.IntegerField(help_text='债券流水号')
    SECID = models.CharField(max_length=20, help_text='债券代码')
    IPAYDATE = models.DateField(help_text='付息日')
    STATDATE = models.DateField(help_text='计息开始日')
    ENDDATE = models.DateField(help_text='计息结束日')
    RATECODE = models.CharField(max_length=20, null=True, blank=True, help_text='利率代码')
    INTRATE = models.DecimalField(max_digits=30, decimal_places=12, default=0, null=True, help_text='计息利率')
    INTRATEACT = models.DecimalField(max_digits=30, decimal_places=12, default=0, null=True, help_text='计息实际利率')
    SPREADRATE = models.DecimalField(max_digits=30, decimal_places=12, default=0, null=True, help_text='利差')
    BASIS = models.CharField(max_length=6, null=True, help_text='计息基础')
    RATEFIXDATE = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), help_text='利率确定日')
    PRINAMT = models.DecimalField(max_digits=30, decimal_places=12, default=0, help_text='本金总量')
    INTPAYAMT = models.DecimalField(max_digits=30, decimal_places=12, default=0, null=True, help_text='应付利息额')
    INTPAYAMTACT = models.DecimalField(max_digits=30, decimal_places=12, default=0, help_text='实付利息额')
    PRINPAYAMT = models.DecimalField(max_digits=30, decimal_places=12, default=0, help_text='本金支付量')
    CASHFLOW = models.DecimalField(max_digits=30, decimal_places=12, default=0, help_text='现金流总量')
    PAYFLAG = models.CharField(max_length=1, default='P', help_text='付息标识 P计算 A实际付息')
    CREATEDATE = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), help_text='创建时间')
    EFFECTFLAG = models.CharField(max_length=1, help_text='有效标识 E有效 D无效 A新建')
    LSTMNDATE = models.DateTimeField(null=True, help_text='更新时间')
    LSTMNUSER = models.CharField(max_length=64, null=True, help_text='更新用户')
    SECMARKETID = models.CharField(max_length=40, help_text='市场代码')

    class Meta:
        db_table = 'TGT_SECSCHEDULE'
        verbose_name = '债券还本付息计划表'
