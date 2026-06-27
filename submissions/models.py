from django.db import models
from django.utils import timezone
from assignments.models import Assignment
from django.contrib.auth.models import User

# Create your models here.
class Submissions(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="submissions")
    code = models.TextField()
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    feedback = models.TextField(blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student.username
