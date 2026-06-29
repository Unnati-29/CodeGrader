from rest_framework import serializers
from .models import Assignment, TestCase


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ('id', 'input_data', 'expected_output')


class AssignmentSerializer(serializers.ModelSerializer):
    test_cases = TestCaseSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ('id', 'title', 'description', 'marks', 'deadline', 'created_at', 'test_cases')
        read_only_fields = ('created_at',)


class AssignmentCreateSerializer(serializers.ModelSerializer):
    test_cases = TestCaseSerializer(many=True)

    class Meta:
        model = Assignment
        fields = ('title', 'description', 'marks', 'deadline', 'test_cases')

    def create(self, validated_data):
        test_cases_data = validated_data.pop('test_cases')
        assignment = Assignment.objects.create(**validated_data)
        for tc in test_cases_data:
            TestCase.objects.create(assignment=assignment, **tc)
        return assignment