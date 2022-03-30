from django.db import models


# Create your models here.
class SysUsers(models.Model):
    USERID = models.CharField(verbose_name='用户代码', max_length=64, primary_key=True, unique=True)
    ORGID = models.CharField(verbose_name='机构编号', max_length=20)
    USERNAME = models.CharField(verbose_name='用户名称', max_length=10)
    USERCLASS = models.CharField(verbose_name='用户类别 01前台 02中台 03后台 04管理员', max_length=4)
    SEX = models.CharField(verbose_name='用户性别', max_length=1, blank=True, null=True)
    IDCARD = models.CharField(verbose_name='身份证号', max_length=20)
    PASSWOED = models.CharField(verbose_name='用户密码', max_length=64)
    EMAIL = models.CharField(verbose_name='用户邮箱', max_length=50, blank=True, null=True)
    STATUS = models.CharField(verbose_name='启用状态 1启用 0禁用', max_length=1)
    ADMINFLAG = models.CharField(verbose_name='管理员标识 Y是 N不是', max_length=1)
    TELNO = models.CharField(verbose_name='联系方式', max_length=20, blank=True, null=True)
    CREATDATE = models.DateTimeField(verbose_name='创建时间', blank=True, null=True)
    LSTMNDATE = models.DateTimeField(verbose_name='更新时间', blank=True, null=True)
    LSTMNUSER = models.CharField(verbose_name='更新人员', max_length=64, blank=True, null=True)
    EFFECTFLAG = models.CharField(verbose_name='有效标识', max_length=1)

    class Meta:
        db_table = "SYS_USERS"
        verbose_name = '用户信息表'
