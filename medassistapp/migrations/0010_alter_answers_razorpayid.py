# Generated by Django 4.1.6 on 2023-11-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medassistapp', '0009_alter_answers_razorpayid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='razorpayid',
            field=models.CharField(blank=True, default=None, max_length=4000),
        ),
    ]