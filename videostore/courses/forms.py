from django import forms
from .models import Course


class CourseAddForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Название URL',
        label_suffix='*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL'})
    )
    title = forms.CharField(
        label='Название курса',
        label_suffix='*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название курса'})
    )
    description = forms.CharField(
        label='Описание курса',
        label_suffix='*',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание курса'})
    )
    img = forms.ImageField(
        label='Загрузить изображение',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']
