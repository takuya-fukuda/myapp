# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:28:06 2019

@author: asuto
"""


from django.urls import path

from . import views


urlpatterns=[
        path("",views.index, name = "index"),
        #ログアウト処理
        path("logout/",views.logout, name = "logout"),
        
        #新規ユーザー登録
        path("home/creatuser/",views.create_user,name = "createuser"),

        #detection画面
        path("home/detection/", views.image_detection, name = "detection"),

        #パスワードの変更(未完成)
        path("home/uppass/", views.updatePass, name="updatepass"),
        
        #ユーザの削除（未完成）
        path("home/deleteuser/", views.delete_user, name="deleteuser"),
        
]