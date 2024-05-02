# Generated by Django 4.2.11 on 2024-04-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=24)),
                ('last_name', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=12)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('address', models.CharField(default='Default Address', max_length=255)),
                ('country', models.CharField(choices=[('India', 'India'), ('USA', 'USA'), ('UK', 'UK'), ('Australia', 'Australia'), ('Canada', 'Canada'), ('Japan', 'Japan'), ('China', 'China'), ('Russia', 'Russia'), ('Germany', 'Germany'), ('France', 'France'), ('Italy', 'Italy'), ('Spain', 'Spain'), ('Portugal', 'Portugal'), ('Brazil', 'Brazil'), ('Argentina', 'Argentina'), ('Mexico', 'Mexico'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('North Korea', 'North Korea')], max_length=24)),
                ('city', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Chennai', 'Chennai'), ('Kolkata', 'Kolkata'), ('Hyderabad', 'Hyderabad'), ('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Pune', 'Pune'), ('Jaipur', 'Jaipur'), ('Lucknow', 'Lucknow'), ('Kanpur', 'Kanpur')], max_length=24)),
                ('skills', models.CharField(choices=[('AWS', 'AWS'), ('DevOps', 'DevOps'), ('Full Stack Developer', 'Full Stack Developer'), ('Middleware', 'Middleware'), ('QA-Automation', 'QA-Automation'), ('WebServices', 'WebServices')], max_length=24)),
            ],
        ),
    ]