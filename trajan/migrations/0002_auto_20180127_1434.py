# Generated by Django 2.0.1 on 2018-01-27 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trajan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_dateTime', models.DateTimeField(verbose_name='visit date')),
                ('visit_chiefComplaint', models.CharField(max_length=256)),
                ('visit_complaintDuration', models.CharField(max_length=64)),
                ('visit_complaintFrequency', models.CharField(max_length=64)),
                ('visit_complaintQuality', models.CharField(max_length=128)),
                ('visit_complaintSymptoms', models.CharField(max_length=512)),
                ('visit_complaintLocation', models.CharField(max_length=64)),
                ('visit_aggravatingFactors', models.CharField(max_length=256)),
                ('visit_alleviatingFactors', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AddField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trajan.Patient'),
        ),
    ]
