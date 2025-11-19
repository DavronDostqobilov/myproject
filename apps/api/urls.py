from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('report/', views.report_view, name='report'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path("media_list/", views.media_list, name="media_list"),
    path('policy/', views.policy, name='policy'),
    # Project URLs
    path('quality/', views.quality, name='quality'),
    path('gender/', views.gender, name='gender'),
    path('economic/', views.economic, name='economic'),
    path('pleace/', views.peace, name='peace'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('industry/', views.industry, name='industry'),
    # We have urls
    path('statistics/', views.statistics_view, name='statistics'),
    path('student-engagement/', views.student_engagement_view, name='student_engagement'),
    path('womens-empowerment/', views.student_womens_empowerment, name='womens_empowerment'),
    path('sustainable-economy/', views.sustainable_economy, name='sustainable_economy'),

    #Quality Education URLs
    path('quality/1/', views.quality1, name='quality1'),
    path('quality/2/', views.quality2, name='quality2'),
    path('quality/3/', views.quality3, name='quality3'),
    path('quality/4/', views.quality4, name='quality4'),
    path('quality/5/', views.quality5, name='quality5'),
    path('quality/6/', views.quality6, name='quality6'),
    path('quality/7/', views.quality7, name='quality7'),
    path('quality/8/', views.quality8, name='quality8'),
    path('quality/9/', views.quality9, name='quality9'),
    path('quality/10/', views.quality10, name='quality10'),
    path('quality/11/', views.quality11, name='quality11'),
    path('quality/12/', views.quality12, name='quality12'),
    path('quality/13/', views.quality13, name='quality13'),

    #Gender Equality URLs
    path('gender/1/', views.gender1, name='gender1'),
    path('gender/2/', views.gender2, name='gender2'),
    path('gender/3/', views.gender3, name='gender3'),
    path('gender/4/', views.gender4, name='gender4'),
    path('gender/5/', views.gender5, name='gender5'),

    #Economic Growth URLs
    path('economic/1/', views.economic1, name='economic1'),
    path('economic/2/', views.economic2, name='economic2'),
    path('economic/3/', views.economic3, name='economic3'),
    #Partnerships for the Goals URLs
    path('partnerships/1/', views.partnerships1, name='partnerships1'),
    path('partnerships/2/', views.partnerships2, name='partnerships2'),
    path('partnerships/3/', views.partnerships3, name='partnerships3'),
    path('partnerships/4/', views.partnerships4, name='partnerships4'),
    #Peace, Justice and Strong Institutions URLs
    path('pleace/1/', views.place1, name='pleace1'),
    path('pleace/2/', views.place2, name='pleace2'),
    #Industry, Innovation and Infrastructure URLs
    path('industry/1/', views.industry1, name='industry1'),
    path('industry/2/', views.industry2, name='industry2'),
    path('industry/3/', views.industry3, name='industry3'),



]
from django.conf.urls import handler404

handler404 = "api.views.custom_404"
