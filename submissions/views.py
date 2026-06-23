from django.shortcuts import render,redirect
from .forms import SubmissionForm
from assignments.models import Assignment
from .models import Submissions
from .evaluator import evaluator_submission

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
            score, feedback = evaluator_submission(submission.code,assignment)

            submission.score = score
            submission.feedback = feedback           
            submission.save()

        return redirect('submission_result',submission_id=submission.id)

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

    return render(request,'submissions/list.html',{'submissions': submissions})

def submission_result(request, submission_id):
    submission = Submissions.objects.get(id=submission_id)

    return render(request,'submissions/result.html',{'submission': submission})