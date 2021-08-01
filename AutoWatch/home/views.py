from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import simplejson
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# 회원가입


def home(request):
    res_data = {}
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'home.html', res_data)
        else:  # 아이디 중복 체크
            user = User.objects.get(email=email)
            if(user):
                res_data['error'] = '존재하는 Email 입니다.'
                return render(request, 'home.html', res_data)

        # 위의 조건문에서 걸리지 않으면 회원가입 성공
        user = User(email=email, username=username, password=password)
        user.save()
        return redirect('/login')

# 로그인


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        res_data = {}   # 딕션어리 = key, value 값을 가지는 변수
        if not(email and password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif not(email):
            res_data['error'] = '이메일을 입력하세요.'
        elif not(password):
            res_data['error'] = '비밀번호를 입력하세요.'
        else:
            try:
                user = User.objects.get(email=email)  # 필드명 = 값 이면 user 객체 생성
            except User.DoesNotExist:
                res_data['error'] = '존재하지 않는 아이디 입니다.'    # 아이디가 없는 예외 처리
                return render(request, 'login.html', res_data)

            user_password = user.password
            if check_password(password, user_password):
                request.session['user'] = user.id  # session 변수에 저장
                return redirect('/main')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
                return render(request, 'login.html', res_data)
        return render(request, 'login.html', res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


@method_decorator(csrf_exempt, name='dispatch')
def app_signup(request):
    # 앱 에서 오는 POST 요청
    if request.method == "GET":
        return render(request, 'main/app_signup.html')
    elif request.method == "POST":
        #data = JSONParser().parse(request)
        #serializer = PostSerializer(data=data)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        name = request.POST.get('name', None)
        print(email)
        if User.objects.filter(email=email).exists():
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail"}))

        else:
            user = User(email=email, password=make_password(
                password), username=name)
            user.save()
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": name}))


@method_decorator(csrf_exempt, name='dispatch')
def app_login(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        # 받은 이메일이랑 비밀번호 =데이터와 일치하면
        # 리턴값으로 숫자 200 = 로그인 성공
        # 일치 안하면 숫자 100 = 로그인 실패
        if User.objects.filter(email=email).exists():
            myuser = User.objects.get(email=email)
            # db에서 꺼내는 명령.Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(password, myuser.password):
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": myuser.username}))
            else:
                return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail"}))

        else:
            return HttpResponse(simplejson.dumps({"email": "aa", "password": "aa", "name": "Fail"}))


@method_decorator(csrf_exempt, name='dispatch')
def app_delete(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        mydelete = User.objects.get(email=email)
        mydelete.delete()
        return HttpResponse(200)


@method_decorator(csrf_exempt, name='dispatch')
def app_image(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        res_data = {}
        image = request.FILES['image']
        print(image)
        fs = FileSystemStorage()
        res_data['image_url'] = fs.url(image.name)
        text = list(image.name)
        del text[len(text)-4:len(text)]
        a = ''.join(text)
        myuser = User.objects.get(email=a)
        myuser.image = image
        myuser.save()
        return HttpResponse(simplejson.dumps({"image": "ok"}))  # 이미지 변경완료


@method_decorator(csrf_exempt, name='dispatch')
def app_modify(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        name = request.POST.get("username", None)
        myuser = User.objects.get(email=email)
        myuser.username = name
        myuser.save()
        return HttpResponse(simplejson.dumps({"email": "aa", "password": "aa", "name": myuser.username}))


@method_decorator(csrf_exempt, name='dispatch')
def app_mypage(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        myuser = User.objects.get(email=email)
        name = myuser.username
        image = str(myuser.image)
        print(email)
        print(name)
        print(image)

        return HttpResponse(simplejson.dumps({"email": email, "image": image, "name": name}))
