# Generated by Django 4.1.6 on 2023-11-22 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medassistapp', '0011_alter_answers_razorpayid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='razorpayid',
        ),
    ]
