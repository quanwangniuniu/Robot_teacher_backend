from django.urls import path
from . import views

urlpatterns = [
    path('pdf2docx', views.pdf2docx,name='pdf2docx'),
    path('docx2pdf', views.docx2pdf,name='docx2pdf'),
    path('pdf2excel', views.pdf2excel,name='pdf2excel'),
    path('excel2pdf', views.excel2pdf,name='excel2pdf'),
    # 添加其他URL配置
]