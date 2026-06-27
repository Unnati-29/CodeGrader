from django.shortcuts import render, get_object_or_404, redirect
from urllib3 import request
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/list.html', {'assignments': assignments})

def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return render(request, 'assignments/detail.html', {'assignment': assignment})

@login_required
def assignment_create(request):

    if request.user.profile.role != "teacher":
        return HttpResponseForbidden("Only teachers can create assignments.")

    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("assignment_list")
    else:
        form = AssignmentForm()

    return render(
        request,
        "assignments/create.html",
        {
            "form": form
        }
    )