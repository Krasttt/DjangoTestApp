from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .utils import DBWorker


@login_required
def list_of_lessons(request):
    lessons = DBWorker.find_all()
    context = {
        'title': 'Lessons',
        'lessons': lessons
    }
    return render(request, 'academy/list_of_lessons.html', context)


@login_required
def lesson(request, lesson_id):
    lesson = DBWorker.find_by_id(lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'academy/lesson.html', context)


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.data.get('username'), 'test@test.com', form.data.get('password'))
            user.save()
            context = {
                'title': 'Sign In',
                'form': UserForm()
            }
            return redirect('/sign-in', context)
        else:
            error = 'The username or password were incorrect.'
    form = UserForm()
    context = {
        'title': 'Sign Up',
        'form': form,
        'error': error
    }
    return render(request, 'academy/registration.html', context)


def sign_in(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        user = authenticate(username=form.data.get('username'), password=form.data.get('password'))
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('list_of_lessons')
            else:
                error = "The password is valid, but the account has been disabled!"
        else:
            error = "The username or password were incorrect."

    form = UserForm()
    context = {
        'title': 'Sign In',
        'form': form,
        'error': error
    }
    return render(request, 'academy/sign_in.html', context)


@login_required
def logout_view(request):
    logout(request)
    context = {
        'form': UserForm()
    }
    return redirect('/sign-in', context)
