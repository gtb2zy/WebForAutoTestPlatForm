#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/4/10 9:57
# software: PyCharm
import os
'''
DDPT：
D:develop（开发）
D：DevOps(运维)
P:product(产品)
T：Test(测试)
1、创建Django
2、到https://github.com/zhixuchen/xadmin/tree/django2 下载xadmin-master.zip
解压xadmin-master.zip,将解压后文件夹内xadmin拷贝到项目根目录下
3、在settings.py中的INSTALLED_APPS下增加：
    'xadmin',
    'crispy_forms',
    'reversion',
    
安装 pip install django-import-export
4、在urls.py中增加
import xadmin
在urlpatterns 中增加：
path('xadmin/', xadmin.site.urls),


5、python manage.py migrate  #初始化表单
python manage.py createsuperuser    #创建超级用户

6、修改默认为中文：
在settings.py中修改以下
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

7、extra_apps目录找到xadmin/views/dashboard.py，在36行的位置
    def render(self, name, value, attrs=None):
    修改为def render(self, name, value, attrs=None,renderer=None):
8、xadmin使用的导航图标采用font-awesome图标，你可以到

http://fontawesome.dashgame.com

下载最新的图标文件，并解压出css和font目录
'''
if __name__ == '__main__':
    try:
        # print(os.system('%s' % ("py manage.py makemigrations")))
        # print(os.system('%s' % ("py manage.py migrate")))
        # print(os.system('%s'%('py manage.py createsuperuser')))
        # print(os.system('%s' % ("pip freeze > requirements.txt")))#部署需要生成requirements.txt文件（宝塔部署需要修改生成文件内的Django 改为django）


        print(os.system('%s' % ("python manage.py runserver 127.0.0.1:8080")))
        # print(os.system('%s' % ("py manage.py startapp Report_Platform")))#创建新的APP注意修改url，settingT
    except Exception as e:
        print(e)
