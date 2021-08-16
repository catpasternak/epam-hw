import os

PROJECT_NAME = "db_project"


def main():
    import csv

    from db_app.models import Homework, HomeworkResult, Student, Teacher

    column_names = ["Student name", "Creation date", "Teacher name"]
    result_objects = HomeworkResult.objects.all()
    with open("report.csv", "w") as csv_file:
        writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(column_names)
        for object in result_objects:
            student_obj = Student.objects.get(id=object.student_id)
            student_field = student_obj.first_name + " " + student_obj.last_name
            created_field = object.created
            homework_obj = Homework.objects.get(id=object.homework_id)
            teacher_obj = homework_obj.teacher
            teacher_field = teacher_obj.first_name + " " + teacher_obj.last_name
            row = [student_field, created_field, teacher_field]
            writer.writerow(row)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_NAME)
    import django

    django.setup()
    main()
