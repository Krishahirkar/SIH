from rest_framework import serializers
from .models import Class, Subject, Chapter, Question, Option, MatchPair, Score

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'level']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name_en', 'name_od']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title_en', 'title_od', 'order_index']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_text_en', 'option_text_od', 'is_correct']

class MatchPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPair
        fields = ['id', 'item_a', 'item_b']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    match_pairs = MatchPairSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id', 'question_text_en', 'question_text_od', 'question_type', 
            'is_boss', 'blank_answer', 'scramble_word', 'options', 'match_pairs'
        ]

class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Score
        fields = ['id', 'user', 'score', 'played_at']