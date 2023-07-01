from django.shortcuts import render,redirect
from  django.template import loader
from .models import User,Photo
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from glob import glob
import json
from datetime import datetime,timedelta
import os
#データ分析用のライブラリ
import pandas as pd
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
import japanize_matplotlib
import scipy.cluster as cluster
import random

#YOLOのインポート
from ultralytics import YOLO
from PIL import Image

# Create your views here.

#初回のＵＲＬ遷移
def index(request):
    form = LoginForm()  #ログインフォーム生成
    usform = CreateUserForm() #ユーザー登録フォーム生成
    context={"form":form,"usform":usform}
    #ログインページにジャンプ
    return render(request,"myapp/login.html",context=context)

def logout(request):
    request.session.clear()
    return index(request)

#パスワードの更新
def updatePass(request):
    if "POST" == request.method:
        uppass = UpdatePasswordForm(request.POST)
        uid = request.session["user"]["id"]
    
        if uppass.is_valid():
            password = uppass.cleaned_data.get("password")

            user = User.objects.filter(id=uid)[0]
            user.password = password
        
            #DB更新
            user.save()
        
        return redirect(request.META['HTTP_REFERER'])
    else:
        return mypage(request)

#ユーザーの追加
def create_user(request):
    if "POST" == request.method:
        new_user = CreateUserForm(request.POST,request.FILES)
        
        if new_user.is_valid():
            name = new_user.cleaned_data.get("name")
            pw = new_user.cleaned_data.get("pw")

            
            u = User(account_name=name, password=pw)

            #DB追加
            u.save()
        else:
            form = LoginForm()  #ログインフォーム生成
            usform = new_user
            context={"form":form,"usform":usform}
            #ログインページにジャンプ
            return render(request,"myapp/login.html",context=context)

    return index(request)
        
#ユーザーの削除
def delete_user(request):

    uid = request.session["user"]["id"]
    user = User.objects.filter(id=uid)[0]
    friends = Friend.objects.filter(my_num=uid)

    user.delete()
    friends.delete()

    return index(request)


#自分アレンジ
def image_detection(request):
    if "GET" == request.method:
        #セッションにログイン情報がない時
        if not "user" in request.session:
                
            f = LoginForm(request.GET)
                
            #入力チェック
            if f.is_valid():            
                name = f.cleaned_data.get("name")
                password = f.cleaned_data.get("password")

                #DB検索
                parameter={"account_name":name,"password":password}
                u = User.objects.filter(**parameter)
            
                if len(u) == 0:#DBにいない
                    return index(request)
                #辞書型リストに変換して、0番目の辞書をuに再代入
                u = u.values()[0]
            
                #セッションに格納
                request.session["user"]=u
            else:
                return index(request) 
        #セッションにログイン情報があるとき
        else:
            u = request.session["user"]

        dform = CreateDetectionForm()
        context={"dform":dform}
        return render(request,"myapp/detection.html",context)
    
    elif "POST" == request.method:

        dform = CreateDetectionForm(request.POST,request.FILES)

        #ファイルの不正チェック
        if dform.is_valid():
            image = dform.cleaned_data.get("image")
            #return HttpResponse(str(image))
        
            photo = Photo()
            photo.image=image
            photo.save()

            url = 'myapp/static/media/myapp/' + str(image)

            img = str(image)

            print(url)
            print(os.getcwd())

            model = YOLO("yolov8x.pt")
            #results = model("samplesns/static/media/samplesns/bus.png",save=True)
            #results = model(url,save=True)
            results = model.predict(source=url,
                                    project='myapp/static/media/output/',
                                    name='mypredict',
                                    exist_ok=True,
                                    save=True)


            #url2 = '/media/output/' + str(image)

        #return render(request,"samplesns/detection.html")
        return render(request,"myapp/detection.html", context={"dform": dform,"img":img})

