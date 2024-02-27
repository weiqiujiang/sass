# -*- coding: utf-8 -*-
# @Author: weiqiujiang
# @Date: 2024/2/27 23:39
from django.shortcuts import render, redirect, HttpResponse
from django import forms
from myapp import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^1[3456789]\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

    class Meta:
        model = models.UserInfo
        fields = '__all__'


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})