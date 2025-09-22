from django.db import models
from django.contrib.auth.models import User

# Defines the school grade level, e.g., Class 8
class Class(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Class 8, Class 9")
    level = models.IntegerField(unique=True, help_text="e.g., 8, 9, 10 for ordering")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Classes"

# Defines a subject that belongs to a specific class
class Subject(models.Model):
    school_class = models.ForeignKey(Class, related_name='subjects', on_delete=models.CASCADE)
    name_en = models.CharField(max_length=100)
    name_od = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.school_class.name} - {self.name_en}"

# Defines a chapter that belongs to a subject
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, related_name='chapters', on_delete=models.CASCADE)
    title_en = models.CharField(max_length=150)
    title_od = models.CharField(max_length=150)
    order_index = models.IntegerField()
    
    def __str__(self):
        return self.title_en

# Defines a question/challenge that belongs to a chapter
class Question(models.Model):
    QUESTION_TYPES = [
        ('mcq', 'Multiple Choice'),
        ('scramble', 'Word Scramble'),
        ('fill_blank', 'Fill in the Blanks'),
        ('match', 'Matching Pairs'),
    ]
    chapter = models.ForeignKey(Chapter, related_name='questions', on_delete=models.CASCADE)
    question_text_en = models.TextField()
    question_text_od = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='mcq')
    is_boss = models.BooleanField(default=False)
    blank_answer = models.CharField(max_length=100, blank=True, null=True)
    scramble_word = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question_text_en[:50]

# Defines a multiple-choice option for a question
class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text_en = models.CharField(max_length=255)
    option_text_od = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.option_text_en

# Defines a pair for a matching game question
class MatchPair(models.Model):
    question = models.ForeignKey(Question, related_name='match_pairs', on_delete=models.CASCADE)
    item_a = models.CharField(max_length=255)
    item_b = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.item_a} = {self.item_b}"
        
# Defines a user's score record
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    played_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.score}"