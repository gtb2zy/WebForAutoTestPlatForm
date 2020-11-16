from django import forms
from django.db import models
from WebforAutoTestPlatform.global_variable import *


class Config(models.Model):
    conf_name = models.CharField("配置标题", max_length=20)
    conf_key = models.CharField("配置的KEY", max_length=20)
    conf_value = models.CharField("配置的VALUE", max_length=500)

    class Meta:
        verbose_name = '配置管理'
        verbose_name_plural = '配置管理'

    def __str__(self):
        return self.conf_value


class ActionManage(models.Model):
    action_name = models.CharField("动作名称", max_length=200)
    action_param = models.CharField("动作的传参", max_length=200)
    action_file = models.FileField("动作文件", upload_to=MOBILE_ACTION_PLUGIN_PATH, blank=True)
    action_add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '动作管理'
        verbose_name_plural = '动作管理'

    def __str__(self):
        return self.action_name


class CaseManage(models.Model):
    case_name = models.CharField("用例名称", max_length=200)
    action_name = models.ManyToManyField(ActionManage)
    case_file = models.FileField("用例文件", upload_to=MOBILE_CASE_PLUGIN_PATH, blank=True)
    case_add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '用例管理'
        verbose_name_plural = '用例管理'

    def __str__(self):
        return self.case_name


class SuiteManage(models.Model):
    remote_ip = models.CharField("远端地址", max_length=200, default="127.0.0.1")
    remote_port = models.CharField("远端端口", max_length=200, default=4723)
    platform = models.CharField("平台", max_length=200, default="Android")
    suite_name = models.CharField("用例集名称", max_length=200)
    case_name = models.CharField("用例名", max_length=200, default="")
    suite_param = models.CharField("用例集的传参", max_length=200)
    suite_add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '用例集管理'

        verbose_name_plural = '用例集管理'

    def __str__(self):
        return self.suite_name
