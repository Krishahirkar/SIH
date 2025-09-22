from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Class, Subject, Chapter, Question, Score
from .serializers import (
    ClassSerializer,
    SubjectSerializer,
    ChapterSerializer,
    QuestionSerializer,
    ScoreSerializer
)

class ClassListView(generics.ListAPIView):
    queryset = Class.objects.all().order_by('level')
    serializer_class = ClassSerializer

class SubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        class_id = self.kwargs['class_id']
        return Subject.objects.filter(school_class_id=class_id)

class ChapterListView(generics.ListAPIView):
    serializer_class = ChapterSerializer
    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Chapter.objects.filter(subject_id=subject_id).order_by('order_index')

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Question.objects.filter(chapter_id=chapter_id)

class ScoreCreateView(generics.CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)