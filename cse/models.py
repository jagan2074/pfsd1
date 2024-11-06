from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title


'''select_branch = [('cse', 'Computer Science and Engineering'), ('ece', 'Electronics and Communication Engineering')]
select_subject = [('pfsd', 'Professional Software Development'), ('mswd', 'Mobile Software Development')]


class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=100)  # New field for student's name
    branch = models.CharField(max_length=3, choices=select_branch)
    subject = models.CharField(max_length=4, choices=select_subject)

    def __str__(self):
        return f"Student ID: {self.sid}, Name: {self.name}, Branch: {self.branch}, Subject: {self.subject}" '''

from django.db import models

SELECT_BRANCH = [
    ('cse', 'Computer Science and Engineering'),
    ('ece', 'Electronics and Communication Engineering')
]

SELECT_SUBJECT = [
    ('pfsd', 'Professional Software Development'),
    ('mswd', 'Mobile Software Development')
]


class students(models.Model):
    SID = models.IntegerField()
    NAME = models.CharField(max_length=100)
    BRANCH = models.CharField(max_length=3, choices=SELECT_BRANCH)
    SUBJECT = models.CharField(max_length=4, choices=SELECT_SUBJECT)

    def __str__(self):
        return f"Student ID: {self.SID}, Name: {self.NAME}, Branch: {self.get_BRANCH_display()}, Subject: {self.get_SUBJECT_display()}"
