# Generated by Django 5.1.3 on 2024-11-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_customuser_recommend_company_recommend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='recommend',
        ),
        migrations.AddField(
            model_name='customuser',
            name='recommend',
            field=models.CharField(default=''),
        ),
    ]