from django.shortcuts import render,redirect
from .forms import SubmissionForm
from assignments.models import Assignment
from .models import Submissions

# Create your views here.

def submit(request, assignment_id):
    assignment = Assignment.objects.get(
        id=assignment_id
    )
    if request.method == "POST":

        form = SubmissionForm(request.POST)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.save()

            return redirect('assignment_detail',pk=assignment.id)

    else:
        form = SubmissionForm()

    return render(
        request,
        'submissions/submit.html',
        {
            'form': form,
            'assignment': assignment
        }
    )


def submission_list(request):
    submissions = Submissions.objects.all().order_by('-submitted_at')

    return render(
        request,
        'submissions/list.html',
        {
            'submissions': submissions
        }
    )