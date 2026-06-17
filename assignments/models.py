from django.db import models
from django.utils import timezone
# Create your models here.
class Assignment(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    marks = models.PositiveIntegerField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class TestCase(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,
           related_name="test_cases")
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"TestCase for {self.assignment.title}"