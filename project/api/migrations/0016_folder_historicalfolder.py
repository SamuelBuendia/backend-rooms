# Generated by Django 2.2 on 2021-11-18 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0015_space_functionarys'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFolder',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('expiration_date', models.DateField(null=True)),
                ('guide_file', models.TextField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('functionary', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.Functionary')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.Room')),
            ],
            options={
                'verbose_name': 'historical folder',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('expiration_date', models.DateField(null=True)),
                ('guide_file', models.FileField(upload_to='Uploaded Files/')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('functionary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='functionaryfolder', to='api.Functionary')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folderroom', to='api.Room')),
            ],
            options={
                'verbose_name': 'folder',
                'verbose_name_plural': 'folders',
                'ordering': ['-id'],
            },
        ),
    ]
