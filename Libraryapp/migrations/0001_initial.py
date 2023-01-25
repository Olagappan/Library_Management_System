# Generated by Django 4.1.4 on 2023-01-19 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Books_Name', models.CharField(max_length=50)),
                ('Author_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Name', models.CharField(max_length=50)),
                ('Stud_pass', models.CharField(max_length=50)),
                ('Stud_Phno', models.IntegerField()),
                ('Stud_Sem', models.IntegerField()),
                ('Stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.IntegerField()),
                ('End_Date', models.IntegerField()),
                ('Book_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.books')),
                ('Stud_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='Course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.course'),
        ),
    ]
