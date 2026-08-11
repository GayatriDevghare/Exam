from django.db import models

# Questions table
class ExamInfo(models.Model):
    qno = models.IntegerField(unique=True, primary_key=True)
    qtext = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    subject = models.CharField(max_length=60)
    ans = models.CharField(max_length=200)

    class Meta:
        db_table = 'examinfo'


# Student / User table
class UserData(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'userdata'


# Result table
class Result(models.Model):
    username = models.ForeignKey(UserData, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    marks = models.IntegerField()

    class Meta:
        db_table = 'result'