from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Questions(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="questions")
    question = models.CharField("Question", max_length=300)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["-create"]

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"q_slug": self.slug})

    def __str__(self):
        return self.question


class Responses(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="responses")
    question = models.ForeignKey(Questions, verbose_name="Question", on_delete=models.CASCADE, related_name="response")
    answer = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"
        ordering = ["-create"]

    def __str__(self):
        return self.answer


class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="surveys")
    title = models.CharField("Survey", max_length=200)
    questions = models.ManyToManyField(Questions, verbose_name="Question", related_name='surveys')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    date_for_beginning = models.DateTimeField()
    date_for_end = models.DateTimeField()

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"
        ordering = ["-create"]

    def get_absolute_url(self):
        return reverse("survey_detail", kwargs={"s_slug": self.slug})

    def __str__(self):
        return self.title
