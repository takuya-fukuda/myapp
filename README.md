# myapp
AI_application_sample

このアプリの概要
物体および顔検出における基本的なアプリの標準化
現在下記拡張中
・パスワード変更とか
・YOLO以外での物体検出例実装
・マッチング系AIの機能追加


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




YOLOを使用するのでプロジェクト配下にyolov8.ptをいれていること
いったんは25MB以上あるので格納していない。
