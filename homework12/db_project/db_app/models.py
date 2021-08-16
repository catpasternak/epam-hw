from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Teacher({self.first_name} {self.last_name})"


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Student({self.first_name} {self.last_name})"


class Homework(models.Model):
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"Homework({self.text})"


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"HomeworkResult({self.solution})"
