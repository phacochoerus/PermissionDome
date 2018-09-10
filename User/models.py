from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    name = models.CharField(max_length=128)
    age = models.CharField(max_length=16)
    def __str__(self):
        return self.username


class Students(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16)
    def __str__(self):
        return self.user.username
    class Meta:
        permissions = (
            ("User.Students.studentsviewset.post","User.Students.新增"),
            ("User.Students.studentsviewset.delete","User.Students.删除"),
            ("User.Students.studentsviewset.put","User.Students.修改"),
            ("User.Students.studentsviewset.get","User.Students.查看列表"),
            ("User.Students.studentsviewset.get+","User.Students.查看详细"),
        )

class Teachers(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    city = models.CharField(max_length=16)
    def __str__(self):
        return self.user.username
    class Meta:
        permissions = (
            ("User.Teachers.teachersviewset.post","User.Teachers.新增"),
            ("User.Teachers.teachersviewset.delete","User.Teachers.删除"),
            ("User.Teachers.teachersviewset.put","User.Teachers.修改"),
            ("User.Teachers.teachersviewset.get","User.Teachers.查看列表"),
            ("User.Teachers.teachersviewset.get+","User.Teachers.查看详细"),
        )

class Leader(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    pos = models.CharField(max_length=12)
    def __str__(self):
        return self.user.username

