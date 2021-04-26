# Generated by Django 2.2 on 2021-04-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_socialnetworklink'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True, verbose_name='WhatsApp')),
                ('telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telegram ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='links.LinkBoard')),
            ],
        ),
        migrations.DeleteModel(
            name='SocialNetworkLink',
        ),
    ]