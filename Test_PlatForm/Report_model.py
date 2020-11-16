from django.db import models


# Create your models here.


class WebReport(models.Model):
    report_name = models.CharField("报告名称", max_length=200)
    report_suite_id = models.CharField("用例集ID", max_length=200)
    report_path = models.CharField("报告存放路径", max_length=200)
    report_add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    def __str__(self):
        return self.report_name

    class Meta:
        verbose_name = 'Web报告'
        verbose_name_plural = 'Web报告'


class Log(models.Model):
    log_name = models.CharField("日志名称", max_length=200)
    log_path = models.CharField("日志存放路径", max_length=200)
    log_add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    def __str__(self):
        return self.log_name

    class Meta:
        verbose_name = '运行日志'
        verbose_name_plural = '运行日志'


class Image(models.Model):
    image_name = models.CharField("截图名称", max_length=200)
    image_suite_id = models.CharField("截图归属用例集ID", max_length=200)
    image_path = models.CharField("截图存放路径", max_length=200)
    image_add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = '错误截图'
        verbose_name_plural = '错误截图'
