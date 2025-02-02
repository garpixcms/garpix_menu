# Generated by Django 4.2 on 2024-10-14 14:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('garpix_page', '0005_auto_20230210_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basecomponent',
            options={'ordering': ('created_at', 'title'), 'verbose_name': 'Компонент | Component', 'verbose_name_plural': 'Компоненты | Components'},
        ),
        migrations.AlterModelOptions(
            name='basepage',
            options={'base_manager_name': 'objects', 'ordering': ('created_at', 'title'), 'verbose_name': 'Структура страниц | Pages structure', 'verbose_name_plural': 'Структура страниц | Pages structure'},
        ),
        migrations.AlterModelOptions(
            name='garpixpagesiteconfiguration',
            options={'verbose_name': 'Настройки | Settings', 'verbose_name_plural': 'Настройки | Settings'},
        ),
        migrations.AlterModelOptions(
            name='grapesjshtmlcomponent',
            options={'verbose_name': 'GrapesJs компонент | GrapesJs component', 'verbose_name_plural': 'GrapesJs компоненты | GrapesJs components'},
        ),
        migrations.AlterModelOptions(
            name='pagecomponent',
            options={'ordering': ('view_order',), 'verbose_name': 'Компонент страницы | Page component', 'verbose_name_plural': 'Компоненты страницы | Pages components'},
        ),
        migrations.AlterModelOptions(
            name='seotemplate',
            options={'ordering': ['priority_order', 'id'], 'verbose_name': 'Шаблон для seo | SEO template', 'verbose_name_plural': 'Шаблоны для seo | SEO templates'},
        ),
        migrations.AddField(
            model_name='basecomponent',
            name='html_id',
            field=models.CharField(blank=True, default='', max_length=255, validators=[django.core.validators.RegexValidator(code='invalid', message='Допустимы только латинские буквы, цифры, дефисы и знаки подчеркивания', regex='^[a-zA-Z0-9\\-_]*$')], verbose_name='HTML ID'),
        ),
        migrations.AddField(
            model_name='basecomponent',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Запись удалена'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='url',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Полный URL страницы'),
        ),
        migrations.AlterField(
            model_name='basecomponent',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='basepage',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
