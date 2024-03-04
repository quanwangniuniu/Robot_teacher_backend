from django.urls import path

from chatRobotBackend import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('histchart/', views.hist_generation,name='histChart'),
    path('piechart/', views.pie_generation,name='pieChart'),
    path('boxchart/', views.box_generation,name='boxChart'),
    path('linechart/', views.line_generation,name='lineChart'),
]