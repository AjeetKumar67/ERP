from django.urls import path
from .views import OnlineClassListView, AssignmentSubmissionView, QuizView

urlpatterns = [
    path('classes/', OnlineClassListView.as_view(), name='online-class-list'),
    path('assignments/', AssignmentSubmissionView.as_view(), name='assignment-submission'),
    path('quizzes/', QuizView.as_view(), name='quiz'),
]