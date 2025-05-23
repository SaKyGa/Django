# Generated by Django 5.2 on 2025-04-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_category_alter_post_image_post_catwgory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='catwgory',
            new_name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.tag'),
        ),
    ]
