from django.db import models
from django . urls import reverse

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    des = models.TextField(blank=True)
    img = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('e_app:productByCategory', args=[self.slug])

    def __str__(self):
        return self.name


class products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='products', blank=True)
    var = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('e_app:prodCatdetail', args=[self.var.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'products'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
