from django.shortcuts import render,redirect
from .forms import SubmissionForm
from assignments.models import Assignment
from .models import Submissions
from .evaluator import evaluator_submission
from django.db.models import Sum , Max
from django.contrib.auth.decorators import login_required

# Create your views here.

def submit(request, assignment_id):
    assignment = Assignment.objects.get(
        id=assignment_id
    )
    if request.method == "POST":

        form = SubmissionForm(request.POST)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
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

def leaderboard(request):

    leaderboard_data = (Submissions.objects.values("student__username").annotate(total_score=Sum("score")).order_by("-total_score"))

    return render(request,'submissions/leaderboard.html',{'leaderboard_data': leaderboard_data})

@login_required
def dashboard(request):
    submissions = Submissions.objects.filter(student=request.user)

    total_submissions = submissions.count()

    best_score = submissions.aggregate(Max("score"))["score__max"] or 0

    context = {
        "total_submissions": total_submissions,
        "best_score": best_score,
        "submissions": submissions[:5],   # latest 5
    }
    return render(request, "submissions/dashboard.html", context)