# Generated by Django 4.2.7 on 2024-01-29 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('dloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('grade', models.IntegerField(primary_key=True, serialize=False)),
                ('high_sal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_sal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('hiredate', models.DateField()),
                ('sal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]