from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# 커스텀 User 모델
class User(AbstractUser):
    # 닉네임 필드 추가
    nickname = models.CharField(max_length=30)
    # 스탬프 개수 필드
    stamps = models.IntegerField(default=0)
    # 학번 필드
    student_id = models.CharField(max_length=10)
    # 학부 필드 (빈 값 허용)
    department = models.CharField(max_length=100, null=True, blank=True)
    # 대여 상태 필드
    is_renting = models.BooleanField(default=False)
    # 대여 시작 시간 필드
    rental_time = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = "user"  # 테이블 이름 지정

# 대여 코드 모델
class RentalCode(models.Model):
    code = models.CharField(max_length=10, unique=True)  # 대여 코드
    is_used = models.BooleanField(default=False)  # 사용 여부
    used_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # 코드 사용한 사용자 정보

    class Meta:
        db_table = "rental_code"  # 테이블 이름 지정

# 반환 코드 모델
class ReturnCode(models.Model):
    code = models.CharField(max_length=10, unique=True)  # 반환 코드
    is_used = models.BooleanField(default=False)  # 사용 여부
    used_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # 코드 사용한 사용자 정보

    class Meta:
        db_table = "return_code"  # 테이블 이름 지정

class ArduinoLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)  # 위치 데이터가 저장된 시간
    
    def __str__(self):
        return f"Lat: {self.latitude}, Lng: {self.longitude} at {self.timestamp}"
    class Meta:
        db_table = "arduino_location"  # 테이블 이름 지정