# Generated by Django 4.2.4 on 2023-08-29 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('question_number', models.PositiveIntegerField()),
                ('question_body', models.TextField()),
                ('test_tag', models.CharField(choices=[('Dass', 'DASS'), ('Mbti', 'MBTI')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MBTI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('score', models.TextField()),
                ('answers', models.JSONField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultation.customerprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DASS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('score', models.TextField()),
                ('answers', models.JSONField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='consultation.customerprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]