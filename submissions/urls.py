from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:assignment_id>/',views.submit,name='submit'),
    path('submissions/', views.submission_list, name='submission_list'),
    path('result/<int:submission_id>/', views.submission_result,name='submission_result'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
]