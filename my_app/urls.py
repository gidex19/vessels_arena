from django.urls import path
from . import views as my_app_view

urlpatterns = [
    path('', my_app_view.home, name='homepage'),
    path('branches/', my_app_view.branches, name='branches'),
    path('about/', my_app_view.about, name='about'),
    path('devotional/', my_app_view.devotional, name='devotional'),
    path('devotional/<int:pk>/', my_app_view.devotional_detail, name='devotional_detail'),
    path('history/', my_app_view.history, name='history'),
    # path('addform/', my_app_view.addformpage, name='add_form'),
    path('vision/', my_app_view.vision, name='vision'),
    path('message/', my_app_view.message, name='message'),
    path('men-of-valour/', my_app_view.men_of_valour, name='men_of_valour'),
    path('sfw/', my_app_view.sfw, name='sfw'),
    path('tender-vessels/', my_app_view.tender_vessels, name='tender-vessels'),
    # path('download/', my_app_view.download, name='download'),
]
