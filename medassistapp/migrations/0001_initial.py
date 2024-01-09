# Generated by Django 4.1.6 on 2023-11-08 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentdate', models.CharField(default='', max_length=200)),
                ('currenttime', models.CharField(default='', max_length=200)),
                ('ansdata', models.CharField(default='', max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('icon', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=100)),
                ('dob', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('emailid', models.CharField(default='', max_length=100)),
                ('mobileno', models.CharField(default='', max_length=100)),
                ('qualification', models.CharField(default='', max_length=100)),
                ('photograph', models.ImageField(upload_to='static/')),
                ('password', models.CharField(default='', max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('username', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=200)),
                ('emailid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('dob', models.CharField(default='', max_length=200)),
                ('mobileno', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnumber', models.CharField(default='', max_length=200)),
                ('question', models.CharField(default='', max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.category')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Timings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttimings', models.CharField(default='', max_length=100)),
                ('endtimings', models.CharField(default='', max_length=100)),
                ('days', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='', max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subquestionnumber', models.CharField(default='', max_length=200)),
                ('subquestiontext', models.CharField(default='', max_length=200)),
                ('subquestion', models.CharField(default='', max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.category')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.doctors')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentdate', models.CharField(default='', max_length=200)),
                ('currenttime', models.CharField(default='', max_length=200)),
                ('tests', models.CharField(default='', max_length=200)),
                ('diet', models.CharField(default='', max_length=200)),
                ('medicine', models.CharField(default='', max_length=200)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.answers')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctors',
            name='states',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.states'),
        ),
        migrations.AddField(
            model_name='city',
            name='states',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.states'),
        ),
        migrations.AddField(
            model_name='answers',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.doctors'),
        ),
        migrations.AddField(
            model_name='answers',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medassistapp.patient'),
        ),
    ]
