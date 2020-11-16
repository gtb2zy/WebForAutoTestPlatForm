# from Test_Platform.models import Config, PlatForm,WebReport
from django.contrib import admin
from django.utils.safestring import mark_safe

import xadmin

from Test_Platform.models import Config, SuiteManage, CaseManage, ActionManage
from xadmin import views
from Test_Platform import models
from Report_Platform.report_views import LogView, ImageView, WebReportView
from Test_Platform.test_views import MobileTestView
from Report_Platform.models import WebReport, Log, Image


class ConfigAdmin():
    list_display = ['conf_name', 'conf_key', 'conf_value']
    list_per_page = 20
    list_display_links = ('conf_key',)

    def dename(self, obj):
        if obj.deid:
            bbb = models.Config.objects.all().values_list('conf_name', 'conf_key', 'conf_value').get(
                id=obj.conf_id)[1]
        else:
            bbb = None
        return bbb

    #
    search_fields = ['conf_key']


class CaseManageAdmin():
    list_display = ["id", "case_name", "action_name", "case_file"]
    list_per_page = 20
    list_display_links = ("case_name")
    filter_horizontal = ('action_name',)
    style_fields = {"action_name": "m2m_transfer"}


class ActionManageAdmin():
    list_display = ["id", "action_name", "action_param", "action_file"]
    list_per_page = 20
    list_display_links = ("action_name")


class SuiteManageAdmin(object):
    list_display = ["suite_name", "remote_ip", "remote_port", "platform", "case_name", "suite_param", "suite_add_time",
                    "操作"]
    list_per_page = 20
    list_display_links = ("suite_name")

    def 操作(self, obj):
        exebutton = '<p class="default btn btn-primary hide-xs"  onclick="exe_click_action_info(\'%s\')">执行</p>' % (
            str(obj.id))
        delbutton = '<p class="default btn btn-primary hide-xs"  onclick="del_click_action_info(\'%s\')">删除</p>' % (
            str(obj.id))
        r = mark_safe(exebutton + delbutton)
        return r

    def get_media(self):
        media = super(SuiteManageAdmin, self).get_media() + self.vendor('xadmin.page.list.js', 'xadmin.page.form.js')
        media += self.vendor('xadmin.list.xxxx.js', 'xadmin.jquery.cookie.min.js', 'xadmin.form.css')
        return media


class WebReportAdmin(object):
    list_display = ["report_name", "report_suite_id", "report_path", "report_add_time", "操作"]
    list_per_page = 20
    list_display_links = ("report_name")

    def 操作(self, obj):
        button = '<p class="default btn btn-primary hide-xs"  onclick="webclick_action_info(\'%s\')">查看</p>' % (
            str(obj.id))
        r = mark_safe(button)
        return r

    def get_media(self):
        media = super(WebReportAdmin, self).get_media() + self.vendor('xadmin.page.list.js', 'xadmin.page.form.js')
        media += self.vendor('xadmin.list.xxxx.js', 'xadmin.jquery.cookie.min.js', 'xadmin.form.css')
        return media


class LogAdmin(object):
    list_display = ["log_name", "log_path", "log_add_time", "操作"]
    list_per_page = 20
    list_display_links = ("log_name")

    def 操作(self, obj):
        button = '<p class="default btn btn-primary hide-xs"  onclick="logclick_action_info(\'%s\')">查看</p>' % (
            str(obj.log_path))
        r = mark_safe(button)
        return r

    def get_media(self):
        media = super(LogAdmin, self).get_media() + self.vendor('xadmin.page.list.js', 'xadmin.page.form.js')
        media += self.vendor('xadmin.list.xxxx.js', 'xadmin.jquery.cookie.min.js', 'xadmin.form.css')
        return media


class ImageAdmin(object):
    list_display = ["image_name", "image_suite_id", "image_path", "image_add_time", "操作"]
    list_per_page = 20
    list_display_links = ("image_name")

    def 操作(self, obj):
        button = '<p class="default btn btn-primary hide-xs"  onclick="imageclick_action_info(\'%s\')">查看</p>' % (
            str(obj.image_path))
        r = mark_safe(button)
        return r

    def get_media(self):
        media = super(ImageAdmin, self).get_media() + self.vendor('xadmin.page.list.js', 'xadmin.page.form.js')
        media += self.vendor('xadmin.list.xxxx.js', 'xadmin.jquery.cookie.min.js', 'xadmin.form.css')
        return media


class GlobalSetting(object):
    site_title = "自动化测试平台"
    site_footer = "陈治许"

    # menu_style = "accordion"  # 菜单折叠

    def get_site_menu(self):
        return [
            {
                'title': '测试平台管理',
                'icon': 'fa fa-bars',
                'menus': (
                    {
                        'title': '移动端UI测试',

                        'url': "/xadmin/mobile_test_view"
                        # 自定义跳转列表
                    },
                )
            }

        ]


class LoginSetting(object):
    title = "自动化测试平台"


xadmin.site.register_view(r'web_report_view', WebReportView, name='web_report')
xadmin.site.register_view(r'log_view', LogView, name='log')
xadmin.site.register_view(r'image_view', ImageView, name='image')
xadmin.site.register_view(r'mobile_test_view/$', MobileTestView, name='mobile_test')

xadmin.site.register(views.LoginView, LoginSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(Config, ConfigAdmin)
xadmin.site.register(SuiteManage, SuiteManageAdmin)
xadmin.site.register(CaseManage, CaseManageAdmin)
xadmin.site.register(ActionManage, ActionManageAdmin)
xadmin.site.register(WebReport, WebReportAdmin)
xadmin.site.register(Log, LogAdmin)
xadmin.site.register(Image, ImageAdmin)
