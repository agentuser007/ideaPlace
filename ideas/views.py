from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Idea, Like
from .forms import IdeaForm
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from ideas.models import Idea
from django.db.models import Subquery, OuterRef
from django.contrib import messages

def user_ideas(request):
    # Get all ideas created by the current user
    ideas = Idea.objects.filter(user=request.user)
    context = {
        'ideas': ideas,
    }
    return render(request, 'user_profile.html', context)

@login_required
def user_profile(request):
    user = request.user
    ideas = Idea.objects.filter(user=request.user)
    #likes = Like.objects.filter(user=request.user)
    liked_ideas = Like.objects.filter(user=request.user)
    return render(request, 'user_profile.html', {'user': user, 'ideas': ideas, 'liked_ideas': liked_ideas})

@login_required
def idea_like(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    liked = False
    like = Like.objects.filter(user=request.user, idea=idea)
    if like:
        like.delete()
        idea.likes.remove(request.user)
        messages.success(request, 'You unliked this idea.')
    else:
        liked = True
        Like.objects.create(user=request.user, idea=idea)
        idea.likes.add(request.user)
        messages.success(request, 'Idea liked successfully.')
    idea.save()
    return redirect('idea_detail', pk=pk)

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

def home_view(request):
    ideas = Idea.objects.all()
    return render(request, 'home.html', {'ideas': ideas})
    


def idea_list(request):
    ideas = Idea.objects.all()
    return render(request, 'idea_list.html', {'ideas': ideas})


@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'idea_form.html', {'form': form})


def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'idea_detail.html', {'idea': idea})


@login_required
def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.user == idea.user:
        if request.method == 'POST':
            form = IdeaForm(request.POST, instance=idea)
            if form.is_valid():
                form.save()
                return redirect('idea_detail', pk=idea.pk)
        else:
            form = IdeaForm(instance=idea)
        return render(request, 'idea_form.html', {'form': form})
    else:
        return HttpResponse('You are not authorized to edit this idea.')


@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.user == idea.user:
        idea.delete()
        return redirect('user_profile')
    else:
        return HttpResponse('You are not authorized to delete this idea.')


@staff_member_required
def idea_admin(request):
    ideas = Idea.objects.all()
    return render(request, 'idea_admin.html', {'ideas': ideas})


