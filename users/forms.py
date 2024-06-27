from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label = 'Имя пользователя или E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'phone_number', 'first_name')
        labels = {
            'email': 'E-Mail',
            'first_name': 'Имя'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
        }
        
        help_texts = {
            'phone_number': 'Укажите номер телефона в формате +7 ХХХ ХХХХХХX'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('Данный адрес электронной почты уже зарегистрирован в системе')
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Данный номер телефона уже зарегистрирован в системе')
        return phone_number
    
    
class ProfileUserForm(forms.ModelForm):
    photo = forms.ImageField(
        label='Фотография',
        required=False
    )
    
    
    username = forms.CharField(
        disabled=False,  
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'})  
    )
    email = forms.CharField(
        disabled=False,  
        label='E-mail',
        widget=forms.TextInput(attrs={'class': 'form-control'}) 
    )
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','phone_number', 'first_name', 'last_name', 'photo']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'photo': 'Фотография'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
        }
        
        
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(label='Повтор нового пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение нового пароля'}))