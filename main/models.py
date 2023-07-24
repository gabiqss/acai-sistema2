from django.db import models


class Sorvete(models.Model):

    sabor_creme = (
        ('Açaí', 'Açaí'),
        ('Cupuaçu', 'Cupuaçu')
    )

    sabor = models.CharField(
        max_length=10,
        choices=sabor_creme,
        default='Açaí',
    )

    sabor_cobertura = (
        ('Chocolate', 'Chocolate'),
        ('Morango', 'Morango'),
        ('Caramelo', 'Caramelo'),
        ('Leite Condensado', 'Leite condensado')
    )

    cobertura = models.CharField(
        max_length=20,
        choices=sabor_cobertura,
        default='Leite Condensado',
    )

    tipo_tamanho = (
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
        ('Barca', 'Barca')
    )

    tamanho = models.CharField(
        max_length=10,
        choices=tipo_tamanho,
        default='Médio',
    )


    def __str__(self):
        return self.sabor