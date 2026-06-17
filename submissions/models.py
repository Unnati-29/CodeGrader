from django.db import models
from django.utils import timezone
from assignments.models import Assignment

# Create your models here.
class Submissions(models.Model):
    student_name = models.CharField( max_length=50)
    code = models.TextField()
    Assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    feedback = models.TextField(blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name
