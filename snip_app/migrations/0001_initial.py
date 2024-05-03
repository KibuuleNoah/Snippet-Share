# Generated by Django 3.0.6 on 2021-01-06 04:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled', max_length=40)),
                ('text', models.TextField()),
                ('link_code', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('lang', models.CharField(choices=[('text', 'None'), ('Markup', 'markup'), ('html', 'html'), ('CSS', 'css'), ('C-like', 'clike'), ('JavaScript', 'javascript, js'), ('Arduino', 'arduino'), ('Bash', 'bash, shell'), ('BASIC', 'basic'), ('C', 'c'), ('C#', 'csharp, cs, dotnet'), ('Cpp', 'cpp'), ('CoffeeScript', 'coffeescript, coffee'), ('CMake', 'cmake'), ('Clojure', 'clojure'), ('Django/Jinja2', 'django, jinja2'), ('Docker', 'docker, dockerfile'), ('Git', 'git'), ('GameMaker Language', 'gml, gamemakerlanguage'), ('Go', 'go'), ('GraphQL', 'graphql'), ('Groovy', 'groovy'), ('Haml', 'haml'), ('HTTP', 'http'), ('Icon', 'icon'), ('Java', 'java'), ('JavaDoc', 'javadoc'), ('JSDoc', 'jsdoc'), ('JSON', 'json'), ('JSONP', 'jsonp'), ('JSON5', 'json5'), ('Kotlin', 'kotlin'), ('LaTeX', 'latex, tex, context'), ('Latte', 'latte'), ('Less', 'less'), ('LiveScript', 'livescript'), ('Lua', 'lua'), ('Makefile', 'makefile'), ('Markdown', 'markdown, md'), ('MATLAB', 'matlab'), ('nginx', 'nginx'), ('Objective-C', 'objectivec'), ('OpenCL', 'opencl'), ('Parser', 'parser'), ('Pascal', 'pascal, objectpascal'), ('Perl', 'perl'), ('PHP', 'php'), ('PL/SQL', 'plsql'), ('PowerShell', 'powershell'), ('Pug', 'pug'), ('Python', 'python, py'), ('R', 'r'), ('React JSX', 'jsx'), ('React TSX', 'tsx'), ('Regex', 'regex'), ('Ruby', 'ruby, rb'), ('Rust', 'rust'), ('SAS', 'sas'), ('Sass (Sass)', 'sass'), ('Sass (Scss)', 'scss'), ('Scala', 'scala'), ('SQL', 'sql'), ('Stylus', 'stylus'), ('Swift', 'swift'), ('Twig', 'twig'), ('TypeScript', 'typescript, ts'), ('Velocity', 'velocity'), ('vim', 'vim'), ('Visual Basic', 'visual-basic, vb'), ('Wiki markup', 'wiki'), ('YAML', 'yaml, yml'), ('Zig', 'zig')], default='text', max_length=18)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
