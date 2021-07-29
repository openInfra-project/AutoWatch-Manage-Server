from django.http import response
from django.shortcuts import render
from home.models import User

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
            return render(request,'makeroom.html',res_data)
        elif request.method == 'POST':
            room_name = request.POST.get('room-name',None)
            room_password = request.POST.get('room-password',None)
            file = request.POST.get('file',None)
            study = request.POST.getlist('study')
            exam = request.POST.getlist('exam')
            
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
                    return render(request,'makeroom.html')
            return render(request,'makeroom.html',res_data)  # room 정보 비정상 일시
    

    
def enteroom(request):
    res_data={}
    user_session = request.session.get('user')
    if user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username
        return render(request,'enteroom.html',res_data)
    else:
        return render(request,'login.html') 