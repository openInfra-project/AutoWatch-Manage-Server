from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import User

# 회원가입
def home(request):
    res_data={}
    if request.method =='GET':
        return render(request,'home.html')
    elif request.method == 'POST':
        email = request.POST.get('email',None)
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        if password != re_password:
            res_data['error'] = '비밀 번호가 다릅니다.'
            return render(request, 'home.html', res_data,context='#contact')

        user = User(email=email,username=username,password=password)
        user.save()

        return redirect('/login')

#로그인
def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        res_data ={}   # 딕션어리 = key, value 값을 가지는 변수
        if not(email and password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif not(email):
            res_data['error'] = '이메일을 입력하세요.'
        elif not(password):
            res_data['error'] = '비밀번호를 입력하세요.'
        else:
            try:
                user = User.objects.get(email=email) # 필드명 = 값 이면 user 객체 생성
            except User.DoesNotExist:
                res_data['error'] = '존재하지 않는 아이디 입니다.'    # 아이디가 없는 예외 처리
                return render(request,'login.html',res_data)

            user_password = user.password
            if user_password == password:
                request.session['user'] = user.id  # session 변수에 저장
                return redirect('/main')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
                return render(request,'login.html',res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')         