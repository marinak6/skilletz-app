# Generated by Django 2.1.7 on 2019-02-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='computing_id',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='graduation_year',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(choices=[('Undeclared', 'Undeclared'), ('Arts and Sciences', (('African American & African Studies', 'African American & African Studies'), ('American Studies', 'American Studies'), ('Anthropology', 'Anthropology'), ('Art History', 'Art History'), ('Art, Studio', 'Art, Studio'), ('Astronomy', 'Astronomy'), ('Astronomy-Physics', 'Astronomy-Physics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Chinese Language & Literature', 'Chinese Language & Literature'), ('Classics', 'Classics'), ('Cognitive Science', 'Cognitive Science'), ('Comparative Literature', 'Comparative Literature'), ('Computer Science', 'Computer Science'), ('Drama', 'Drama'), ('East Asian Studies', 'East Asian Studies'), ('Economics', 'Economics'), ('English', 'English'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Thought & Practice', 'Environmental Thought & Practice'), ('French', 'French'), ('German', 'German'), ('Global Studies', 'Global Studies'), ('History', 'History'), ('Human Biology', 'Human Biology'), ('Italian', 'Italian'), ('Japanese Language & Literature', 'Japanese Language & Literature'), ('Jewish Studies', 'Jewish Studies'), ('Latin American Studies', 'Latin American Studies'), ('Linguistics', 'Linguistics'), ('Mathematics', 'Mathematics'), ('Media Studies', 'Media Studies'), ('Medieval Studies', 'Medieval Studies'), ('Middle Eastern and South Asian Languages and Cultures', 'Middle Eastern and South Asian Languages and Cultures'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political and Social Thought', 'Political and Social Thought'), ('Political Philosophy, Policy, and Law', 'Political Philosophy, Policy, and Law'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages and Literatures', 'Slavic Languages and Literatures'), ('Sociology', 'Sociology'), ('South Asian Studies', 'South Asian Studies'), ('Spanish', 'Spanish'), ('Statistics', 'Statistics'), ('Teacher Education', 'Teacher Education'), ('Women, Gender, and Sexuality', 'Women, Gender, and Sexuality'))), ('School of Engineering and Applied Science', (('Aerospace Engineering', 'Aerospace Engineering'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Computer Science', 'Computer Science'), ('Electrical Engineering', 'Electrical Engineering'), ('Engineering Science', 'Engineering Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Systems Engineering', 'Systems Engineering'))), ('McIntire Schoole of Commerce', (('Accounting', 'Accounting'), ('Finance', 'Finance'), ('Information Technology', 'Information Technology'), ('Management', 'Management'), ('Marketing', 'Marketing'))), ('School of Architecture', (('Architectural History', 'Architectural History'), ('Architecture', 'Architecture'), ('Urban & Environmental Planning', 'Urban & Environmental Planning'))), ('School of Nursing', (('Bachelor of Science in Nursing (BSN)', 'Bachelor of Science in Nursing (BSN)'),)), ('Batten School of Leadership and Public Policy', (('B.A. in Public Policy and Leadership', 'B.A. in Public Policy and Leadership'),)), ('Curry School of Education', (('Kinesiology', 'Kinesiology'), ('Speech Communications Disorders Major', 'Speech Communications Disorders Major'), ('Youth & Social Innovation Major', 'Youth & Social Innovation Major'), ('Elementary Education', 'Elementary Education'), ('Special Education', 'Special Education'), ('Foreign Language Education', 'Foreign Language Education'), ('English as a Second Language Education', 'English as a Second Language Education'), ('English Education', 'English Education'), ('Mathematics Education', 'Mathematics Education'), ('Science Education', 'Science Education'), ('Social Studies Education', 'Social Studies Education')))], default='Undeclared', max_length=100),
        ),
    ]
