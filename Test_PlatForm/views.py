import configparser
import os

from django.http import HttpResponse
from django.shortcuts import render
from xadmin.views import CommAdminView
from WebforAutoTestPlatform.test_suite.mobile.suite import suite_test
from WebforAutoTestPlatform.global_variable import *
from Test_Platform import models


class MobileTestView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "移动端UI测试"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面

        plugins = self.getobject(MOBILE_ACTION_PLUGIN_PATH)
        cases_name = self.getobject(MOBILE_CASE_PLUGIN_PATH)

        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        # .........
        suite_l = []
        suite_list = models.SuiteManage.objects.all()

        for suite in suite_list:
            suite_o = {}
            suite_o.setdefault("suite_id", suite.id)
            suite_o.setdefault("remote_ip", suite.remote_ip)
            suite_o.setdefault("remote_port", suite.remote_port)
            suite_o.setdefault("platform", suite.platform)
            suite_o.setdefault("suite_name", suite.suite_name)
            suite_o.setdefault("case_name_list", suite.case_name)
            suite_o.setdefault("suite_param", suite.suite_param)
            suite_o.setdefault("suite_add_time", str(suite.suite_add_time))
            suite_l.append(suite_o)
        remote_ip = models.Config.objects.get(conf_key="remote_ip")
        platform = models.Config.objects.get(conf_key="platform")
        remote_ip_list = str(models.Config.objects.get(conf_key="remote_ip_list"))
        remote_ip_list = remote_ip_list.split(",")
        context.setdefault("suite_list", suite_l)
        context.setdefault("remote_ip_list", remote_ip_list)
        context.setdefault("plugins", plugins)
        context.setdefault("cases_name", cases_name)
        context.setdefault("remote_ip", remote_ip)
        context.setdefault("platform", platform)
        return render(request, 'mobile_test.html', context)  # 最后指定自定义的template模板，并返回contex

    def getobject(self, path):
        objects = []
        dir_list = os.listdir(path)
        if not dir_list:
            return
        else:
            # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(path, x)))
        for object_name in dir_list:
            if not object_name.endswith(".py") or object_name.startswith("_"):
                continue
            objects.append(object_name.replace(".py", ''))
        return objects


def suite_exe(request):
    try:
        action = request.POST["action"]
        if "add" in action:

            suite_name = request.POST["suite_name"]
            suite_param = request.POST["suite_param"].strip()
            test_case = request.POST["test_case"]
            remote_ip = request.POST["remote_ip"]
            platform = request.POST["platform"]
            if len(test_case) == 0:
                return HttpResponse("请选择用例")
            models.SuiteManage.objects.create(platform=platform, remote_ip=remote_ip, suite_name=suite_name,
                                              case_name=test_case, suite_param=suite_param)
            result = "添加成功"

        if "exe" in action:
            suite_id = request.POST["suite_id"]
            suite_param = models.SuiteManage.objects.get(id=suite_id).suite_param
            test_case = models.SuiteManage.objects.get(id=suite_id).case_name
            remote_ip = models.SuiteManage.objects.get(id=suite_id).remote_ip
            platform = models.SuiteManage.objects.get(id=suite_id).platform
            models.Config.objects.filter(conf_key="platform").update(conf_value=platform)
            models.Config.objects.filter(conf_key="remote_ip").update(conf_value=remote_ip)
            test_case = test_case.split(",")
            suite_test(test_case,suite_id,suite_param)
            result = "执行成功"
        if "del" in action:
            suite_id = request.POST["suite_id"]
            models.SuiteManage.objects.get(id=suite_id).delete()
            result = "删除成功"


    except Exception as e:
        result = "操作失败"
        print(e)

    return HttpResponse(result)
# send mail etc.
