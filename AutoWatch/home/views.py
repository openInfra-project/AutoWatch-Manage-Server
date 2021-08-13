from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import simplejson
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.datetime_safe import datetime
from main.models import Analytics

# 회원가입
global count


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
            try:
                user = User.objects.get(email=email)    # 아이디가 있는지 확인 해보고
            except User.DoesNotExist:                   # 아이디가 없어서 DoesNotExist이면 저장한다.
                user = User(email=email, username=username,
                            password=make_password(password))
                user.save()
                return redirect('/login')
            if(user):
                res_data['error'] = '존재하는 Email 입니다.'
                return render(request, 'home.html', res_data)


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
                request.session['user_email'] = user.email  # session 변수에 저장
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
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail"}))

        else:
            user = User(email=email, password=make_password(
                password), username=name)
            user.save()
            return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": name, "image": str(user.image)}))


@method_decorator(csrf_exempt, name='dispatch')
def app_login(request):
    # 앱에서 오는 로그인 요청
    if request.method == "POST":
        email = request.POST.get('email', None)
        print(email)
        password = request.POST.get('password', None)
        print(password)
        # 받은 이메일이랑 비밀번호 =데이터와 일치하면
        # 리턴값으로 숫자 200 = 로그인 성공
        # 일치 안하면 숫자 100 = 로그인 실패
        if User.objects.filter(email=email).exists():
            myuser = User.objects.get(email=email)
            # db에서 꺼내는 명령.Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(password, myuser.password):
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": myuser.username, "image": str(myuser.image)}))
            else:
                return HttpResponse(simplejson.dumps({"email": email, "password": password, "name": "Fail", "image": "Fail"}))

        else:
            return HttpResponse(simplejson.dumps({"email": "aa", "password": "aa", "name": "no", "image": "Fail"}))


@method_decorator(csrf_exempt, name='dispatch')
def app_delete(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
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
        return HttpResponse(simplejson.dumps({"image": str(myuser.image)}))


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
        date = myuser.registerd_date
        newdate = date.strftime("%Y-%m-%d %I:%M %p")
        print(newdate)
        print(date)
        print(email)
        print(name)
        print(image)

        return HttpResponse(simplejson.dumps({"email": email, "image": image, "name": name, "date": newdate}))


@method_decorator(csrf_exempt, name='dispatch')
def app_checkin(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        print(email)
        myuser = User.objects.get(email=email)
        myuser.check = True
        myuser.save()

        return HttpResponse(simplejson.dumps({"roomname": "yes"}))

# exam모드시 방 나가기


@method_decorator(csrf_exempt, name='dispatch')
def app_checkout(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        print(email)
        myuser = User.objects.get(email=email)
        myuser.check = False
        myuser.save()

        return HttpResponse(simplejson.dumps({"roomname": "yes"}))

# study모드시 방나가기


@method_decorator(csrf_exempt, name='dispatch')
def app_sendcount(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        count = request.POST.get('count', None)  # 앱 접근횟수
        nonperson = request.POST.get('nonperson', None)  # 자리이탈횟수
        roomname = request.POST.get('roomname', None)
        print(count)
        count_point = int(100) - (int(count)*10)
        nonperson_point = int(100)-(int(nonperson)*5)
        output = ''
        print(nonperson)
        print(roomname)
        myuser = User.objects.get(email=email)
        myuser.check = False
        myuser.save()
        analytics = Analytics.objects.filter(room_name=roomname)
        if analytics:  # 해당 룸의 row가 있다.
            for x in analytics:
                if(x.email == myuser.email):   # 해당 룸의 내 email을 가진 row가 있다.
                    output = 'YES'
                else:
                    output = 'NO'
        elif not(analytics):  # 해당 룸의 row가 없다 -> 내가 제일 처음 -> 바로 생성
            analytics = Analytics(
                room_name=roomname, email=email, person=nonperson_point, app=count_point)
            analytics.save()

        if output == 'YES':  # 해당 룸의 row 중에 내 아이디의 row가 있다.
            analytics = Analytics.objects.filter(email=email).last()
            analytics.person = nonperson_point
            analytics.app = count_point
            analytics.save()
        elif output == 'NO':  # 해당 룸의 row 중에 내 아이디의 row가 없다.
            analytics = Analytics(
                room_name=roomname, email=email, person=nonperson_point, app=count_point)
            analytics.save()

        return HttpResponse(simplejson.dumps({"roomname": "yes"}))
