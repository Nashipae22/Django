from django.urls import path
from. import views

urlpatterns = [
    path('',views.home, name="home"),
    path('homep/',views.home, name="home"),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/', views.account, name='account'),
    path('more/', views.more, name='more'),
    path('house/', views.house, name='house'),
    path('elect/', views.elect, name='elect'),
    path('kitch/', views.kitch, name='kitch'),
    path('bath/', views.bath, name='bath'),
    path('search/', views.search, name='search'),
]
