from django.db import models

# Create your models here.
class EmployeePromotion(models.Model):
    Department=models.CharField(max_length=100)
    Education=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Recruitment=models.CharField(max_length=100)
    No_Of_Trainings=models.IntegerField()
    Age=models.IntegerField()
    Previous_Year_Ratings=models.IntegerField()
    Length_Of_Service=models.IntegerField()
    Awards_Won=models.IntegerField()
    Average_Trainings=models.IntegerField()
    Employee_Promotion=models.IntegerField()
