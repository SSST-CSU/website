# Generated by Django 2.0.2 on 2018-08-28 16:38

import ResourceBorrowingSystem.LaboratoryBorrowing.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ResourceBorrowingSystem', '0003_auto_20180827_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboratory', models.CharField(max_length=20, verbose_name='实验室')),
                ('duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='职务')),
            ],
            options={
                'verbose_name': '实验室管理员',
                'verbose_name_plural': '实验室借用申请',
            },
        ),
        migrations.CreateModel(
            name='ApplyUserGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Student_Grade', verbose_name='年级')),
            ],
            options={
                'verbose_name': '可申请年级',
                'verbose_name_plural': '可申请年级',
            },
        ),
        migrations.AddField(
            model_name='laboratoryborrowingapply',
            name='content',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='laboratoryborrowingapply',
            name='proof_document',
            field=models.FileField(blank=True, null=True, upload_to=ResourceBorrowingSystem.LaboratoryBorrowing.models.upload_to, verbose_name='附件'),
        ),
        migrations.AddField(
            model_name='laboratoryborrowingapply',
            name='seat_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='座位号'),
        ),
        migrations.AlterField(
            model_name='laboratoryborrowingapply',
            name='reason',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='申请理由'),
        ),
    ]
