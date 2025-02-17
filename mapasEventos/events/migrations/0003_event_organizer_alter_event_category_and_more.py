# Generated by Django 5.0.7 on 2024-07-10 00:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('music', 'Música'), ('show', 'Show'), ('museum', 'Museu'), ('theater', 'Teatro')], max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='language',
            field=models.CharField(choices=[('pt', 'Portuguese'), ('de', 'German'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('nl', 'Dutch'), ('sv', 'Swedish')], max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(choices=[('free', 'Gratuito'), ('paid', 'Pago')], max_length=10),
        ),
    ]
