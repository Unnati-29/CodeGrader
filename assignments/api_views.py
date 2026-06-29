from rest_framework import generics, permissions
from .models import Assignment
from .serializers import AssignmentSerializer, AssignmentCreateSerializer


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'profile') and
            request.user.profile.role == 'teacher'
        )


class AssignmentListCreateView(generics.ListCreateAPIView):
    
    queryset = Assignment.objects.all().order_by('-created_at')
    permission_classes = [IsTeacherOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AssignmentCreateSerializer
        return AssignmentSerializer


class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Assignment.objects.all()
    permission_classes = [IsTeacherOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return AssignmentCreateSerializer
        return AssignmentSerializer