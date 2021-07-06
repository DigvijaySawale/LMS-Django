from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import IssueBook,Book,Student


class IssueForm(ModelForm):
    class Meta:
        model= IssueBook
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'     


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
		
		