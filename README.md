# myapp
AI_application_sample

■このアプリの概要<br>
物体および顔検出における基本的なアプリの標準化  

■現在ある機能  
現場情報を持ち帰れないため、現在は最低限構成  
ログイン画面からのログイン  
新規ユーザ登録  
画像系AIのYOLOを用いた物体検出機能  

■フレームワーク  
Django  

■アプリ開発経緯  
現場知識のアウトプットおよびDjango開発における標準化  

■現在下記拡張中の機能  
・パスワード変更とか  
・YOLO以外での物体検出例実装  
・マッチング系AIの新規機能追加  

■以下構築手順  
・仮想環境の作成  
python -m venv venv_work  

・仮想環境の起動  
cd venv_work\Scripts  
activate.bat  

・仮想環境の停止  
deactivate  

・プロジェクトの作成(仮想環境上で）  
django-admin startproject myproject  

・アプリケーション作成  
python manage.py startapp myapp  

・apps.pyモジュールの確認  
class MyappConfig(AppConfig):  
    name = 'myapp'  

・settings.pyへの追記  
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
]

・DBの構築  
python manage.py makemigrations myapp  
python manage.py migrate  

(注意）
YOLOを使用するのでプロジェクト配下にyolov8.ptをいれていること  
いったんは25MB以上あるので格納していない。git上のultralytics/ultralyticsフォルダを格納してもよい
