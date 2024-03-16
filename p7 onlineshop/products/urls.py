from django.urls import path
from . import  views
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

    path('', views.IndexView.as_view() , name='index'),
    path('detail/<int:pk>', views.product_detail , name='product_detail'),
    path('change_lang/', views.switch_lang, name='switch_lang'),
    path('msg/', views.msg, name='msg'),

]
# urlpatterns += i18n_patterns()