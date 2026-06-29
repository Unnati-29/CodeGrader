from rest_framework import serializers
from .models import Submissions


class SubmissionSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username', read_only=True)
    assignment_title = serializers.CharField(source='assignment.title', read_only=True)

    class Meta:
        model = Submissions
        fields = (
            'id', 'student', 'student_username', 'assignment', 'assignment_title',
            'code', 'score', 'feedback', 'submitted_at'
        )
        read_only_fields = ('student', 'score', 'feedback', 'submitted_at')


class SubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = ('assignment', 'code')


class LeaderboardSerializer(serializers.Serializer):
    student__username = serializers.CharField()
    total_score = serializers.FloatField()