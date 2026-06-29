from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Max
from .models import Submissions
from .evaluator import evaluator_submission
from .serializers import SubmissionSerializer, SubmissionCreateSerializer


class SubmissionListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'profile') and user.profile.role == 'teacher':
            return Submissions.objects.all().order_by('-submitted_at')
        return Submissions.objects.filter(student=user).order_by('-submitted_at')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubmissionCreateSerializer
        return SubmissionSerializer

    def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        assignment = serializer.validated_data['assignment']
        code = serializer.validated_data['code']

        score, feedback = evaluator_submission(code, assignment)

        submission = Submissions.objects.create(
            student=request.user,
            assignment=assignment,
            code=code,
            score=score,
            feedback=feedback,
        )
        return Response(SubmissionSerializer(submission).data, status=status.HTTP_201_CREATED)


class SubmissionDetailView(generics.RetrieveAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'profile') and user.profile.role == 'teacher':
            return Submissions.objects.all()
        return Submissions.objects.filter(student=user)


class LeaderboardView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = (
            Submissions.objects.values('student__username')
            .annotate(total_score=Sum('score'))
            .order_by('-total_score')
        )
        return Response(list(data))


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        submissions = Submissions.objects.filter(student=request.user)
        total_submissions = submissions.count()
        best_score = submissions.aggregate(Max('score'))['score__max'] or 0
        return Response({
            'total_submissions': total_submissions,
            'best_score': best_score,
            'recent_submissions': SubmissionSerializer(submissions[:5], many=True).data,
        })