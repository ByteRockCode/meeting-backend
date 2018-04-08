# Generated by Django 2.0.3 on 2018-04-07 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compromise',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('description', models.TextField()),
                (
                    'company',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='compromises',
                        to='companies.Company',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('creator', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'guests',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('motive', models.CharField(max_length=255)),
                ('from_datetime', models.DateTimeField()),
                ('to_datetime', models.DateTimeField()),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('companies', models.ManyToManyField(to='companies.Company')),
                ('guests', models.ManyToManyField(through='meetings.Guest', to='profiles.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='meeting',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='meetings.Meeting',
            ),
        ),
        migrations.AddField(
            model_name='guest',
            name='profile',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='profiles.Profile',
            ),
        ),
        migrations.AddField(
            model_name='compromise',
            name='meeting',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='compromises',
                to='meetings.Meeting',
            ),
        ),
        migrations.AddField(
            model_name='agreement',
            name='meeting',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='agreements',
                to='meetings.Meeting',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together={('meeting', 'profile')},
        ),
    ]