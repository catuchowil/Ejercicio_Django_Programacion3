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



class Producto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre Producto', unique=True,
                blank=False, null=False)
    cate = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name='Categoria Producto')
    pre_uni = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,
                    verbose_name='Precio Unitario')

    def __str__(self):
        return '{}'.format(self.name)
    

    def save(self):
        self.name = self.name.upper()
        super(Producto,self).save()


    class Meta:
        verbose_name_plural = 'Productos'
        ordering = ['name']