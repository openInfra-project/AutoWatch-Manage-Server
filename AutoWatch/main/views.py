from django.http import response
from django.shortcuts import redirect, render
from home.models import User
from .models import Room
import string, random

def main(request):
    res_data={}
    user_session = request.session.get('user')               #로그인 체크
    if user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username
        return render(request,'main.html',res_data)
    else:
        return render(request,'login.html')


def makeroom(request):
    res_data={}
    user_session = request.session.get('user')
    if user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username                # 로그인 체크
        if request.method == 'GET':
            res_data['string'] = ''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(7))  # 랜덤 문자열 생성
            return render(request,'makeroom.html',res_data)
        elif request.method == 'POST':
            room_name = request.POST.get('room-name',None)
            room_password = request.POST.get('room-password',None)
            file = request.POST.get('file',None)
            study = request.POST.getlist('study')
            exam = request.POST.getlist('exam')
            maker = user.email

            request.session['room_name'] = room_name
            request.session['file'] = file
            request.session['study'] = study
            request.session['exam'] = exam
            request.session['maker'] = maker

            if (len(room_name) > 7):
                res_data['name_error'] = '방 이름을 생성해 주세요.'
            elif not(room_password):
                res_data['password_error'] = '비밀번호를 생성해 주세요.'
            elif not(study or exam):
                res_data['mode_error'] = 'Mode를 선택해 주세요.'    
            else:
                if (exam and not(file)):
                    res_data['file_error'] = 'Exam Mode는 명단 첨부가 필수 입니다.'
                    return render(request,'makeroom.html',res_data)  # room 정보 비정상 일시
                else:  # 정상적으로 room 정보 기입시
                    if study and not(exam):     # mode를 db에 저장
                        mode = 'STUDY'
                    elif exam and not(study):
                        mode = 'EXAM'
                    room = Room(room_name=room_name, room_password=room_password, file=file,mode=mode ,maker=maker) # db에 room 정보 저장
                    room.save()   
                    return redirect('/main/makeroom/success')
            return render(request,'makeroom.html',res_data)  # room 정보 비정상 일시
    
def make_success(request):
    res_data={}
    room_session = request.session.get('room_name')   # 아까 POST 할때 session에 저장한 값 불러옴
    user_session = request.session.get('user')
    if room_session and user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username
        
        room = Room.objects.get(room_name=room_session)   # 가장 최근의 room_name과 session에 저장한 것을 비교함
        res_data['room_name'] = room.room_name
        res_data['room_password'] = room.room_password
        res_data['mode'] = room.mode
        res_data['maker'] = room.maker  
        if request.method == 'GET':
            return render(request,'make_success.html',res_data)
        elif request.method == 'POST':
            return render(request,'ssimong.html')

def enteroom(request):
    res_data={}
    user_session = request.session.get('user')
    if user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username
        if request.method == 'GET':
            return render(request,'enteroom.html',res_data)
        elif request.method == 'POST':
            room_name = request.POST.get('room_name')
            room_password = request.POST.get('room_password')
            if not(room_name):
                res_data['name_error'] = 'Room 이름을 입력하세요.'
            elif not(room_password):
                res_data['password_error'] = 'Room 비밀번호를 입력하세요.'
            elif not(room_name and room_password):
                res_data['all_error'] = '모든 값을 입력하세요.'
            else:
                try:
                    room = Room.objects.get(room_name=room_name) # 필드명 = 값 이면 Room 객체 생성
                except Room.DoesNotExist:
                    res_data['error'] = '존재하지 않는 Room 입니다.'    # room이 없는 예외 처리
                    return render(request,'enteroom.html',res_data)

                db_password = room.room_password
                if db_password == room_password:     # room 정상 입장
                    return render(request, 'ssimong.html')
                else:
                    res_data['error'] = '비밀번호가 틀렸습니다.'
                    return render(request, 'enteroom.html',res_data)
            return render(request,'enteroom.html',res_data)  # room 정보 비정상 일시
