# Generated by Django 4.2.7 on 2024-11-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BreakFast_app', '0013_dailysurvey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastingplan',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fastingplan',
            name='eating_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fastingplan',
            name='fasting_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fastingplan',
            name='plan_type',
            field=models.CharField(choices=[('16:8', '16:8 Intermittent Fasting'), ('18:6', '18:6 Intermittent Fasting'), ('20:4', '20:4 Intermittent Fasting'), ('5:2', '5:2 Diet'), ('CUSTOM', 'Custom Plan')], max_length=20),
        ),
    ]
