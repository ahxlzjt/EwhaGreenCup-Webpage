from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from user.models import User, ReturnCode, RentalCode, ArduinoLocation
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def home(request):
    return render(request, 'page/home.html')

def returnvalue(request):
    if request.method == "POST":
        input_code = request.POST.get('search_text')

        try:
            return_code = ReturnCode.objects.get(code=input_code, is_used=False)
            user = request.user
            user.stamps += 1
            show_popup = False

            if user.stamps >= 5:
                user.stamps = 0
                show_popup = True

            user.is_renting = False  # 대여 상태 초기화
            user.save()

            return_code.is_used = True
            return_code.used_by = request.user
            return_code.save()

            if 'rental_time' in request.session:
                del request.session['rental_time']

            messages.success(request, "반환 코드가 확인되었습니다. 스탬프가 추가되었습니다.")
            if show_popup:
                return render(request, 'page/popup.html')

            return redirect('board')

        except ReturnCode.DoesNotExist:
            messages.error(request, "잘못된 반환 코드입니다. 다시 시도해주세요.")
            return redirect('returnvalue')

    return render(request, 'page/returnvalue.html')


@never_cache
@login_required
def rentalvalue(request):
    if request.user.is_renting:
        return redirect('rental')

    if request.method == "POST":
        input_code = request.POST.get('search1_text')

        try:
            rental_code = RentalCode.objects.get(code=input_code, is_used=False)
            rental_code.is_used = True
            rental_code.used_by = request.user
            rental_code.save()

            rental_time = datetime.datetime.now()
            request.user.rental_time = rental_time  # 사용자 모델에 대여 시간 저장
            request.user.is_renting = True
            request.user.save()

            # 세션에 대여 시작 시간 저장
            request.session['rental_time'] = rental_time.strftime('%Y-%m-%d %H:%M:%S')

            messages.success(request, "대여 코드가 확인되었습니다. 대여가 완료되었습니다.")
            return redirect('rental')

        except RentalCode.DoesNotExist:
            messages.error(request, "잘못된 대여 코드입니다. 다시 시도해주세요.")
            return redirect('rentalvalue')

    return render(request, 'page/rentalvalue.html')

@never_cache
def rental(request):
    rental_time = request.session.get('rental_time', None)

    if rental_time:
        rental_time = datetime.datetime.strptime(rental_time, '%Y-%m-%d %H:%M:%S')
        current_time = datetime.datetime.now()
        time_elapsed = current_time - rental_time

        context = {
            'rental_time': rental_time,
            'time_elapsed': time_elapsed,
        }

        return render(request, 'page/rental.html', context)
    
    else:
        # 세션이 없는데 사용자가 여전히 대여 상태인 경우 초기화
        if request.user.is_renting:
            request.user.is_renting = False
            request.user.save()
        messages.error(request, "대여 시작 시간이 기록되지 않았습니다. 다시 시도해주세요.")
        return redirect('rentalvalue')

def get_arduino_location(request):
    latest_location = ArduinoLocation.objects.last()  # 가장 최근의 위치 정보 가져오기
    if latest_location:
        return JsonResponse({
            'lat': latest_location.latitude,
            'lng': latest_location.longitude,
            'timestamp': latest_location.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return JsonResponse({'error': 'No location data available'}, status=404)

def position(request):
    if request.method == "GET":
        return render(request, 'page/position.html')
    
def position1(request):
    if request.method == "GET":
        return render(request, 'page/position1.html')

def sidebar(request):
    if request.method == "GET":
        return render(request, 'page/sidebar.html')

def sidebar1(request):
    if request.method == "GET":
        return render(request, 'page/sidebar1.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # 로그인 시 rental_time이 있으면 세션에 저장
            if user.rental_time:
                request.session['rental_time'] = user.rental_time.strftime('%Y-%m-%d %H:%M:%S')

            if user.is_renting:
                return redirect('rental')
            else:
                return redirect('board')
        else:
            messages.error(request, "입력값을 확인해 주세요")
            return redirect('signin')

    return render(request, 'page/signin.html')
        
def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')

    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        nickname=request.POST['nickname']
        student_id = request.POST['student_id']
        department = request.POST['department']
        
        user = User.objects.filter(username=username)
        # exists - 존재하면 True, 존재하지 않으면 False
        if user.exists():
            messages.error(request, "이미 가입한 아이디입니다.")
            return redirect('signup')
        else:
            new_user = User(
                username=username,
                password=make_password(password),
                nickname=nickname,
                student_id=student_id,
                department=department,
            )
            new_user.save()
            login(request, new_user)
            return redirect("board")
        
def signout(request):
    if request.method=="GET":
        logout(request)
        return redirect("board")
    
