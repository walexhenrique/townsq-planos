# Generated by Django 4.1.3 on 2022-11-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="iam",
            field=models.CharField(
                choices=[
                    ("S", "Selecione"),
                    ("Q", "Quero ser síndico"),
                    ("M", "Síndico morador"),
                    ("P", "Síndico profissional"),
                ],
                default="S",
                max_length=1,
                verbose_name="Eu sou*",
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="solution",
            field=models.CharField(
                choices=[
                    ("S", "Selecione"),
                    ("T", "TownSq Essencial"),
                    ("A", "TownSq Administração Digital"),
                ],
                default="S",
                max_length=1,
                verbose_name="Em qual solução da TownSq você tem interesse?*",
            ),
        ),
    ]
