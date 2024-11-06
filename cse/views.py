from django.shortcuts import render, redirect
from .models import Post, students
from .forms import studentForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'cse/post_list.html', {'posts': posts})


def student_list(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = studentForm()

    all_students = students.objects.all()

    context = {
        'students': all_students,
        'form': form,
    }
    return render(request, 'cse/student_list.html', context)
