from django.urls import path
from .views import (
    ClassListView,
    SubjectListView,
    ChapterListView,
    QuestionListView,
    ScoreCreateView
)

urlpatterns = [
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/<int:class_id>/subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/chapters/', ChapterListView.as_view(), name='chapter-list'),
    path('chapters/<int:chapter_id>/questions/', QuestionListView.as_view(), name='question-list'),
    path('scores/submit/', ScoreCreateView.as_view(), name='score-create'),
]