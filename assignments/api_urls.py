from django.urls import path
from .api_views import AssignmentListCreateView, AssignmentDetailView

urlpatterns = [
    path('assignments/', AssignmentListCreateView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
]