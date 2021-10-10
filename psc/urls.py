from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('account_verified/<slug:token>',views.account_verified,name="account_verified")
]