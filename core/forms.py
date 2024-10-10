from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField 

class PeriodistaForm(ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Periodista
        fields = '__all__'

class TipoPeriodista(ModelForm):

    class Meta:
        model = TipoPeriodista
        fields = '__all__'

class NoticiaForm(ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Noticia
        fields = '__all__' 

class NoticiaPeriodistaForm(ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Noticia
        fields = ['periodista','TipoNoticia','titulo','descripcion','fecha','imagen','motivo']

class NoticiaPeriodistaaddForm(ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Noticia
        fields = ['periodista','TipoNoticia','titulo','descripcion','fecha','imagen']

class TipoNoticiaForm(ModelForm):
    
    class Meta:
        model = TipoNoticia
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = {'username','first_name','last_name','password1','password2'}

class solicitudesForm(ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Noticia
        fields = '__all__' 
        