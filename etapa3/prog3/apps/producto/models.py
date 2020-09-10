from django.db import models

# Create your models here.
class Categoria(models.Model):

    name = models.CharField(max_length=150, verbose_name='Nombre de la Categoría',unique=True,
                blank=False, null=False)
    

    def __str__(self):
        return '{}'.format(self.name)
    

    def save(self):
        self.name = self.name.upper()
        super(Categoria,self).save()
    
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['name']