from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name=models.CharField(max_length=24)
  last_name=models.CharField(max_length=24)
  email=models.EmailField()
  mobile=models.CharField(max_length=12)
  dob=models.DateField()
  gender_choices=(
    ('M','Male'),
    ('F','Female'),
    ('O','Others')
  )
  gender=models.CharField(max_length=1,choices=gender_choices)
  address = models.CharField(max_length=255, default='Default Address')  
  country_choices=(
    ('India','India'),
    ('USA','USA'),
    ('UK','UK'),
    ('Australia','Australia'),
    ('Canada','Canada'),
    ('Japan','Japan'),
    ('China','China'),
    ('Russia','Russia'),
    ('Germany','Germany'),
    ('France','France'),
    ('Italy','Italy'),
    ('Spain','Spain'),
    ('Portugal','Portugal'),
    ('Brazil','Brazil'),
    ('Argentina','Argentina'),
    ('Mexico','Mexico'),
    ('South Africa','South Africa'),
    ('South Korea','South Korea'),
    ('North Korea','North Korea'),)
  country=models.CharField(max_length=24,choices=country_choices)
  city_choices=(
    ('Mumbai','Mumbai'),
    ('Delhi','Delhi'),
    ('Bangalore','Bangalore'),
    ('Chennai','Chennai'),
    ('Kolkata','Kolkata'),
    ('Hyderabad','Hyderabad'),
    ('Ahmedabad','Ahmedabad'),
    ('Surat','Surat'),
    ('Pune','Pune'),
    ('Jaipur','Jaipur'),
    ('Lucknow','Lucknow'),
    ('Kanpur','Kanpur'),  
  )
  city=models.CharField(max_length=24,choices=city_choices)
  SKILL_CHOICES = (
        ('AWS', 'AWS'),
        ('DevOps', 'DevOps'),
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Middleware', 'Middleware'),
        ('QA-Automation', 'QA-Automation'),
        ('WebServices', 'WebServices'),
    )
  skills = models.CharField(max_length=24, choices=SKILL_CHOICES)

  def __str__(self):
    return self.first_name + " " + self.last_name
