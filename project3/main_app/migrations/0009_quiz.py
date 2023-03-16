# Generated by Django 4.1.7 on 2023-03-16 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_category_imagepath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qustion', models.TextField(max_length=500)),
                ('option1', models.CharField(max_length=150)),
                ('option2', models.CharField(max_length=150)),
                ('option3', models.CharField(max_length=150)),
                ('option4', models.CharField(max_length=150)),
                ('correctAnswer', models.CharField(max_length=150)),
                ('isApproved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
            ],
        ),
    ]