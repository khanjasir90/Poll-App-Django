# Generated by Django 3.2.7 on 2021-11-04 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=1000)),
                ('choice_one', models.CharField(max_length=1000)),
                ('choice_two', models.CharField(max_length=1000)),
                ('choice_three', models.CharField(max_length=1000)),
                ('choice_four', models.CharField(max_length=1000)),
                ('choice_one_vote', models.IntegerField(max_length=100)),
                ('choice_two_vote', models.IntegerField(max_length=100)),
                ('choice_three_vote', models.IntegerField(max_length=100)),
                ('choice_four_vote', models.IntegerField(max_length=100)),
                ('poll_date', models.DateField()),
                ('poll_status', models.BooleanField()),
            ],
        ),
    ]
