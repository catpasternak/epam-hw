# Generated by Django 3.2.6 on 2021-08-16 12:01
import datetime

from django.db import migrations


def add_teacher(apps, schema_editor):
    Teacher = apps.get_model("db_app", "Teacher")
    Teacher.objects.bulk_create(
        [
            Teacher(first_name="Remus", last_name="Lupin"),
            Teacher(first_name="Severus", last_name="Snape"),
        ]
    )


def add_student(apps, schema_editor):
    Student = apps.get_model("db_app", "Student")
    Student.objects.bulk_create(
        [
            Student(first_name="Ron", last_name="Weasley"),
            Student(first_name="Harry", last_name="Potter"),
        ]
    )


def add_homework(apps, schema_editor):
    Homework = apps.get_model("db_app", "Homework")
    Homework.objects.bulk_create(
        [
            Homework(
                text="Boggarts essay", deadline=datetime.timedelta(days=7), teacher_id=1
            ),
            Homework(
                text="Poison recipe", deadline=datetime.timedelta(days=7), teacher_id=2
            ),
        ]
    )


def add_result(apps, schema_editor):
    HomeworkResult = apps.get_model("db_app", "HomeworkResult")
    HomeworkResult.objects.bulk_create(
        [
            HomeworkResult(homework_id=1, solution="This is an essay", student_id=1),
            HomeworkResult(
                homework_id=1, solution="This is another essay", student_id=2
            ),
            HomeworkResult(
                homework_id=2, solution="This is a poison recipe", student_id=2
            ),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("db_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_teacher),
        migrations.RunPython(add_student),
        migrations.RunPython(add_homework),
        migrations.RunPython(add_result),
    ]
