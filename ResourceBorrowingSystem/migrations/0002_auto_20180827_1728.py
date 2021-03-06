# Generated by Django 2.0.7 on 2018-08-27 09:28

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
        ('ResourceBorrowingSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '申请理由',
                'verbose_name_plural': '申请理由',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '实验室',
                'verbose_name_plural': '实验室',
            },
        ),
        migrations.CreateModel(
            name='LaboratoryBorrowingApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_id', models.IntegerField(verbose_name='申请编号')),
                ('room', models.CharField(max_length=20, verbose_name='申请实验室')),
                ('apply_time', models.DateTimeField(verbose_name='申请提交时间')),
                ('update_time', models.DateTimeField(verbose_name='申请变更时间')),
                ('reason_type', models.CharField(max_length=20, verbose_name='申请类型')),
                ('reason', models.TextField(max_length=500, verbose_name='申请理由')),
                ('start_time', models.DateTimeField(verbose_name='申请开始时间')),
                ('end_time', models.DateTimeField(verbose_name='申请结束时间')),
                ('stat', models.CharField(max_length=30, verbose_name='申请状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='UserManagement.User', verbose_name='申请人')),
            ],
            options={
                'verbose_name': '实验室借用申请',
                'verbose_name_plural': '实验室借用申请',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='laboratoryborrowingapply',
            unique_together={('apply_id', 'stat')},
        ),
    ]
