# Generated by Django 3.2.5 on 2021-07-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadry', '0002_alter_employee_pesel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='health_exam_expires_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='health_exam_file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='id_card_no',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='ohs_expires_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='passport_no',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_no',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_netto',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='viza_expires_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pesel',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
