from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment, TestCase
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

@login_required
def assignment_delete(request, pk):
    if request.user.profile.role != "teacher":
        return HttpResponseForbidden("Only teachers can delete assignments.")
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == "POST":
        assignment.delete()
        return redirect("assignment_list")
    return redirect("assignment_list")

@login_required
def assignment_create(request):
    if request.user.profile.role != "teacher":
        return HttpResponseForbidden("Only teachers can create assignments.")
    if request.method == "POST":
        # Assignment banao
        assignment = Assignment.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            marks=request.POST.get('marks'),
            deadline=request.POST.get('deadline'),
        )
        # Test cases banao
        input_data_list = request.POST.getlist('input_data[]')
        expected_output_list = request.POST.getlist('expected_output[]')
        for input_data, expected_output in zip(input_data_list, expected_output_list):
            if input_data.strip() and expected_output.strip():
                TestCase.objects.create(
                    assignment=assignment,
                    input_data=input_data.strip(),
                    expected_output=expected_output.strip(),
                )
        return redirect("assignment_list")
    return render(request, "assignments/create.html")