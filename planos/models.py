from django.db import models


class Attendance(models.Model):

    IAM_CHOICES = (
        ('S', 'Selecione'),
        ('Q', 'Quero ser síndico'),
        ('M', 'Síndico morador'),
        ('P', 'Síndico profissional'),
    )

    CONDO_SIZE_CHOICES = (
        ('S', 'Selecione'),
        ('P', 'Até 50 unidades'),
        ('M', 'de 50 até 100 unidades'),
        ('G', 'de 100 até 200 unidades'),
    )
    NUMBER_CONDOS_CHOICES = (
        ('S', 'Selecione'),
        ('N', 'Nenhum'),
        ('P', 'Até 1 condomínio'),
        ('M', '2 a 3 condomínios'),
        ('G', '4 a 6 condomínios'),
    )
    SOLUTION_CHOICES = (
        ('S', 'Selecione'),
        ('T', 'TownSq Essencial'),
        ('A', 'TownSq Administração Digital'),
    )

    name = models.CharField(verbose_name='Nome*', max_length=255)
    iam = models.CharField(max_length=1, choices=IAM_CHOICES, default='S', verbose_name='Eu sou*')
    email = models.EmailField(verbose_name='Email*')
    phone_number = models.CharField(max_length=30, verbose_name='Telefone*')
    condo_size = models.CharField(max_length=1, choices=CONDO_SIZE_CHOICES, default='S', verbose_name='Tamanho do condomínio')
    number_condos = models.CharField(max_length=1, choices=NUMBER_CONDOS_CHOICES, default='S', verbose_name='Quantos condomínios você administra?')
    solution = models.CharField(max_length=1, default='S', choices=SOLUTION_CHOICES, verbose_name='Em qual solução da TownSq você tem interesse?*')

    def __str__(self) -> str:
        return self.name
