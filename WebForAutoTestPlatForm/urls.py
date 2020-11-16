"""WebforAutoTestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Report_Platform import report_views
import xadmin
from Test_Platform import test_views


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('xadmin/mobile_test_view/suite_test/', test_views.suite_exe, name='suite_exe'),
    # path('xadmin/web_report_view/web_report/', report_views.WebReportView, name='web_report'),
]
