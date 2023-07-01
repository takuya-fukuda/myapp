# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:30:39 2019

@author: asuto
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:10:56 2019

@author: asuto
"""


from django import forms
from .models import User



class LoginForm(forms.Form):
    name = forms.CharField(label="",required=True, max_length=100,
                           widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"ユーザ名"}))
    password = forms.CharField(label="",required=True,max_length=100,
                               widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"パスワード"}))

class UploadFileForm(forms.Form):
    text = forms.CharField(label="",max_length=200,widget=forms.TextInput(attrs={"placeholder":"投稿メッセージを入力", "class":"form-control"}))
    image = forms.ImageField(label="", required=True)

class UpdatePasswordForm(forms.Form):
    password = forms.CharField(label="", max_length=20,min_length=8,required=True,widget=forms.PasswordInput(attrs={"placeholder":"新しいパスワード", "class":"form-control"}))
    re_password = forms.CharField(label="", max_length=20,min_length=8,required=True,widget=forms.PasswordInput(attrs={"placeholder":"もう一度新しいパスワード", "class":"form-control","oninput":"checkPassword(this)"}))


class CreateUserForm(forms.Form):
    name = forms.CharField(label="",required=True, max_length=100,
                           widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ユーザ名"}))
    pw = forms.CharField(label="", max_length=20,min_length=8,required=True,widget=forms.PasswordInput(attrs={"placeholder":"パスワード", "class":"form-control"}))
    re_pw = forms.CharField(label="", max_length=20, min_length=8, required=True, widget=forms.PasswordInput(attrs={"placeholder": "もう一度パスワード", "class": "form-control", "oninput": "checkPassword(this)"}))

    def clean_name(self):
        ac_name = self.cleaned_data.get('name')
        if User.objects.filter(account_name=ac_name).count() > 0:
            raise forms.ValidationError("その名前は既に登録されています。")
        return ac_name
    
class CreateDetectionForm(forms.Form):
    image = forms.ImageField(label="", required=True)