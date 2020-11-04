# from Test_Platform.models import Config, PlatForm,WebReport
import xadmin
from xadmin import views
# from Test_Platform import models


# class ConfigAdmin():
#     list_display = ['config_id', 'config_name', 'config_type', 'suite_id']
#     list_per_page = 20
#     list_display_links = ('config_id',)
#
#     def dename(self, obj):
#         if obj.deid:
#             bbb = models.Config.objects.all().values_list('config_id', 'config_name', 'config_type', 'suite_id').get(
#                 id=obj.config_id)[1]
#         else:
#             bbb = None
#         return bbb
#
#     #
#     search_fields = ['config_id']
#
#
# class PlatFormAdmin():
#     list_display = ['platform_id', 'platform_name']
#     list_per_page = 20
#     list_display_links = ('platform_id',)
#     search_fields = ['platform_id', 'platform_name']
#
#
# class WebReportAdmin():
#     list_display=[]
#     object_list_template = "http://www.baidu.com"

class GlobalSetting(object):
    site_title = "自动化测试平台"
    site_footer = "陈治许"
    menu_style = "accordion"  # 菜单折叠

    def get_site_menu(self):
        return [
            {
                'title': '测试平台管理',
                'icon': 'fa fa-bars',
                'menus': (
                    {
                        'title': '移动端UI测试',

                        'url': ""
                        # 自定义跳转列表
                    },
                    {
                        'title': 'WEB端UI测试',

                        'url': ""
                        # 自定义跳转列表
                    },
                    {
                        'title': 'API接口测试',

                        'url': ""
                        # 自定义跳转列表
                    },
                    {
                        'title': 'PC(WIN)UI测试',

                        'url': ""
                        # 自定义跳转列表
                    },

                )
            },
            {
                'title': '配置管理中心',
                'icon': 'fa fa-cog',  # Font Awesome图标
                'menus': (
                    {
                        'title': '全局配置',
                        'icon': 'fa fa-cog',
                        'url': ""
                    },
                    {
                        'title': '局部配置',
                        'icon': 'fa fa-cog',
                        'url': "",
                    }
                )
            },
            {"title": "报告管理平台",
             "icon": "fa fa-bars",
             "menus": ({
                           "title": "WEB报告",
                           "url": "/xadmin/test_view"
                       }, {
                           "title": "运行日志",
                           "url": ""
                       },
                       {
                           "title": "错误截图",
                           "url": ""
                       }
             )
             }

        ]


class LoginSetting(object):
    title = "自动化测试平台"


from .views import TestView

xadmin.site.register_view(r'test_view/$', TestView, name='for_test')
xadmin.site.register(views.LoginView, LoginSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
#
# xadmin.site.register(Config, ConfigAdmin)
# xadmin.site.register(PlatForm, PlatFormAdmin)