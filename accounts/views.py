from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """处理用户注册"""
    if request.method != 'POST':
        # 显示空表单
        form = UserCreationForm()
    else:
        # 处理填好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 自动登录用户
            login(request, new_user)
            return redirect('learning_logs:index')

    # 显示空或无效表单
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# Create your views here.
