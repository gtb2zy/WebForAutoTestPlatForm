from bs4 import BeautifulSoup
from django.shortcuts import render

from django.shortcuts import render
import os

from xadmin.views import CommAdminView


class WebReportView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "Web报告"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        current_path = os.path.realpath(os.path.dirname(__file__))
        web_datedir_report_path = current_path + "/../templates/report/html/"
        path = request.get_full_path()
        file_path = web_datedir_report_path + path.replace("/xadmin/web_report_view/", "")
        html = read_file_as_str(file_path)
        context.setdefault("path", path)
        context.setdefault("html", html)
        return render(request, 'web_report.html', context)  # 最后指定自定义的template模板，并返回contex


class LogView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "LOG日志"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        current_path = os.path.realpath(os.path.dirname(__file__))
        log_datedir_report_path = current_path + "/../templates/report/log/"
        path = request.get_full_path()
        file_path = log_datedir_report_path + path.replace("/xadmin/log_view/", "")

        log = read_file_as_str(file_path)

        context.setdefault("log", log)

        return render(request, 'log_dir.html', context)  # 最后指定自定义的template模板，并返回contex


class ImageView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "错误截图"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        current_path = os.path.realpath(os.path.dirname(__file__))
        image_datedir_report_path = current_path + "/../templates/report/image/"

        image_report_list = []
        dir_list = os.listdir(image_datedir_report_path)
        dir_list.reverse()
        for dirname in dir_list:
            image_report_dir_list = {}
            image_report_file_list = []
            for filename in os.listdir(image_datedir_report_path + "/" + dirname):
                image_report_file_list.append(filename)
            image_report_dir_list.setdefault(dirname, image_report_file_list)
            image_report_list.append(image_report_dir_list)
        context.setdefault("image_report_list", image_report_list)

        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        # .........

        return render(request, 'image_dir.html', context)  # 最后指定自定义的template模板，并返回contex


def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path, encoding="utf-8").read()
    # print type(all_the_text)
    return all_the_text
