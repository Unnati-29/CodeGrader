from django.urls import path
from .api_views import (
    SubmissionListCreateView, SubmissionDetailView,
    LeaderboardView, DashboardView
)

urlpatterns = [
    path('submissions/', SubmissionListCreateView.as_view(), name='submission-list'),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
    path('submissions/leaderboard/', LeaderboardView.as_view(), name='leaderboard-api'),
    path('submissions/dashboard/', DashboardView.as_view(), name='dashboard-api'),
]