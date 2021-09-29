from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    first_name = None
    last_name = None
    groups = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setup_place = models.CharField(verbose_name='설치 장소', max_length=50)
    setup_day = models.CharField(verbose_name='설치 날짜', help_text='설치 날짜를 입력하시오, YYYY/MM/DD hh:mm:ss', max_length=19)
    company_name = models.CharField(verbose_name='업체명', help_text='업체명을 입력하시오', max_length=100)
    display = models.CharField(verbose_name='해상도', max_length=9, help_text='해상도를 입력하시오, NxM')
    max_brgt = models.IntegerField(verbose_name='최대 밝기', default=0)
    player_serial = models.CharField(verbose_name='플레이어 Serial', unique=True, primary_key=True, max_length=16)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
