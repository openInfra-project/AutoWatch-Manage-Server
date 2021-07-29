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
        res_data['username'] = user.username
        if request.method == 'GET':
            return render(request,'makeroom.html',res_data)
        elif request.method == 'POST':
            room_name = request.POST
    else:
        return render(request,'login.html')
    

    
def enteroom(request):
    res_data={}
    user_session = request.session.get('user')
    if user_session:
        user = User.objects.get(pk=user_session)
        res_data['username'] = user.username
        return render(request,'enteroom.html',res_data)
    else:
        return render(request,'login.html') 