from django.db import models


class Base(models.Model):
    criado_em = models.DateField('Criação', auto_now_add=True)
    modificado_em = models.DateField('Atualização', auto_now=True)
    lido = models.BooleanField('Lido')

    class Meta:
        abstract = True


class Book(Base):
    titulo = models.CharField('Titulo', max_length=100)
    resenha = models.CharField('Resenha', max_length=255)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.titulo

