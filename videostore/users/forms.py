from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text="Пароль не должен быть маленьким и простым",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.Form):
# чтобы работала подстановка значений текущего пользователя, нужно поменять наследование класса.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email*',
        label_suffix='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    username = forms.CharField(
        label='Имя пользователя*',
        label_suffix='',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )
    gender_list = (
        ('M', 'Мужской'),
        ('F', 'Женский')
    )
    gender = forms.ChoiceField(
        label='Выберите пол*',
        label_suffix='',
        required=True,
        choices=gender_list,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    agree = forms.BooleanField(
        label='Соглашение про отправку уведомлений на почту',
        label_suffix='',
        required=False,
        widget=forms.CheckboxInput(attrs={'class:': 'myclass'})
    )

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'agree']
